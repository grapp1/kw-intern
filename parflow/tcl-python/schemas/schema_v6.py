# schema_v6.py - more working ideas for class definitions

class ValidationException(Exception):
    pass

# Validation class to define validation function
class Validation:
    @staticmethod
    def validate(val, domain, verify=None):
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
            if not isinstance(val, str):
                raise ValidationException(f'{val} ({type(val)} must be a string')
            for entry in verify:
                if val == entry:
                    pass

        elif domain['type'] == 'AnyString':
            if not isinstance(val, str):
                raise ValidationException(f'{val} ({type(val)} must be a string')

class Process:
    def __init__(self):
        self.Topology = Topology()

class Topology:
    """This section describes how processors are
    assigned in order to solve the domain in parallel.
    """
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
                'help': '{Type: integer} P allocates the number of processors to the grid cells in x.'
            },
            'Q': {
                'domain': {
                    'type': 'IntRange',
                    'kwargs': {
                        'minValue': 1,
                        'maxValue': 1000,
                    }
                },
                'help': '{Type: integer} Q allocates the number of processors to the grid cells in y.'
            },
            'R': {
                'domain': {
                    'type': 'IntRange',
                    'kwargs': {
                        'minValue': 1,
                        'maxValue': 1000,
                    }
                },
                'help': '{Type: integer} R allocates the number of processors to the grid cells in z. Please note R '
                        'should always be 1 if you are running with Solver Richards unless you are running a totally '
                        'saturated domain (solver IMPES).'
            }
        }

    def __setattr__(self, name, value):
        if hasattr(self, '_details'):
            domain = self._details[name]['domain']
            Validation.validate(value, domain)
        self.__dict__[name] = value

    def help(self, key = None):
        if key is not None:
            if hasattr(self, '_details'):
                print(self._details[key]['help'])
        else:
            print(self.__doc__)

class GeomInput:
    """GeomInput defines all 'geometrical' information needed by ParFlow. For example, the domain, lithology or
    hydrostratigraphic units, faults, initial plume shapes, and so on, are considered geometries.
    """
    def __init__(self):
        self.Names = ''
        self._details = {
            'Names': {
                'domain': {
                    'type': 'AnyString'
                },
                'help': '{Type: string} This is a list of the geometry input names which define the containers for all '
                        'the geometries defined for this problem. Input names should be separated by spaces.'
            }
        }

    def __setattr__(self, name, value):
        if hasattr(self, '_details'):
            domain = self._details[name]['domain']
            Validation.validate(value, domain)
            # breaking up the spaced out string entries into multiple values
            if " " in value:
                value = value.split()
        self.__dict__[name] = value

    def help(self, key = None):
        if key is not None:
            if hasattr(self, '_details'):
                print(self._details[key]['help'])
        else:
            print(self.__doc__)


Process.Topology = Process().Topology
Process.Topology.P = 4
Process.Topology.Q = 400
Process.Topology.help()
Process.Topology.help('P')

GeomInput = GeomInput()
GeomInput.Names = 'box_input indi_input'
print(GeomInput.Names) # list with individual names
GeomInput.help()
GeomInput.help('Names')

