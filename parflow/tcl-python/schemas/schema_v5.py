# schema_v5.py - more working ideas for class definitions

# part 1: testing writing of classes with documentation and validation

class ValidationException(Exception):
    pass

class Process:
    def __init__(self):
        self.Topology = Topology()

class Topology:
    def __init__(self):
        self.P = 1
        self.Q = 1
        self._requirements = {
            'P': {
                'min': 0,
                'max': 1000,
                'help': 'helptextP'
            },
            'Q': {
                'min': 0,
                'max': 1000,
                'help': 'helptextQ'
            }
        }

    def __setattr__(self, name, value):
        self.validate(value)
        self.__dict__[name] = value

    def validate(self, v):
        if isinstance(v, int):
            # Make sure it is in the int range
            if v > domain.max_int:
                raise Exception(str(v) + ' is greater than max int: ' + str(domain.max_int))
            elif v < domain.min_int:
                raise Exception(str(v) + ' is smaller than the min int: ' + str(domain.min_int))

    def validate(self):
        for key, req in self._requirements.items():
            val = getattr(self, key)
            if isinstance(val, int):
                # For integers, we check mins and maxes
                if 'min' in req and val < req['min']:
                    raise ValidationException(f'{val} is less than min: {req["min"]}')
                elif 'max' in req and val > req['max']:
                    raise ValidationException(f'{val} is greater than max: {req["max"]}')

    def help(self, key):
        print(self._requirements[key]['help'])


obj = Process().Topology
obj.P = 4
obj.Q = 400
obj.validate()
obj.help('Q')
print(obj._requirements.keys())
print(obj.Q)
print(obj._requirements['P']['max'])


# part 2: working to automate the class definitions from yaml
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
