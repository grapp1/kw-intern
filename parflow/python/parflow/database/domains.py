r'''
This module aims to gather all kind of value validation you would like to
enable inside Parflow run.
'''

import sys
import types
import traceback

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


class AnyDoubleDomain:
  def validate(self, value, **kwargs):
    errors = []
    if isinstance(value, float):
      return errors

    errors.append(f'{value} must be a double')
    return errors

# -----------------------------------------------------------------------------
# Helper map with an instance of each domain type
# -----------------------------------------------------------------------------

AVAILABLE_DOMAINS = {
  'IntRangeDomain': IntRangeDomain(),
  'EnumDomain': EnumDomain(),
  'AnyStringDomain': AnyStringDomain(),
  'AnyDoubleDomain': AnyDoubleDomain(),
}

class bgcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

# -----------------------------------------------------------------------------
# API meant to be used outside of this module
# -----------------------------------------------------------------------------

def validateValueWithErrors(value, domainDefinition=None):
  errors = []
  if domainDefinition and domainDefinition['type'] in AVAILABLE_DOMAINS:
    domainObj = AVAILABLE_DOMAINS[domainDefinition['type']]
    errors = domainObj.validate(value, **domainDefinition)

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


    # for i in range(3):
    #   tb_frame = tb_frame.f_back
    #   tb_lasti = tb_frame.f_lasti
    #   f_lineno = tb_frame.f_lineno

    # back_tb = types.TracebackType(tb_next=None,
    #                               tb_frame=tb_frame,
    #                               tb_lasti=tb_lasti,
    #                               tb_lineno=f_lineno)
    # raise ValidationException(errorString).with_traceback(back_tb)

# -----------------------------------------------------------------------------

def validateValueWithPrint(name, value, domainDefinition=None, indent=1):
  indentStr = '  '* (indent - 1)
  ok = u'\u2714'
  ko = u'\u2718'
  errorItem = u'\u2605'
  errors = validateValueWithErrors(value, domainDefinition)

  if len(errors):
    print(f'{indentStr}  {bgcolors.FAIL}{ko}{bgcolors.ENDC} {name}: {value}')
    for error in errors:
      print(f'{indentStr}    {bgcolors.WARNING}{errorItem}{bgcolors.ENDC} {error}')
  else:
    print(f'{indentStr}  {bgcolors.OKGREEN}{ok}{bgcolors.ENDC} {name}: {value}')

  return len(errors)
