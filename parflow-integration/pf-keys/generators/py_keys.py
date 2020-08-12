r'''
This module provide the infrastructure to load and generate the Parflow
database structure as Python classes so IDE and runtime environment can
be used to query the help and constraints associated to each keys.
'''

import os
import sys
import traceback
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
    'netcdf',
    'run'
]
# -----------------------------------------------------------------------------


def is_field(key, definition):
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


def is_class(key, definition):
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

    return True

# -----------------------------------------------------------------------------


def has_value(key, definition):
    if key[0] == '_':
        return False

    return '__value__' in definition

# -----------------------------------------------------------------------------


def is_class_item(key, definition):
    if key[0] == '.':
        return True

    return False

# -----------------------------------------------------------------------------


def json_to_python(txt):
    return txt.replace(' true,', ' True,').replace(' false,', ' False,').replace(' null', ' None').replace(': true', ': True')

# -----------------------------------------------------------------------------


def yaml_value(yamlval):
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

    def add_class(self, className):
        self.classCount += 1
        if className in self.classNameCount:
            self.classNameCount[className] += 1
        else:
            self.classNameCount[className] = 1

        return self.classNameCount[className] - 1

    def get_deduplicate_class_name(self, className, classDefinition=None):
        if classDefinition and '__class__' in classDefinition:
            return classDefinition['__class__']
        if className in self.classNameCount:
            return f'{className}_{self.classNameCount[className]}'
        return className

    def add_field(self, fieldName):
        self.fieldCount += 1

    def get_summary(self, lineSeparator='\n'):
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

    def print_summary(self):
        print(self.get_summary())

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

    def add_line(self, content=''):
        self.content.append(content)

    def add_separator(self):
        self.add_line()
        self.add_line(f"# {'-'*78}")
        self.add_line()

    def add_class(self, className, classDefinition):
        try:
            classKeys = classDefinition.keys()
            classMembers = []
            fieldMembers = []
            classInstances = []
            classItems = []
            classDetails = {}

            self.add_separator()

            dedupClassName = self.validationSummary.get_deduplicate_class_name(
                className, classDefinition)
            self.validationSummary.add_class(className)

            self.add_line(f'class {dedupClassName}(PFDBObj):')
            if '__doc__' in classKeys:
                self.add_comment(classDefinition['__doc__'], self.strIndent)

            for key in classDefinition:
                if is_class(key, classDefinition):
                    classMembers.append(key)
                if is_field(key, classDefinition):
                    fieldMembers.append(key)
                if key == '__class_instances__':
                    classInstances = classDefinition['__class_instances__']
                if is_class_item(key, classDefinition):
                    classItems.append(classDefinition[key])

            if len(classMembers) + len(fieldMembers) + len(classInstances) > 0 or '_dynamic' in classDefinition:
                '''
                  def __init__(self, parent=None):
                    super().__init__(parent)
                    self.Topology = Topology(self)
                '''
                self.add_line(
                    f'{self.strIndent}def __init__(self, parent=None):')
                self.add_line(f'{self.strIndent*2}super().__init__(parent)')

                if has_value(className, classDefinition):
                    self.add_field(
                        '_value', classDefinition['__value__'], classDetails)

                for instance in classMembers:
                    self.add_line(
                        f'{self.strIndent*2}self.{instance} = {self.validationSummary.get_deduplicate_class_name(instance)}(self)')

                for instance in classInstances:
                    self.add_class_instance(instance)

                for field in fieldMembers:
                    self.add_field(field, classDefinition[field], classDetails)

                self.add_details(classDetails)
                self.add_dynamic(classDefinition)

            for classMember in classMembers:
                # Catch error
                if classMember == 'help':
                    print(
                        f'Invalid syntax: {className} must use __doc__ rather than help')
                    sys.exit(1)
                self.add_class(classMember, classDefinition[classMember])

            for classItem in classItems:
                self.add_class(classItem['__class__'], classItem)

        except:
            # traceback.print_exc()
            print(f'Error when processing class {className}')

    def add_details(self, classDetails):
        if len(classDetails):
            detailsLines = json.dumps(classDetails, indent=2).splitlines()
            self.add_line(
                f'{self.strIndent * 2}self._details = {detailsLines[0]}')
            for line in detailsLines[1:]:
                lineWithIndent = f'{self.strIndent * 2}{line}'
                self.add_line(json_to_python(lineWithIndent))

    def add_dynamic(self, classDetails):
        if '_dynamic' in classDetails:
            dynamicLines = json.dumps(
                classDetails['_dynamic'], indent=2).splitlines()
            self.add_line(
                f'{self.strIndent * 2}self._dynamic = {dynamicLines[0]}')
            for line in dynamicLines[1:]:
                lineWithIndent = f'{self.strIndent * 2}{line}'
                self.add_line(json_to_python(lineWithIndent))
            self.add_line(f'{self.strIndent * 2}self.processDynamic()')

    def add_field(self, fieldName, fieldDefinition, classDetails):
        self.validationSummary.add_field(fieldName)
        field_val = None
        if 'default' in fieldDefinition:
            field_val = yaml_value(fieldDefinition['default'])
            fieldDefinition['default'] = field_val

        if isinstance(field_val, str):
            self.add_line(f"{self.strIndent*2}self.{fieldName} = '{field_val}'")
        else:
            self.add_line(f"{self.strIndent * 2}self.{fieldName} = {field_val}")
        classDetails[fieldName] = fieldDefinition

    def add_class_instance(self, fieldName):
        self.add_line(
            f"{self.strIndent*2}self.{fieldName} = {fieldName}(self)")

    def add_comment(self, docContent, strIndent):
        self.add_line(f"{strIndent}'''")
        for line in docContent.splitlines():
            self.add_line(f'{strIndent}{line}')
        self.add_line(f"{strIndent}'''")

    def get_content(self,  lineSeparator='\n'):
        self.content[4] = self.validationSummary.get_summary(lineSeparator)
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
    generatedModule = PythonModule()

    for yaml_file in definitions:
        with open(yaml_file) as file:
            yamlStruct = yaml.load(file, Loader=yaml.FullLoader)

            for rootKey in yamlStruct.keys():
                generatedModule.add_class(rootKey, yamlStruct[rootKey])

    return generatedModule

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    coreDefinitions = YAML_MODULES_TO_PROCESS
    basePath = os.path.dirname(os.path.abspath(__file__))
    defPath = os.path.join(basePath, '../key_definitions')
    definitionFiles = [os.path.join(
        defPath, f'{module}.yaml') for module in coreDefinitions]
    outputFilePath = os.path.join(basePath, '../../pf-python/parflow/tools/database/generated.py')

    print('-'*80)
    print('Generate Parflow database module')
    print('-'*80)
    generatedModule = generate_module_from_definitions(definitionFiles)
    print(generatedModule.validationSummary.get_summary())
    print('-'*80)
    generatedModule.write(outputFilePath)
