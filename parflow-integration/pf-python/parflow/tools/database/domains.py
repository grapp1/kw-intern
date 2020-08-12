r'''
This module aims to gather all kind of value validation you would like to
enable inside Parflow run.
'''

import sys
import types
import traceback
import os

from ..terminal import Colors as term
from ..terminal import Symbols as termSymbol

# -----------------------------------------------------------------------------
# Validation helper functions
# -----------------------------------------------------------------------------

def filterErrorsByType(msgType, errors):
  filterList = []
  for error in errors:
    if error['type'] == msgType:
      filterList.append(error['message'])

  return filterList


# -----------------------------------------------------------------------------

def error(message):
  return {
    'type': 'ERROR',
    'message': message
  }

# -----------------------------------------------------------------------------

def warning(message):
  return {
    'type': 'WARNING',
    'message': message
  }
# -----------------------------------------------------------------------------

def duplicateSearch(history):
  if len(history) > 1:
    dup_count = len(history)
    return dup_count
  else:
    pass

# -----------------------------------------------------------------------------

def getComparableVersion(version):
  cVersion = 0
  versionTokens = version.split('.')
  for versionToken in versionTokens:
    cVersion *= 1000
    cVersion += int(versionToken)
  return cVersion

# -----------------------------------------------------------------------------

def getInstalledParFlowModule(module):
  moduleFile = f'{os.getenv("PARFLOW_DIR")}/config/Makefile.config'
  hasModuleInstalled = False
  if os.path.exists(os.path.abspath(moduleFile)):
    with open(moduleFile, "rt") as f:
      for line in f.readlines():
        if f'PARFLOW_HAVE_{module}' in line and 'yes' in line:
          hasModuleInstalled = True
  else:
    print(f'Cannot find Makefile.config in {os.path.abspath(moduleFile)}.')
  return hasModuleInstalled

# -----------------------------------------------------------------------------
# Validation classes
# -----------------------------------------------------------------------------

class ValidationException(Exception):
  '''
  Basic parflow exception used for domains to report error
  '''
  pass

# -----------------------------------------------------------------------------
class MandatoryValue:
  def validate(self, value, **kwargs):
    errors = []

    if value == None:
      errors.append(error('Needs to be set'))
      return errors

    return errors


class IntValue:
  '''
  IntRange domain allow to constrain value to be an integer
  while also ensure optionally if its value needs to be
  above or below another one.

  The expected set of keyword arguments are:
    - minValue: If available the value must be strictly above it
    - maxValue: If available the value must be strictly below it
  '''
  # NEED TO COME UP WITH A BETTER WAY TO HANDLE THE VARIABLE DZ CORNER CASE
  def validate(self, value, minValue=None, maxValue=None, intoList=False, **kwargs):
    errors = []

    if value == None:
      return errors

    if not isinstance(value, int):
      errors.append(error('Needs to be an integer'))

    if intoList:
      return errors

    if minValue != None and value < minValue:
      errors.append(error(f'Is smaller than min: {minValue}'))
    if maxValue != None and value > maxValue:
      errors.append(error(f'Is greater than max: {maxValue}'))

    return errors


class DoubleValue:
  '''
  DoubleValue domain allow to constrain value to be a double
  while also ensure optionally if its value needs to be
  above or below another one.

  The expected set of keyword arguments are:
    - minValue: If available the value must be strictly above it
    - maxValue: If available the value must be strictly below it
  '''
  def validate(self, value, minValue=None, maxValue=None, negInt=None, **kwargs):
    errors = []

    if value == None:
      return errors

    # added for verification of DumpInterval (double if positive, int if negative)
    if negInt == True and isinstance(value, int) and value < 0:
      return errors

    elif not isinstance(value, float):
      errors.append(error('Needs to be a double'))

    if minValue != None and value < minValue:
      errors.append(error(f'Is smaller than min: {minValue}'))
    if maxValue != None and value > maxValue:
      errors.append(error(f'Is greater than max: {maxValue}'))

    return errors

# -----------------------------------------------------------------------------

