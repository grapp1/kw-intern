# test.py
# testing ideas for developing a class generator to define ParFlow keys

import time

class mydoc( str ):
    def __init__(self, value):
        self.txt = value
    def expandtabs( self, *args, **kwargs ):
        return "{} created on {}".format(self.txt, time.asctime() ).expandtabs( *args, **kwargs )


class Parflow:
    '''Class doc'''
    def __init__(self, a, b):
      '''
      Init doc
      param a test
      '''
      self.fieldDemo = 'seb'
      self.fieldDemo.__doc__ = mydoc('seb super doc field')
      # self.fieldDemo.__doc__ = 'My internal doc'

    def test(self, c):
      '''test doc'''
      pass

#pf = Parflow(4,5)
#print(pf.fieldDemo.__doc__)
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
        return self.domain.validate(self.value)

    def getValidationError(self):
        return self.domain.errorMessage(self.value)

    def setValue(self, value: int) -> bool:
        '''Update value'''
        if self.domain.validate(value):
            self.value = value
        else:
            print('error')
            #throw Error('The value is invalid:', self.domain.errorMessage(value))

class _T_P_R(ValueObject):
    '''
    Number of process along Z
    '''
    pass

class Processor:
    def __init__(self):
        self.R = _T_P_R(5, IntRange(1, 10))
        self.P = ValueObject(5, IntRange(1, 10))
        self.Q = ValueObject(5, IntRange(1, 10))


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
Process_Topology_P = type("Process_Topology_P", (object,), {
    # constructor
    "__init__": constructor,

    # data members
    "help": "P allocates the number of processes to the grid-cells in x.",
    "defaultValue": 1,
    "min_val": 1,
    "max_val": 1000,

    # member functions
    #"range_validation": IntRange(Process_Topology_P.min_val, Process_Topology_P.max_val), # can't get this to work yet
    "class_func": classMethod
})

print(sorted(Process_Topology_P.__dict__.keys()))


# creating objects
obj = Process_Topology_P("constructor argument")
print(obj.__init__)
print(obj.defaultValue)
print(obj.min_val)
print(obj.max_val)
Process_Topology_P.class_func("Class Dynamically Created!")




range = IntRange(1,10)


proc = Processor()
proc.R = 20
#print(proc.R.__doc__)
#proc.R.setValue(10)
#help(proc.R)
