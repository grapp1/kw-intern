r'''
This module aims to provide the core components that are required to build
a Parflow input deck.
'''

from .domains import validateValueWithException, validateValueWithPrint
from .valueHandlers import decorateValue

class PFDBObj:
  def __init__(self):
    self._details = {}

  def __setattr__(self, name, value):
    '''
    Helper method that aims to streamline dot notation assignment
    '''
    domain = None
    valueHandler = None
    if hasattr(self, '_details') and name in self._details:
      if 'domain' in self._details[name]:
        domain = self._details[name]['domain']
      if 'valueHandler' in self._details[name]:
        valueHandler = self._details[name]['valueHandler']

    # Run domain validation
    validateValueWithException(value, domain)

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
        print(f'{indentStr}{name}')
        obj.validate(indent=indent+1)
      elif name in self._details and 'domain' in self._details[name]:
        errorCount += validateValueWithPrint(name, obj, self._details[name]['domain'], indent+1)
      else:
        print(f'{indentStr}{name} - Nothing to validate')

    return errorCount
