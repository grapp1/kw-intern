# schema_v4.py: dynamic class definitions from yaml

import yaml

class parflow:

    """Hello, welcome to ParFlow"""

    def __init__(self, runname='runname', config_file = "input_set2.yaml"):
        self.runname = runname
        with open(config_file) as file:
            self.pf = yaml.load(file, Loader=yaml.FullLoader)

class ValidationException(Exception):
  pass


class IntRange:
    def __init__(self, minValue, maxValue):
        self.minValue = minValue;
        self.maxValue = maxValue

    def validate(self, value):
        if value < self.minValue:
            raise ValidationException(f'The value is below the min range of {self.minValue}')
        elif value > self.maxValue:
            raise ValidationException(f'The value is above the max range of {self.maxValue}')

        # All good
        return None

    def __call__(self, val):
        self.validate(val)


class ValueObject:
    def __init__(self, defaultValue, domain):
        self.domain = domain
        self.value = defaultValue

    def isValid(self):
        return self.domain.validate

    def getValidationError(self):
        return self.domain.errorMessage(self.value)

    def setValue(self, value: int) -> bool:
        '''Update value'''
        if self.domain.validate:
            self.value = value
        else:
            print('error')
        # throw Error('The value is invalid:', self.domain.errorMessage(value))


# program to create class dynamically

# constructor
def constructor(self, arg):
    self.constructor_arg = arg


# method
def displayMethod(self, arg):
    print(arg)


# class method
@classmethod
def classMethod(cls, arg):
    print(arg)


# creating class dynamically
min_val = 1
max_val = 1000
Process_Topology_P = type("Process_Topology_P", (object,), {
    # constructor
    "__init__": constructor,
    # data members
    "help": "P allocates the number of processes to the grid-cells in x.",
    "defaultValue": 1,
    "min_val": min_val,
    "max_val": max_val,
    # member functions
    "range_validation": IntRange(min_val, max_val),
    "class_func": classMethod
})

print(Process_Topology_P.max_val)

# creating objects
obj = Process_Topology_P("constructor argument")
print(obj.__init__)
print(obj.defaultValue)
print(obj.min_val)
print(obj.range_validation(500))
Process_Topology_P.class_func("Class Dynamically Created!")

obj = parflow()
print(obj.pf)
for key in obj.pf:
    print(obj.pf[key])