# schema_v7.py - implementing Seb's suggestions

class ValidationException(Exception):
    pass


# defining available domains to validate key setting
class IntRangeDomain:
    def validate(self, value, minValue=None, maxValue=None, **kwargs):
        if minValue != None and value < minValue:
            raise ValidationException(f'{value} is smaller than min int: {minValue}')
        if maxValue != None and value > maxValue:
            raise ValidationException(f'{value} is greater than max int: {maxValue}')


class EnumDomain:
    def validate(self, value, enumList=[]):
        if value not in enumList:
            raise ValidationException('{:s} must be one of [{:s}]'.format(value, ','.join(enumList)))


class AnyStringDomain:
    def validate(self, value):
        if not isinstance(value, str):
            raise ValidationException(f'{value} ({type(value)} must be a string')


AVAILABLE_DOMAINS = {
    'IntRangeDomain': IntRangeDomain(),
    'EnumDomain': EnumDomain(),
    'AnyStringDomain': AnyStringDomain()
}

# defining ParFlow database object to consolidate the defined __setattr__ and help functions
class PFDBObj:
    def __setattr__(self, name, value):
        if hasattr(self, '_details'):
            domain = self._details[name]['domain']
            if domain['type'] in AVAILABLE_DOMAINS:
                domainObj = AVAILABLE_DOMAINS[domain['type']]
                if 'kwargs' in domain:
                    domainObj.validate(value, **domain['kwargs'])
                else:
                    domainObj.validate(value)
            # breaking up the spaced out string entries into multiple values
            if type(value) == str:
                if " " in value:
                    value = value.split()
        self.__dict__[name] = value

    def help(self, key=None):
        if key is not None:
            if hasattr(self, '_details'):
                print(self._details[key]['help'])
        else:
            print(self.__doc__)

# Defining ParFlow keys
class Process(PFDBObj):
    def __init__(self):
        self.Topology = Topology()


class Topology(PFDBObj):
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
                    'type': 'IntRangeDomain',
                    'kwargs': {
                        'minValue': 1,
                        'maxValue': 1000,
                    }
                },
                'help': '{Type: integer} P allocates the number of processors to the grid cells in x.'
            },
            'Q': {
                'domain': {
                    'type': 'IntRangeDomain',
                    'kwargs': {
                        'minValue': 1,
                        'maxValue': 1000,
                    }
                },
                'help': '{Type: integer} Q allocates the number of processors to the grid cells in y.'
            },
            'R': {
                'domain': {
                    'type': 'IntRangeDomain',
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


class GeomInput(PFDBObj):
    """GeomInput defines all 'geometrical' information needed by ParFlow. For example, the domain, lithology or
    hydrostratigraphic units, faults, initial plume shapes, and so on, are considered geometries.
    """

    def __init__(self):
        self.Names = ''
        self._details = {
            'Names': {
                'domain': {
                    'type': 'AnyStringDomain'
                },
                'help': '{Type: string} This is a list of the geometry input names which define the containers for all '
                        'the geometries defined for this problem. Input names should be separated by spaces.'
            }
        }

    def setnames(self):
        print(self.Names)


class Geom(PFDBObj):
    """This builds off of GeomInput
    """
    def __init__(self, name):
        pass


# testing

Process.Topology = Process().Topology
Process.Topology.P = 4
Process.Topology.Q = 400
Process.Topology.help()
Process.Topology.help('P')

GeomInput = GeomInput()
GeomInput.Names = 'box_input indi_input'
GeomInput.setnames()
print(GeomInput.Names)  # list with individual names
print(GeomInput.__dict__)
GeomInput.help()
GeomInput.help('Names')
