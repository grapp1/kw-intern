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
    'wells',
    'phase',
    'timing',
    'run'
]
# -----------------------------------------------------------------------------

LEVELS = [
  '=',
  '-',
  '^',
  '"',
  '"',
  '"',
  '"',
]

def handleDomain(name, definition):
  indentStr = ' '*4
  lines = []
  listCount = 0

  if name == 'MandatoryValue':
    lines.append(f'{indentStr}The value is required')

  if name == 'IntValue':
    lines.append(f'{indentStr}The value must be an Integer')
    if definition and 'minValue' in definition:
      listCount += 1
      lines.append(
          f'{indentStr}  - with a value greater than or equal to {definition["minValue"]}')
    if definition and 'maxValue' in definition:
      listCount += 1
      lines.append(
          f'{indentStr}  - with a value less than or equal to {definition["maxValue"]}')

  if name == 'DoubleValue':
    lines.append(f'{indentStr}The value must be an Integer')
    if definition and 'minValue' in definition:
      listCount += 1
      lines.append(
          f'{indentStr}  - with a value greater than or equal to {definition["minValue"]}')
    if definition and 'maxValue' in definition:
      listCount += 1
      lines.append(
          f'{indentStr}  - with a value less than or equal to {definition["maxValue"]}')

  if name == 'EnumDomain':
    lines.append(
        f'{indentStr}The value must be one of the following options: {(", ".join(definition["enumList"]))}')

  if name == 'AnyString':
    lines.append(f'{indentStr}The value must be a string')

  if name == 'BoolDomain':
    lines.append(f'{indentStr}The value must be True or False')

  if listCount:
    lines.append('')

  return '\n'.join(lines)


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

    if key == '__value__':
      title = prefix

    warning = ''
    if '__rst__' in subSection:
      if 'name' in subSection['__rst__']:
        title = subSection['__rst__']['name']
      if 'warning' in subSection['__rst__']:
        warning = subSection['__rst__']['warning']
      if 'skip' in subSection['__rst__']:
        for subKey in subSection:
          if subKey[0] != '_' or subKey == '__value__':
            self.addSection(level, title, subKey, subSection[subKey])
        return

    self.addLine()
    self.addLine(title)
    self.addLine(LEVELS[level]*80)
    self.addLine()
    if warning:
      self.addLine('.. warning::')
      self.addLine(f'    {warning}')

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
      if 'default' in subSection:
        self.addLine(f':default: {subSection["default"]}')

      if 'domains' in subSection:
        self.addLine('.. note::')
        for domain in subSection['domains']:
          self.addLine(handleDomain(domain, subSection['domains'][domain]))
        self.addLine()

    else:
      # Keep adding sections
      for subKey in subSection:
        if subKey[0] != '_' or subKey == '__value__':
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
