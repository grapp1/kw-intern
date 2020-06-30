# generator.py - breaking out class generator from schema_v5.py

classes = [
    {
        'name': 'Process',
        'members': {
            'P': {
                'default': 1,
                'min': 0,
                'max': 1000,
                'help': 'helptextP'
            },
            'Q': {
                'default': 1,
                'min': 0,
                'max': 1000,
                'help': 'helptextQ'
            }
        }
    }
]
# Write out the classes
definition = ''
for c in classes:
    name = c['name']
    definition += f'class {name}:\n'
    definition += '    def __init__(self):\n'
    members = c['members']
    for member, info in members.items():
        default = info['default']
        definition += f'        self.{member} = {default}\n'
    definition += f'        self._requirements = {{\n'
    for member, info in members.items():
        min_val = info['min']
        max_val = info['max']
        helptext = info['help']
        definition += f'            {member}: {{\n'
        definition += f'                "min": {min_val}\n'
        definition += f'                "max": {max_val}\n'
        definition += f'                "help": {helptext}\n'
# Write out the definitions at the end
#with open('output.py', 'w') as wf:
#    wf.write(definition)
print(definition)
