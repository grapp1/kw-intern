r'''
This module aims to provide the core components that are required to build
a Parflow input deck.
'''
import os
from .domains import validateValueWithException, validateValueWithPrint, duplicateSearch
from .handlers import decorateValue
from . import TerminalColors as term

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------

def mapToParent(pfdbObj):
  return pfdbObj._parent

# -----------------------------------------------------------------------------

def mapToSelf(pfdbObj):
  return pfdbObj

# -----------------------------------------------------------------------------

def mapToChild(name):
  return lambda pfdbObj: getattr(pfdbObj, name)

# -----------------------------------------------------------------------------

def mapToChildrenOfType(className):
  def getChildrenOfType(pfdbObj):
    return pfdbObj.getChildrenOfType(className)
  return getChildrenOfType

# -----------------------------------------------------------------------------
# Main DB Object
# -----------------------------------------------------------------------------
class PFDBObj:
  printLineError = False
  exitOnError = False
  workingDirectory = os.getcwd()

  # ---------------------------------------------------------------------------
  # Global settings
  # ---------------------------------------------------------------------------

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

  # ---------------------------------------------------------------------------
  # Instance specific code
  # ---------------------------------------------------------------------------

  def __init__(self, parent=None):
    '''
    Create container object while keeping a reference to your parent
    '''
    self._parent = parent

  # ---------------------------------------------------------------------------

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

  # ---------------------------------------------------------------------------

  def __len__(self):
    '''
    Return the count of nested fields.
      - If a field is not set but is Mandatory it will count as 1
      - If a field is not set, it will count as 0
      - A container does not count. (0)
    '''
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

  # ---------------------------------------------------------------------------

  def help(self, key=None):
    '''
    Dynamic help function for runtime evaluation
    '''
    if key is not None:
      if key in self._details and 'help' in self._details[key]:
        print(self._details[key]['help'])
      else:
        print(self.__doc__)

  # ---------------------------------------------------------------------------

  def validate(self, indent=1, workdir=None):
    '''
    Method to validate sub hierarchy
    '''
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
        if 'default' in self._details[name] and obj == self._details[name]['default'] and 'MandatoryValue' not in self._details[name]['domains']:
          pass
        else:
          errorCount += validateValueWithPrint(name, obj, self._details[name]['domains'], self.getContextSettings(),
                                               history, indent)
      elif name[0] == '_':
        # skip internal variables
        pass
      elif obj != None:
        print(f'{indentStr}{name}: {obj}')
      elif obj == None:
        pass

    return errorCount

  # ---------------------------------------------------------------------------

  def getParFlowKey(self, parentNamespace, key):
    '''
    Helper method returning the key to use for Parflow on a given field key.
    This allow to handle differences between what can be defined in Python vs Parflow key.
    '''
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

  # ---------------------------------------------------------------------------

  def getChildrenOfType(self, className):
    results = []
    for (key, value) in self.__dict__.items():
      if key[0] == '_':
        continue
      if value.__class__.__name__ == className:
        results.append(value)

    return results

  # ---------------------------------------------------------------------------

  def getSelectionFromLocation(self, location='.'):
    '''
    Return a PFDBObj object based on a location.

    i.e.:
      run.Process.Topology.getObjFromLocation('.') => run.Process.Topology
      run.Process.Topology.getObjFromLocation('..') => run.Process
      run.Process.Topology.getObjFromLocation('../../Geom') => run.Geom
    '''
    # print(f'getSelectionFromLocation({location})')
    current_location = self
    path_items = location.split('/')
    if location[0] == '/':
      while current_location._parent != None:
        current_location = current_location._parent

    nextList = [current_location]
    for path_item in path_items:
      if path_item == '':
        continue

      # print(f'>>> List: {nextList}')
      # print(f'>>> Path: {path_item}')

      currentList = nextList
      nextList = []

      if path_item == '..':
        nextList.extend(map(mapToParent, currentList))
      elif path_item == '.':
        nextList.extend(map(mapToSelf, currentList))
      elif path_item[0] == '{':
        multiList = map(mapToChildrenOfType(path_item[1:-1]), currentList)
        nextList = [item for sublist in multiList for item in sublist]
      else:
        nextList.extend(map(mapToChild(path_item), currentList))
        if isinstance(nextList[0], list):
          nextList = [item for sublist in nextList for item in sublist]

    # print(f'=>{nextList}')
    return nextList

  # ---------------------------------------------------------------------------

  def getContextSettings(self):
    '''
    Return global settings for our current parflow run.
    This is useful when providing global information for domains or else.
    '''
    return {
      'printLineError': PFDBObj.printLineError,
      'exitOnError': PFDBObj.exitOnError,
      'workingDirectory': PFDBObj.workingDirectory,
    }

  # ---------------------------------------------------------------------------

  def pfset(self, key='', value=None):
    '''
    Allow to define any parflow key so it can be exported
    '''
    tokens = key.split('.')
    container = self.getSelectionFromLocation('/'.join(tokens[:-1]))[0]
    if container:
      container[tokens[-1]] = value
    else:
      # store key on the side
      if '_pfstore' not in self.__dict__:
        self.__dict__['_pfstore'] = {}
      self.__dict__['_pfstore'][key] = value

  # ---------------------------------------------------------------------------

  def processDynamic(self):
    from . import generated
    for (className, selection) in self._dynamic.items():
      klass = getattr(generated, className)
      names = self.getSelectionFromLocation(selection)
      for name in names:
        self.__dict__[name] = klass(self)