class EnumDomain:
  def validate(self, value, enumList=[], **kwargs):
    errors = []

    if value == None:
      return errors

    if isinstance(value, list) and len(value) == 1:
      value = value[0]

    if value not in enumList:
      strList = ', '.join(enumList)
      errors.append(error(f'{value} must be one of [{strList}]'))

    return errors

# -----------------------------------------------------------------------------

class AnyString:
  def validate(self, value, **kwargs):
    errors = []

    if value == None:
      return errors

    if isinstance(value, list) or isinstance(value, str):
      return errors

    errors.append(error(f'{value} ({type(value)} must be a string'))
    return errors

# -----------------------------------------------------------------------------

class BoolDomain:
  def validate(self, value, **kwargs):
    errors = []

    if value == None:
      return errors

    if isinstance(value, bool):
      return errors

    errors.append(error(f'{value} ({type(value)} must be True/False)'))
    return errors

# -----------------------------------------------------------------------------

class ValidFile:
  def validate(self, value, workingDirectory=None, **kwargs):
    errors = []

    if value == None:
      return errors

    if workingDirectory == None:
      errors.append(error('Working directory is not defined'))
      return errors

    if os.path.exists(os.path.join(workingDirectory, value)):
      return errors

    errors.append(error(f'Could not locate file {os.path.abspath(os.path.join(workingDirectory, value))}'))
    return errors

# -----------------------------------------------------------------------------

class Deprecated:
  def validate(self, value, arg, pfVersion=None, **kwargs):
    errors = []

    if value == None:
      return errors

    version = getComparableVersion(arg)
    currentVersion = getComparableVersion(pfVersion)

    if version <= currentVersion:
      errors.append(error(f'Deprecated in v{arg}'))

    if version > currentVersion:
      errors.append(warning(f'Will be deprecated in v{arg}'))

    return errors

# -----------------------------------------------------------------------------

class Removed:
  def validate(self, value, arg, pfVersion=None, **kwargs):
    errors = []

    if value == None:
      return errors

    version = getComparableVersion(arg)
    currentVersion = getComparableVersion(pfVersion)

    if version <= currentVersion:
      errors.append(error(f'Removed in v{arg}'))

    if version > currentVersion:
      errors.append(warning(f'Will be removed in v{arg}'))

    return errors

# -----------------------------------------------------------------------------

class RequiresModule:
  def validate(self, value, arg, **kwargs):
    errors = []

    if value == None:
      return errors

    argList = arg.split() if isinstance(arg, str) else arg

    for module in argList:
      if not getInstalledParFlowModule(module):
        errors.append(error(f'Need to install {module} module'))

    return errors

# -----------------------------------------------------------------------------
# Helper map with an instance of each domain type
# -----------------------------------------------------------------------------

AVAILABLE_DOMAINS = {}

def getDomain(className):
  if className in AVAILABLE_DOMAINS:
    return AVAILABLE_DOMAINS[className]

  if hasattr(sys.modules[__name__], className):
    klass = getattr(sys.modules[__name__], className)
    instance = klass()
    AVAILABLE_DOMAINS[className] = instance
    return instance

  print(f'{term.FAIL}{termSymbol.ko}{term.ENDC} Could not find domain: "{className}"')

  return None

# -----------------------------------------------------------------------------
# API meant to be used outside of this module
# -----------------------------------------------------------------------------

def validateValueWithErrors(value, domainDefinitions=None, domainAddOnKwargs=None):
  '''
  domainDefinitions = {
    IntRangeDomain: {
      minValue: 1
    },
    NoNoneValueDomain:
  }
  '''
  errors = []
  if not domainDefinitions:
    return errors

  for domain_classname in domainDefinitions:
    domain = getDomain(domain_classname)
    if domain:
      domain_kwargs = {}
      if domainAddOnKwargs:
        domain_kwargs.update(domainAddOnKwargs)

      if domainDefinitions[domain_classname]:
        if isinstance(domainDefinitions[domain_classname], str):
          domain_kwargs['arg'] = domainDefinitions[domain_classname]
        elif isinstance(domainDefinitions[domain_classname], list):
          domain_kwargs['arg'] = domainDefinitions[domain_classname]
        else:
          domain_kwargs.update(domainDefinitions[domain_classname])

      errors.extend(domain.validate(value, **domain_kwargs))

  return errors

