r'''
This module aims to provide the core components that are required to build
a Parflow input deck.
'''
import os
from .domains import validateValueWithException, validateValueWithPrint, duplicateSearch
from .handlers import decorateValue
from . import TerminalColors as term

class PFDBObj:
  printLineError = False
  exitOnError = False
  workingDirectory = os.getcwd()

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

  @staticmethod
  def setWorkingDirectory(workdir):
    if workdir:
      PFDBObj.workingDirectory = workdir
    else:
      PFDBObj.workingDirectory = os.getcwd()

  def __init__(self, parent=None):
    self._parent = parent

  def __setattr__(self, name, value):
    '''
    Helper method that aims to streamline dot notation assignment
    '''
    domains = None
    handlers = None
    if name[0] != '_' and hasattr(self, '_details'):
      if name in self._details:
        if 'domains' in self._details[name]:
          domains = self._details[name]['domains']
        if 'handlers' in self._details[name]:
          handlers = self._details[name]['handlers']
        if 'history' in self._details[name]:
          self._details[name]['history'].append(value)
        else:
          self._details[name]['history'] = []
          self._details[name]['history'].append(value)

      else:
        print(self._details)
        print(f'Field {name} is not part of the expected schema {self.__class__}')
        if PFDBObj.exitOnError:
          raise ValueError(
              f'Field "{name}" is not part of the expected schema {self.__class__}')

    # Run domain validation
    if PFDBObj.printLineError:
      validateValueWithException(value, domains, PFDBObj.exitOnError)

    # Decorate value if need be (i.e. Geom.names: 'a b c')
    self.__dict__[name] = decorateValue(value, self, handlers)


  def help(self, key=None):
    '''
    Dynamic help function for runtime evaluation
    '''
    if key is not None:
      if key in self._details and 'help' in self._details[key]:
        print(self._details[key]['help'])
      else:
        print(self.__doc__)

  def __len__(self):
    valueCount = 0
    for name in self.__dict__:
      if name[0] == '_':
        continue

      obj = self.__dict__[name]
      if isinstance(obj, PFDBObj):
        valueCount += len(obj)
      elif obj != None:
        valueCount += 1
      elif hasattr(self, '_details') and name in self._details and 'domains' in self._details[name]:
        if 'MandatoryValue' in self._details[name]['domains']:
          valueCount += 1

    return valueCount

  def validate(self, indent=1, workdir=None):
    if len(self) == 0:
      return 0

    errorCount = 0
    indentStr = '  '*indent
    for name in self.__dict__:
      if name[0] == '_':
        continue

      obj = self.__dict__[name]
      if isinstance(obj, PFDBObj):
        if len(obj):
          print(f'{indentStr}{name}:')
          errorCount += obj.validate(indent+1)
      elif hasattr(self, '_details') and name in self._details and 'domains' in self._details[name]:
        history = None
        if 'history' in self._details[name] and len(self._details[name]['history']):
          history = self._details[name]['history']
        errorCount += validateValueWithPrint(name, obj, self._details[name]['domains'], self.getContextSettings(), history, indent)
      elif name[0] == '_':
        # skip internal variables
        pass
      elif obj != None:
        print(f'{indentStr}{name}: {obj}')
      elif obj == None:
        pass

    return errorCount

  def getParFlowKey(self, parentNamespace, key):
    if hasattr(self, '_details') and key in self._details and 'exportName' in self._details[key]:
      exportKey = self._details[key]['exportName']
      parentTokens = parentNamespace.split('.')
      parentOffset = 0

      while exportKey[parentOffset] == '.':
        parentOffset += 1

      if len(parentTokens[:1-parentOffset]):
        return f'{".".join(parentTokens[:1-parentOffset])}.{exportKey[parentOffset:]}'

      return exportKey[parentOffset:]

    if parentNamespace:
      return f'{parentNamespace}.{key}'

    return key

  def getObjFromLocation(self, location='.'):
    path_items = location.split('/')
    current_location = self
    for path_item in path_items:
      if path_item == '..':
        current_location = current_location._parent
      elif path_item == '.':
        pass
      else:
        current_location = getattr(current_location, path_item)

    return current_location

  def getContextSettings(self):
    return {
      'printLineError': PFDBObj.printLineError,
      'exitOnError': PFDBObj.exitOnError,
      'workingDirectory': PFDBObj.workingDirectory,
    }