# generator.py - breaking out class generator from schema_v5.py

import os
import yaml

print(os.getcwd())
input_file = 'input_set2.yaml'

with open(input_file) as file:
    pf_classes = yaml.load(file, Loader=yaml.FullLoader)

definition = ''
for parent in pf_classes.keys():

    definition += f'class {parent}:\n'
    if 'help' in pf_classes[parent]:
        definition += f'    """{pf_classes[parent]["help"]}"""\n'

    definition += '    def __init__(self):\n'

    if 'instances' in pf_classes[parent]:
        definition += f'        self.{pf_classes[parent]["instances"]} = {pf_classes[parent]["instances"]}()\n'

    if 'keys' in pf_classes[parent]:
        for key in pf_classes[parent].keys():
            print(pf_classes[parent][key])
            # definition += f'        {pf_classes[parent][keys]}:\n'

    definition += '\n'
    definition += '\n'


print(definition)