# -----------------------------------------------------------------------------

def validateValueWithException(value, domainDefinition=None, domainAddOnKwargs=None, exitOnError=False):
  allMessages = validateValueWithErrors(value, domainDefinition, domainAddOnKwargs)
  errors = filterErrorsByType('ERROR', allMessages)

  if len(errors):
    print()
    try:
      raise ValidationException()
    except ValidationException:
      exp, val, tb = sys.exc_info()
      listing = traceback.format_stack(tb.tb_frame)
      for item in listing:
        if 'parflow/database' in item:
          continue
        print(item)

    print(f'    The value {value} is invalid')
    for error in errors:
      print(f'    - {error}')
    print()

    if exitOnError:
      sys.exit(1)


# -----------------------------------------------------------------------------

def validateValueWithPrint(name, value, domainDefinition=None, domainAddOnKwargs=None, history=None, indent=1):
  indentStr = '  '* (indent - 1)
  allMessages = validateValueWithErrors(value, domainDefinition, domainAddOnKwargs)
  errors = filterErrorsByType('ERROR', allMessages)
  warnings = filterErrorsByType('WARNING', allMessages)

  if len(errors):
    print(f'{indentStr}  {term.FAIL}{termSymbol.ko}{term.ENDC} {name}: {value}')
    for error in errors:
      print(f'{indentStr}    {term.WARNING}{termSymbol.errorItem}{term.ENDC} {error}')
  elif value != None:
    # checking for duplicates and changing print statement
    if history != None:
      dupCount = duplicateSearch(history)
      if dupCount != None and dupCount >= 1:
        # offset = 1 if 'default' in name else 1
        dup_str = '('
        for val in range(dupCount-1):
          dup_str += str(history[val]) + ' => '
        dup_str += str(history[dupCount-1]) + ')'
        print(f'{indentStr}  {term.MAGENTA}{termSymbol.warning}{term.ENDC} {name}: {value}  {term.MAGENTA}{dup_str}{term.ENDC}')
      # elif 'default' in name
      else:
        print(f'{indentStr} {name}: {value} {term.OKGREEN}{termSymbol.ok}{term.ENDC}')
    else:
      print(f'{indentStr}  {name}: {value} {term.OKGREEN}{termSymbol.ok}{term.ENDC}')

  if len(warnings):
    for warning in warnings:
      print(f'{indentStr}    {term.CYAN}{termSymbol.warning}{term.ENDC} {warning}')

  return len(errors)

def validateValueToString(name, value, domainDefinition=None, domainAddOnKwargs=None, history=None, indent=1):
  indentStr = '  '* (indent - 1)
  allMessages = validateValueWithErrors(value, domainDefinition, domainAddOnKwargs)
  errors = filterErrorsByType('ERROR', allMessages)
  warnings = filterErrorsByType('WARNING', allMessages)
  validationString = []

  if len(errors):
    validationString.append(f'{value} {term.FAIL}{termSymbol.ko}{term.ENDC}')
    for error in errors:
      validationString.append(f'{indentStr}    {term.WARNING}{termSymbol.errorItem}{term.ENDC} {error}')
  elif value != None:
    # checking for duplicates and changing print statement
    if history != None:
      dupCount = duplicateSearch(history)
      if dupCount != None and dupCount >= 1:
        # offset = 1 if 'default' in name else 1
        dup_str = '('
        for val in range(dupCount-1):
          dup_str += str(history[val]) + ' => '
        dup_str += str(history[dupCount-1]) + ')'
        validationString.append(f'{term.MAGENTA}{termSymbol.warning}{term.ENDC} {value}  {term.MAGENTA}{dup_str}{term.ENDC}')
      # elif 'default' in name
      else:
        validationString.append(f'{value} {term.OKGREEN}{termSymbol.ok}{term.ENDC}')
    else:
      validationString.append(f'{value} {term.OKGREEN}{termSymbol.ok}{term.ENDC}')

  if len(warnings):
    for warning in warnings:
      validationString.append(f'{indentStr}    {term.CYAN}{termSymbol.warning}{term.ENDC} {warning}')

  return len(allMessages), '\n'.join(validationString)