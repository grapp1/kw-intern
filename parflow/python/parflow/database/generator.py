r'''
This module provide the infrastructure to load and generate the Parflow
database structure as Python classes so IDE and runtime environment can
be used to query the help and constraints associated to each keys.
'''

import os
import yaml
import json
from datetime import datetime

# -----------------------------------------------------------------------------

def isField(key, definition):
  if key[0] == '_':
    return False

  value = definition[key]

  if '__doc__' in value:
    return False

  if 'help' in value:
    return True

  if '__field__' in value:
    return True

  return False

# -----------------------------------------------------------------------------

def isClass(key, definition):
  if key[0] == '_':
    return False

  value = definition[key]

  if '__doc__' in value:
    return True

  if 'help' in value:
    return False

  if '__field__' in value:
    return False

  return True

# -----------------------------------------------------------------------------

class PythonModule:
  def __init__(self, indent=2):
    self.content = [
      "r'''",
      "--- DO NOT EDIT ---",
      "File automatically generated - any manual change will be lost",
      f"Generated on {datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}",
      "'''",
      "from .core import PFDBObj",
    ]
    self.strIndent = ' '*indent

  def addLine(self, content=''):
    self.content.append(content)

  def addSeparator(self):
    self.addLine()
    self.addLine(f"# {'-'*78}")
    self.addLine()

  def addClass(self, className, classDefinition):
    classKeys = classDefinition.keys()
    classMembers = []
    fieldMembers = []
    classDetails = {}

    self.addSeparator()

    self.addLine(f'class {className}(PFDBObj):')
    if '__doc__' in classKeys:
      self.addComment(classDefinition['__doc__'], self.strIndent)

    for key in classDefinition:
      if isClass(key, classDefinition):
        classMembers.append(key)
      if isField(key, classDefinition):
        fieldMembers.append(key)

    if len(classMembers) + len(fieldMembers) > 0:
      self.addLine(f'{self.strIndent}def __init__(self):')
      for instance in classMembers:
        self.addLine(f'{self.strIndent*2}self.{instance} = {instance}()')
      for field in fieldMembers:
        self.addField(field, classDefinition[field], classDetails)
      if len(classDetails):
        detailsLines = json.dumps(classDetails, indent=2).splitlines()
        self.addLine(f'{self.strIndent*2}self._details = {detailsLines[0]}')
        for line in detailsLines[1:]:
          self.addLine(f'{self.strIndent*2}{line}')

    for classMember in classMembers:
      self.addClass(classMember, classDefinition[classMember])

  def addField(self, fieldName, fieldDefinition, classDetails):
    self.addLine(f"{self.strIndent*2}self.{fieldName} = {fieldDefinition['default'] if 'default' in fieldDefinition else 'None'}")
    classDetails[fieldName] = fieldDefinition

  def addComment(self, docContent, strIndent):
    self.addLine(f"{strIndent}'''")
    for line in docContent.splitlines():
      self.addLine(f'{strIndent}{line}')
    self.addLine(f"{strIndent}'''")

  def write(self, filePath, lineSeparator='\n'):
    # Ensure new line at the end
    if len(self.content[-1]):
      self.content.append('')

    with open(filePath, 'w') as output:
      output.write(lineSeparator.join(self.content))

  def print(self):
    # Ensure new line at the end
    if len(self.content[-1]):
      self.content.append('')

    print('\n'.join(self.content))

# -----------------------------------------------------------------------------
# Expected API to use
# -----------------------------------------------------------------------------

def generateModuleFromDefinitions(definitions):
  generatedModule = PythonModule()

  for yaml_file in definitions:
    with open(yaml_file) as file:
      yamlStruct = yaml.load(file, Loader=yaml.FullLoader)

      for rootKey in yamlStruct.keys():
        generatedModule.addClass(rootKey, yamlStruct[rootKey])

  return generatedModule

# -----------------------------------------------------------------------------

if __name__ == "__main__":
  coreDefinitions = ['core']
  basePath = os.path.dirname(os.path.abspath(__file__))
  defPath = os.path.join(basePath, 'definitions')
  definitionFiles = [os.path.join(defPath, f'{module}.yaml') for module in coreDefinitions]
  outputFilePath = os.path.join(basePath, 'generated.py')

  print('-'*80)
  print('Generate Parflow database module')
  print('-'*80)
  generatedModule = generateModuleFromDefinitions(definitionFiles)
  generatedModule.print()
  print('-'*80)
  generatedModule.write(outputFilePath)
  print('=> Done')

