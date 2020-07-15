r'''
This module provide the infrastructure to load and generate the Parflow
database structure as Python classes so IDE and runtime environment can
be used to query the help and constraints associated to each keys.
'''

import os, sys, traceback
import yaml
import json
from datetime import datetime

# -----------------------------------------------------------------------------
YAML_MODULES_TO_PROCESS = [
  'core',
  'geom',
  'solver',
  'wells',
  'timing',
  'phase',
  'bconditions',
  'run'
]
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

  if key[0] == '.':
    return False

  value = definition[key]

  if '__doc__' in value:
    return True

  if 'help' in value:
    return False

  if '__field__' in value:
    return False

  if '_dynamic' in value:
    return False

  return True

# -----------------------------------------------------------------------------

def isClassItem(key, definition):
  if key[0] == '.':
    return True

  return False

# -----------------------------------------------------------------------------

def jsonToPython(txt):
  return txt.replace(' true,', ' True,').replace(' false,', ' False,').replace(' null', ' None')

# -----------------------------------------------------------------------------

def yamlValue(yamlval):
  if isinstance(yamlval, str):
    try:
      return float(yamlval)
    except ValueError:
      return yamlval

  return yamlval

# -----------------------------------------------------------------------------

class ValidationSummary:
  def __init__(self):
    self.classNameCount = {}
    self.classCount = 0
    self.fieldCount = 0

  def addClass(self, className):
    self.classCount += 1
    if className in self.classNameCount:
      self.classNameCount[className] += 1
    else:
      self.classNameCount[className] = 1

    return self.classNameCount[className] - 1

  def getDeduplicateClassName(self, className, classDefinition=None):
    if classDefinition and '__class__' in classDefinition:
      return classDefinition['__class__']
    if className in self.classNameCount:
      return f'{className}_{self.classNameCount[className]}'
    return className

  def addField(self, fieldName):
    self.fieldCount += 1

  def getSummary(self, lineSeparator='\n'):
    content = [
        f'Created {self.classCount} classes',
    ]
    if len(self.classNameCount) == self.classCount:
      content.append(' => No class name duplication found')
    else:
      content.append(
          f' => We found overlapping classNames ({self.classCount - len(self.classNameCount)})')
      for name in self.classNameCount:
        if self.classNameCount[name] > 1:
          content.append(
              f'   + {name} was defined {self.classNameCount[name]} times')

    content.append(f'Defined {self.fieldCount} fields were found')
    return lineSeparator.join(content)

  def printSummary(self):
    print(self.getSummary())

# -----------------------------------------------------------------------------

class PythonModule:
  def __init__(self, indent=2):
    self.validationSummary = ValidationSummary()
    self.content = [
      "r'''",
      "--- DO NOT EDIT ---",
      "File automatically generated - any manual change will be lost",
      f"Generated on {datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}",
      "",
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
    try:
      classKeys = classDefinition.keys()
      classMembers = []
      fieldMembers = []
      classInstances = []
      classItems = []
      classDetails = {}
      classDynamicNames = {}

      self.addSeparator()

      dedupClassName = self.validationSummary.getDeduplicateClassName(className, classDefinition)
      self.validationSummary.addClass(className)

      self.addLine(f'class {dedupClassName}(PFDBObj):')
      if '__doc__' in classKeys:
        self.addComment(classDefinition['__doc__'], self.strIndent)

      if '_dynamic' in classKeys:
        classDynamicNames.append(classDefinition['_dynamic'])

      for key in classDefinition:
        if isClass(key, classDefinition):
          print(key)
          classMembers.append(key)
        if isField(key, classDefinition):
          fieldMembers.append(key)
        if key == '__class_instances__':
          classInstances = classDefinition['__class_instances__']
        if isClassItem(key, classDefinition):
          classItems.append(classDefinition[key])

      if len(classMembers) + len(fieldMembers) + len(classInstances) > 0:
        '''
          def __init__(self, parent=None):
            super().__init__(parent)
            self.Topology = Topology(self)
        '''
        self.addLine(f'{self.strIndent}def __init__(self, parent=None):')
        self.addLine(f'{self.strIndent*2}super().__init__(parent)')

        for instance in classMembers:
          self.addLine(
              f'{self.strIndent*2}self.{instance} = {self.validationSummary.getDeduplicateClassName(instance)}(self)')

        for instance in classInstances:
          self.addClassInstance(instance)

        for field in fieldMembers:
          self.addField(field, classDefinition[field], classDetails)

        self.addDynamicName(classDynamicNames)
        self.addDetails(classDetails)

      for classMember in classMembers:
        # Catch error
        if classMember == 'help':
          print(f'Invalid syntax: {className} must use __doc__ rather than help')
          sys.exit(1)
        self.addClass(classMember, classDefinition[classMember])

      for classItem in classItems:
        self.addClass(classItem['__class__'], classItem)

    except:
      # traceback.print_exc()
      print(f'Error when processing class {className}')

  def addDetails(self, classDetails):
    if len(classDetails):
      detailsLines = json.dumps(classDetails, indent=2).splitlines()
      self.addLine(f'{self.strIndent * 2}self._details = {detailsLines[0]}')
      for line in detailsLines[1:]:
        lineWithIndent = f'{self.strIndent * 2}{line}'
        self.addLine(jsonToPython(lineWithIndent))

  def addDynamicName(self, classDynamicNames):
    if len(classDynamicNames):
      dynamicLines = json.dumps(classDynamicNames, indent=2).splitlines()
      self.addLine(f'{self.strIndent * 2}self._dynamic = {dynamicLines[0]}')
      for line in dynamicLines[1:]:
        lineWithIndent = f'{self.strIndent * 2}{line}'
        self.addLine(jsonToPython(lineWithIndent))

  def addField(self, fieldName, fieldDefinition, classDetails):
    self.validationSummary.addField(fieldName)
    field_val = None
    if 'default' in fieldDefinition:
      field_val = yamlValue(fieldDefinition['default'])
      fieldDefinition['default'] = field_val

    if isinstance(field_val, str):
      self.addLine(f"{self.strIndent*2}self.{fieldName} = '{field_val}'")
    else:
      self.addLine(f"{self.strIndent * 2}self.{fieldName} = {field_val}")
    classDetails[fieldName] = fieldDefinition

  def addClassInstance(self, fieldName):
    self.addLine(
        f"{self.strIndent*2}self.{fieldName} = {fieldName}(self)")

  def addComment(self, docContent, strIndent):
    self.addLine(f"{strIndent}'''")
    for line in docContent.splitlines():
      self.addLine(f'{strIndent}{line}')
    self.addLine(f"{strIndent}'''")

  def getContent(self,  lineSeparator='\n'):
    self.content[4] = self.validationSummary.getSummary(lineSeparator)
    # Ensure new line at the end
    if len(self.content[-1]):
      self.content.append('')

    return lineSeparator.join(self.content)

  def write(self, filePath, lineSeparator='\n'):
    with open(filePath, 'w') as output:
      output.write(self.getContent(lineSeparator))

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
  coreDefinitions = YAML_MODULES_TO_PROCESS
  basePath = os.path.dirname(os.path.abspath(__file__))
  defPath = os.path.join(basePath, 'definitions')
  definitionFiles = [os.path.join(defPath, f'{module}.yaml') for module in coreDefinitions]
  outputFilePath = os.path.join(basePath, 'generated.py')

  print('-'*80)
  print('Generate Parflow database module')
  print('-'*80)
  generatedModule = generateModuleFromDefinitions(definitionFiles)
  print(generatedModule.validationSummary.getSummary())
  print('-'*80)
  generatedModule.write(outputFilePath)
