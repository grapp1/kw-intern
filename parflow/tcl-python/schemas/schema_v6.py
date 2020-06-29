# schema_v6.py - more working ideas for class definitions

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
        self.validate(value)
        self.__dict__[name] = value
        
    def validate(self, v):
        if isinstance(v, int):
            # Make sure it is in the int range
            if v > domain.maxValue:
                raise Exception(str(v) + ' is greater than max int: ' + str(domain.maxValue))
            elif v < domain.minValue:
                raise Exception(str(v) + ' is smaller than the min int: ' + str(domain.minValue))
    #
    # def validate(self):
    #     for key, req in self._requirements.items():
    #         val = getattr(self, key)
    #         if isinstance(val, int):
    #             # For integers, we check mins and maxes
    #             if 'min' in req and val < req['min']:
    #                 raise ValidationException(f'{val} is less than min: {req["min"]}')
    #             elif 'max' in req and val > req['max']:
    #                 raise ValidationException(f'{val} is greater than max: {req["max"]}')

    def help(self, key):
        print(self._requirements[key]['help'])


obj = Process().Topology
obj.P = 4
obj.Q = 400
# obj.validate()
obj.help('P')
print(obj._requirements.keys())
# print(obj.Q)
# print(obj._requirements['P']['max'])

