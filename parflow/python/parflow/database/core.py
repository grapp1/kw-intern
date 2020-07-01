r'''
This module aims to provide the core components that are required to build
a Parflow input deck.
'''

from .domains import validateValueWithException, validateValueWithPrint
from .valueHandlers import decorateValue

class PFDBObj:
  printLineError = False
  exitOnError = False

  @staticmethod
  def enableLineError():
    PFDBObj.printLineError = True

  @staticmethod
  def disableLineError():
    PFDBObj.enableDomainExceptions = False

  @staticmethod
  def enableExitError():
    PFDBObj.exitOnError = True

  @staticmethod
  def disableExitError():
    PFDBObj.exitOnError = False

  def __init__(self):
    self._details = {}

  def __setattr__(self, name, value):
    '''
    Helper method that aims to streamline dot notation assignment
    '''
    domain = None
    valueHandler = {}
    if hasattr(self, '_details'):
      if name in self._details:
        if 'domain' in self._details[name]:
          domain = self._details[name]['domain']
        if 'valueHandler' in self._details[name]:
          valueHandler = self._details[name]['valueHandler']
      else:
        print(f'Field {name} is not part of the expected schema {self.__class__}')
        if PFDBObj.exitOnError:
          raise ValueError(
              f'Field "{name}" is not part of the expected schema {self.__class__}')


    # Run domain validation
    if PFDBObj.printLineError:
      validateValueWithException(value, domain, PFDBObj.exitOnError)

    # Decorate value if need be (i.e. Geom.names: 'a b c')
    self.__dict__[name] = decorateValue(value, self, valueHandler)


  def help(self, key=None):
    '''
    Dynamic help function for runtime evaluation
    '''
    if key is not None:
      if key in self._details and 'help' in self._details[key]:
        print(self._details[key]['help'])
      else:
        print(self.__doc__)

  def validate(self, indent=1):
    errorCount = 0
    indentStr = '  '*indent
    for name in self.__dict__:
      if name == '_details':
        continue

      obj = self.__dict__[name]
      if isinstance(obj, PFDBObj):
        print(f'{indentStr}{name}:')
        errorCount += obj.validate(indent=indent+1)
      elif hasattr(self, '_details') and name in self._details and 'domain' in self._details[name]:
        errorCount += validateValueWithPrint(name, obj, self._details[name]['domain'], indent)
      elif name[0] == '_':
        # skip internal variables
        pass
      else:
        print(f'{indentStr}{name}: {obj}')

    return errorCount
