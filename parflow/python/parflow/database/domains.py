r'''
This module aims to gather all kind of value validation you would like to
enable inside Parflow run.
'''

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
    if minValue != None and value < minValue:
      errors.append(f'{value} is smaller than min int: {minValue}')
    if maxValue != None and value > maxValue:
      errors.append(f'{value} is greater than max int: {maxValue}')

    return errors

# -----------------------------------------------------------------------------

class EnumDomain:
  def validate(self, value, enumList=[]):
    errors = []
    if value not in enumList:
      strList = ', '.join(enumList)
      errors.append(f'{value} must be one of [{strList}]')

    return errors

# -----------------------------------------------------------------------------

class AnyStringDomain:
  def validate(self, value):
    errors = []
    if not isinstance(value, str):
      errors.append(f'{value} ({type(value)} must be a string')

    return errors


# -----------------------------------------------------------------------------
# Helper map with an instance of each domain type
# -----------------------------------------------------------------------------

AVAILABLE_DOMAINS = {
  'IntRangeDomain': IntRangeDomain(),
  'EnumDomain': EnumDomain(),
  'AnyStringDomain': AnyStringDomain()
}

# -----------------------------------------------------------------------------
# API meant to be used outside of this module
# -----------------------------------------------------------------------------

def validateValueWithErrors(value, domainDefinition=None):
  errors = []
  if domainDefinition and domainDefinition['type'] in AVAILABLE_DOMAINS:
    domainObj = AVAILABLE_DOMAINS[domainDefinition['type']]
    if 'kwargs' in domainDefinition:
      errors = domainObj.validate(value, **domainDefinition['kwargs'])
    else:
      errors = domainObj.validate(value)

  return errors

# -----------------------------------------------------------------------------

def validateValueWithException(value, domainDefinition=None):
  errors = validateValueWithErrors(value, domainDefinition)

  if len(errors):
    raise ValidationException('\n'.join(errors))


# -----------------------------------------------------------------------------

def validateValueWithPrint(name, value, domainDefinition=None, indent=1):
  indentStr = '  '*indent
  errors = validateValueWithErrors(value, domainDefinition)

  if len(errors):
    print(f'{indentStr}{name}:')
    for error in errors:
      print(f'{indentStr} - {error}')
  else:
    print(f'{indentStr}{name} - OK')

  return len(errors)
