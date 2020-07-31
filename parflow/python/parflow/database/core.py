r'''
This module aims to provide the core components that are required to build
a Parflow input deck.
'''
import os
from .domains import validateValueWithException, validateValueWithPrint, validateValueToString
from .handlers import decorateValue
from . import TerminalColors as term
from . import TerminalSymbols as termSymbol


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

def validateHelper(containerObj, name, obj, indent, errorCount):
  nbErrors = 0
  validationString = ''
  history = None
  if 'history' in containerObj._details[name] and len(containerObj._details[name]['history']):
    history = containerObj._details[name]['history']
  if 'default' in containerObj._details[name] and obj == containerObj._details[name]['default'] and \
          'MandatoryValue' not in containerObj._details[name]['domains']:
    pass
  else:
    nbErrors, validationString = validateValueToString(name, obj, containerObj._details[name]['domains'],
                                             containerObj.getContextSettings(), history, indent)

  return nbErrors, validationString


# -----------------------------------------------------------------------------

def detailHelper(container, name, value):
  domains = None
  handlers = None
  history = None
  crosscheck = None
  if name in container._details:
    if 'domains' in container._details[name]:
      domains = container._details[name]['domains']

    if 'handlers' in container._details[name]:
      handlers = container._details[name]['handlers']

    if 'history' in container._details[name]:
      history = container._details[name]['history']

    else:
      history = []
      container._details[name]['history'] = history
    history.append(value)

    if 'crosscheck' in container._details[name]:
      crosscheck = container._details[name]['crosscheck']

  return domains, handlers, history, crosscheck

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
    history = None
    valueObjectAssignment = False
    if name[0] != '_' and hasattr(self, '_details'):
      if name in self._details:
        domains, handlers, history, crosscheck = detailHelper(self, name, value)
      elif hasattr(self, name) and isinstance(self.__dict__[name], PFDBObj):
        # Handle value object assignment
        valueObjectAssignment = True
        valueObj = self.__dict__[name]
        domains, handlers, history, crosscheck = detailHelper(valueObj, '_value', value)
      else:
        print(f'Field {name} is not part of the expected schema {self.__class__}')
        if PFDBObj.exitOnError:
          raise ValueError(
              f'Field "{name}" is not part of the expected schema {self.__class__}')

    # Run domain validation
    if PFDBObj.printLineError:
      validateValueWithException(value, domains, PFDBObj.exitOnError)

    if valueObjectAssignment:
      self.__dict__[name].__dict__['_value'] = decorateValue(value, self, handlers)
    else:
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
    for name in self.getKeyNames(True):
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
      if key in self._details:
        if 'help' in self._details[key]:
          print(self._details[key]['help'])
      else:
        obj = self.__dict__[key]
        if hasattr(obj, '__doc__'):
          print(obj.__doc__)

        if hasattr(obj, '_details') and '_value' in obj._details and 'help' in obj._details['_value']:
          print(obj._details['_value']['help'])

    elif hasattr(self, '__doc__'):
      print(self.__doc__)
      if hasattr(self, '_details') and '_value' in self._details and 'help' in self._details['_value']:
        print(self._details['_value']['help'])

  # ---------------------------------------------------------------------------

  def getKeyNames(self, skipDefault=False):
    for name in self.__dict__:
      if name[0] == '_':
        continue

      obj = self.__dict__[name]
      if isinstance(obj, PFDBObj):
        if len(obj):
          yield name
        elif hasattr(obj, '_value') and obj._value != None:
          yield name
      else:
        hasDetails = hasattr(self, '_details') and name in self._details
        hasDefault = hasDetails and 'default' in self._details[name]
        hasDomain = hasDetails and 'domains' in self._details[name]
        isMandatory = hasDomain and 'MandatoryValue' in self._details[name]['domains']
        isDefault = hasDefault and obj == self._details[name]['default']

        if obj != None:
          if skipDefault:
            if not isDefault or isMandatory:
              yield name
          else:
            yield name

        elif isMandatory:
          yield name

  # ---------------------------------------------------------------------------

  def validate(self, indent=1, workdir=None):
    '''
    Method to validate sub hierarchy
    '''
    if len(self) == 0:
      return 0

    errorCount = 0
    indentStr = '  '*indent
    for name in self.getKeyNames(skipDefault=True):
      obj = self.__dict__[name]
      if isinstance(obj, PFDBObj):
        if len(obj):
          if hasattr(obj, '_value'):
            value = obj._value
            addErrors, validationString = validateHelper(obj, '_value', value, indent, errorCount)
            print(f'{indentStr}{name}: {validationString}')
            errorCount += addErrors
          else:
            print(f'{indentStr}{name}:')

          errorCount += obj.validate(indent+1)
      elif hasattr(self, '_details') and name in self._details:
        addErrors, validationString = validateHelper(self, name, obj, indent, errorCount)
        print(f'{indentStr}{name}: {validationString}')
        errorCount += addErrors
      elif obj != None:
        print(f'{indentStr}{name}: {obj}')

    return errorCount

  # ---------------------------------------------------------------------------


  def getParFlowKey(self, parentNamespace, key):
    '''
    Helper method returning the key to use for Parflow on a given field key.
    This allow to handle differences between what can be defined in Python vs Parflow key.
    '''
    if hasattr(self, '_details') and key in self._details and 'exportName' in self._details[key]:
    # if hasattr(self, '_details') and key in self._details and 'exportName' in self._details[key]:
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
