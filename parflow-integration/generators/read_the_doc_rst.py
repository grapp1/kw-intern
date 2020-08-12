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
    'netcdf',
    'bconditions',
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


def handle_domain(name, definition):
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

    if name == 'RequiresModule':
        lines.append(
            f'{indentStr}This key requires the availability of the following module(s) in ParFlow: {definition}')

    if name == 'Deprecated':
        lines.append('')
        lines.append('.. warning::')
        lines.append(f'    This key will be deprecated in v{definition}')

    if name == 'Removed':
        lines.append('')
        lines.append('.. warning::')
        lines.append(f'    This key will be removed in v{definition}')

    if listCount:
        lines.append('')

    return '\n'.join(lines)


class RST_module:
    def __init__(self, title):
        self.content = [
            '*'*80,
            title,
            '*'*80,
        ]

    def add_line(self, content=''):
        self.content.append(content)

    def add_section(self, level, prefix, key, subSection):
        if prefix and prefix != 'BaseRun':
            title = f'{prefix}.{key}'
        else:
            title = key

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
                        self.add_section(level, title, subKey,
                                        subSection[subKey])
                return

        self.add_line()
        self.add_line(title)
        self.add_line(LEVELS[level]*80)
        self.add_line()
        if warning:
            self.add_line('.. warning::')
            self.add_line(f'    {warning}')

        leaf = False
        description = ''

        if 'help' in subSection:
            leaf = True
            description = subSection['help']

        if '__doc__' in subSection:
            description = subSection['__doc__']

        self.add_line(description)
        self.add_line()

        if leaf:
            # Need to process domains and more...
            if 'default' in subSection:
                self.add_line(f':default: {subSection["default"]}')

            if 'domains' in subSection:
                self.add_line('.. note::')
                for domain in subSection['domains']:
                    self.add_line(handle_domain(
                        domain, subSection['domains'][domain]))
                self.add_line()

        else:
            # Keep adding sections
            for subKey in subSection:
                if subKey[0] != '_' or subKey == '__value__':
                    self.add_section(level + 1, title, subKey,
                                    subSection[subKey])

    def get_content(self,  lineSeparator='\n'):
        # Ensure new line at the end
        if len(self.content[-1]):
            self.content.append('')

        return lineSeparator.join(self.content)

    def write(self, filePath, lineSeparator='\n'):
        with open(filePath, 'w') as output:
            output.write(self.get_content(lineSeparator))

# -----------------------------------------------------------------------------
# Expected API to use
# -----------------------------------------------------------------------------


def generate_module_from_definitions(definitions):
    generatedRST = RST_module('ParFlow Key Documentation')

    for yaml_file in definitions:
        with open(yaml_file) as file:
            yamlStruct = yaml.load(file, Loader=yaml.FullLoader)

            for rootKey in yamlStruct.keys():
                generatedRST.add_section(0, '', rootKey, yamlStruct[rootKey])

    return generatedRST

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    coreDefinitions = YAML_MODULES_TO_PROCESS
    basePath = os.path.dirname(os.path.abspath(__file__))
    print(basePath)
    defPath = os.path.join(basePath, '../key_definitions')
    definitionFiles = [os.path.join(
        defPath, f'{module}.yaml') for module in coreDefinitions]
    outputFilePath = os.path.join(basePath, '../../parflow/docs/parflow_keys.rst')

    print('-'*80)
    print('Generate Parflow database documentation')
    print('-'*80)
    generatedModule = generate_module_from_definitions(definitionFiles)
    print('-'*80)
    generatedModule.write(outputFilePath)
