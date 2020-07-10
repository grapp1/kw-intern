r'''
This module provide the infrastructure to load and generate the Parflow
database structure as documentation files for Read The Docs.
'''

import os
import sys
import yaml
import json
from datetime import datetime

# -----------------------------------------------------------------------------
YAML_MODULES_TO_PROCESS = [
    'core',
    'geom',
    'solver',
    'run'
]
# -----------------------------------------------------------------------------

LEVELS = [
  '=',
  '-',
  '~',
  '~',
  '~',
  '~',
  '~',
]

class RSTModule:
  def __init__(self, title):
    self.content = [
        '*'*80,
        title,
        '*'*80,
    ]

  def addLine(self, content=''):
    self.content.append(content)

  def addSection(self, level, prefix, key, subSection):
    title = f'{prefix}.{key}' if prefix else key

    self.addLine()
    self.addLine(title)
    self.addLine(LEVELS[level]*80)
    self.addLine()

    leaf = False
    description = ''

    if 'help' in subSection:
      leaf = True
      description = subSection['help']

    if '__doc__' in subSection:
      description = subSection['__doc__']

    self.addLine(description)
    self.addLine()

    if leaf:
      # Need to process domains and more...
      pass
    else:
      # Keep adding sections
      for subKey in subSection:
        if subKey[0] != '_':
          self.addSection(level + 1, title, subKey, subSection[subKey])


  def getContent(self,  lineSeparator='\n'):
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
  generatedRST = RSTModule('ParFlow Key Documentation')

  for yaml_file in definitions:
    with open(yaml_file) as file:
      yamlStruct = yaml.load(file, Loader=yaml.FullLoader)

      for rootKey in yamlStruct.keys():
        generatedRST.addSection(0, '', rootKey, yamlStruct[rootKey])

  return generatedRST

# -----------------------------------------------------------------------------


if __name__ == "__main__":
  coreDefinitions = YAML_MODULES_TO_PROCESS
  basePath = os.path.dirname(os.path.abspath(__file__))
  defPath = os.path.join(basePath, 'definitions')
  definitionFiles = [os.path.join(
      defPath, f'{module}.yaml') for module in coreDefinitions]
  outputFilePath = os.path.join(basePath, '../../../docs/parflow_keys.rst')

  print('-'*80)
  print('Generate Parflow database documentation')
  print('-'*80)
  generatedModule = generateModuleFromDefinitions(definitionFiles)
  print('-'*80)
  generatedModule.write(outputFilePath)
