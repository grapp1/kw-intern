# schema_v5.py - more working ideas for class definitions

classes = [
    {
        'name': 'Process',
        'members': {
            'P': {
                'default': 1,
                'min': 0,
                'max': 1000
            },
            'Q': {
                'default': 1,
                'min': 0,
                'max': 1000
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
# Write out the definitions at the end
#with open('output.py', 'w') as wf:
#    wf.write(definition)
#print(definition)

class Topology:
    pass

class Process:
    def __init__(self):
        self.P = 1
        self.Q = 1
        self.Topology = Topology()
        self._requirements = {
            'P': {
               'min': 0,
               'max': 1000
            }
        }
    def validate(self):
        for key, req in self._requirements.items():
            val = getattr(self, key)
            if isinstance(val, int):
                # For integers, we check mins and maxes
                if 'min' in req and val < req['min']:
                    raise ValidationException(f'{val} is less than min: {req["min"]}')
                elif 'max' in req and val > req['max']:
                    raise ValidationException(f'{val} is greater than max: {req["max"]}')

obj = Process()
obj.Topology