# schema_v6.py - more working ideas for class definitions

# Validation class to define validation function
class Validation:
    @staticmethod
    def validate(key, val, domain):
        if domain['type'] == 'IntRange':
            if not isinstance(val, int):
                raise Exception(f'{val} ({type(val)} must be an int')
            else:
            # Make sure it is in the int range
                if val > domain['kwargs']['maxValue']:
                    raise Exception(str(val) + ' is greater than max int: ' + str(domain['kwargs']['maxValue']))
                elif val < domain['kwargs']['minValue']:
                    raise Exception(str(val) + ' is smaller than the min int: ' + str(domain['kwargs']['minValue']))

        elif domain.type == 'SetString':
            if isinstance(val, str):
                pass
        elif domain.type == 'AnyString':
            if isinstance(val, str):
                pass


class ValidationException(Exception):
    pass

class Process:
    def __init__(self):
        self.Topology = Topology()

class Topology:
    def __init__(self):
        self.P = 1
        self.Q = 1
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
                'help': 'helptextP'
            }
        }


    def __setattr__(self, name, value):
        if hasattr(self, '_details'):
            domain = self._details[name]['domain']
            Validation.validate(name, value, domain)
        self.__dict__[name] = value
        print(self.__dict__[name])

    def help(self, key):
        print(self._details[key]['help'])


obj = Process().Topology
obj.P = 4
obj.Q = 4000
# obj.validate()
#obj.help('P')
#print(obj._details.items())
# print(obj.Q)
# print(obj._requirements['P']['max'])

