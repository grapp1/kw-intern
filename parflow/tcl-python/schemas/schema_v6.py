# schema_v6.py - more working ideas for class definitions

class ValidationException(Exception):
    pass

# Validation class to define validation function
class Validation:
    @staticmethod
    def validate(val, domain):
        if domain['type'] == 'IntRange':
            if not isinstance(val, int):
                raise ValidationException(f'{val} ({type(val)} must be an int')
            else:
            # Make sure it is in the int range
                if val > domain['kwargs']['maxValue']:
                    raise ValidationException(f'{val} is greater than max int: {domain["kwargs"]["maxValue"]}')
                elif val < domain['kwargs']['minValue']:
                    raise ValidationException(str(val) + ' is smaller than the min int: ' + str(domain['kwargs']['minValue']))

        elif domain['type'] == 'SetString':
            if isinstance(val, str):
                pass

        elif domain['type'] == 'AnyString':
            if not isinstance(val, str):
                raise ValidationException(f'{val} ({type(val)} must be a string')

class Process:
    def __init__(self):
        self.Topology = Topology()

class Topology:
    def __init__(self):
        self.P = 1
        self.Q = 1
        self.R = 1
        self._details = {
            'P': {
                'domain': {
                    'type': 'IntRange',
                    'kwargs': {
                        'minValue': 1,
                        'maxValue': 1000,
                    }
                },
                'help': 'helptextP'
            },
            'Q': {
                'domain': {
                    'type': 'IntRange',
                    'kwargs': {
                        'minValue': 1,
                        'maxValue': 1000,
                    }
                },
                'help': 'helptextQ'
            },
            'R': {
                'domain': {
                    'type': 'IntRange',
                    'kwargs': {
                        'minValue': 1,
                        'maxValue': 1000,
                    }
                },
                'help': 'helptextR'
            }
        }

    def __setattr__(self, name, value):
        if hasattr(self, '_details'):
            domain = self._details[name]['domain']
            Validation.validate(value, domain)
        self.__dict__[name] = value

    def help(self, key):
        print(self._details[key]['help'])

class GeomInput:
    def __init__(self):
        self.Names = ''
        self._details = {
            'Names': {
                'domain': {
                    'type': 'AnyString'
                },
                'help': 'This is a list of the geometry input names which define the containers for all the '
                        'geometries defined for this problem. '
            }
        }



    def __setattr__(self, name, value):
        if hasattr(self, '_details'):
            domain = self._details[name]['domain']
            Validation.validate(value, domain)
        self.__dict__[name] = value

    def help(self, key):
        print(self._details[key]['help'])


obj = Process().Topology
obj.P = 4
obj.Q = 400
obj.help('P')
obj2 = GeomInput()
obj2.Names = 'box_input'
obj2.help('Names')

#print(obj._details.items())
# print(obj.Q)
# print(obj._requirements['P']['max'])

