r'''
This module aims to gather all kind of value validation you would like to
enable inside Parflow run.
'''

import sys
import types
import traceback

from . import TerminalColors as term
from . import TerminalSymbols as termSymbol

# -----------------------------------------------------------------------------

class ValidationException(Exception):
  '''
  Basic parflow exception used for domains to report error
  '''
  pass

# -----------------------------------------------------------------------------

class IntRangeDomain:
  '''
  IntRange domain allow to constrain value to be an integer
  while also ensure optionally if its value needs to be
  above or below another one.

  The expected set of keyword arguments are:
    - minValue: If available the value must be strictly above it
    - maxValue: If available the value must be strictly below it
  '''
  def validate(self, value, minValue=None, maxValue=None, **kwargs):
    errors = []

    if value == None:
      errors.append('Needs to be set')
      return errors

    if not isinstance(value, int):
      errors.append('Needs to be an integer')

    if minValue != None and value < minValue:
      errors.append(f'Is smaller than min: {minValue}')
    if maxValue != None and value > maxValue:
      errors.append(f'Is greater than max: {maxValue}')

    return errors


class DoubleRangeDomain:
  '''
  DoubleRange domain allow to constrain value to be a double
  while also ensure optionally if its value needs to be
  above or below another one.

  The expected set of keyword arguments are:
    - minValue: If available the value must be strictly above it
    - maxValue: If available the value must be strictly below it
  '''
  def validate(self, value, minValue=None, maxValue=None, **kwargs):
    errors = []

    if value == None:
      errors.append('Needs to be set')
      return errors

    if not isinstance(value, float):
      errors.append('Needs to be a double')

    if minValue != None and value < minValue:
      errors.append(f'Is smaller than min: {minValue}')
    if maxValue != None and value > maxValue:
      errors.append(f'Is greater than max: {maxValue}')

    return errors

# -----------------------------------------------------------------------------

class EnumDomain:
  def validate(self, value, enumList=[], **kwargs):
    errors = []
    if value not in enumList:
      strList = ', '.join(enumList)
      errors.append(f'{value} must be one of [{strList}]')

    return errors

# -----------------------------------------------------------------------------

class AnyStringDomain:
  def validate(self, value, **kwargs):
    errors = []
    if isinstance(value, list) or isinstance(value, str):
      return errors

    errors.append(f'{value} ({type(value)} must be a string')
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

def validateValueWithErrors(value, domainDefinitions=None):
  '''
  domainDefinitions = {
    IntRangeDomain: {
      minValue: 1
    },
    NoNoneValueDomain: '__no_args__'
  }
  '''
  errors = []
  if not domainDefinitions:
    return errors

  for domain_classname in domainDefinitions:
    domain = getDomain(domain_classname)
    if domain:
      domain_kwargs = domainDefinitions[domain_classname]
      if isinstance(domain_kwargs, str):
        errors.extend(domain.validate(value))
      else:
        errors.extend(domain.validate(value, **domain_kwargs))

  return errors

# -----------------------------------------------------------------------------

def validateValueWithException(value, domainDefinition=None, exitOnError=False):
  errors = validateValueWithErrors(value, domainDefinition)

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

def validateValueWithPrint(name, value, domainDefinition=None, indent=1):
  indentStr = '  '* (indent - 1)
  errors = validateValueWithErrors(value, domainDefinition)

  if len(errors):
    print(f'{indentStr}  {term.FAIL}{termSymbol.ko}{term.ENDC} {name}: {value}')
    for error in errors:
      print(f'{indentStr}    {term.WARNING}{termSymbol.errorItem}{term.ENDC} {error}')
  else:
    print(f'{indentStr}  {term.OKGREEN}{termSymbol.ok}{term.ENDC} {name}: {value}')

  return len(errors)
