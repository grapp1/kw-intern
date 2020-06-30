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
    if minValue != None and value < minValue:
      raise ValidationException(f'{value} is smaller than min int: {minValue}')
    if maxValue != None and value > maxValue:
      raise ValidationException(f'{value} is greater than max int: {maxValue}')

# -----------------------------------------------------------------------------

class EnumDomain:
  def validate(self, value, enumList=[]):
    if value not in enumList:
      raise ValidationException('{:s} must be one of [{:s}]'.format(value, ','.join(enumList)))

# -----------------------------------------------------------------------------

class AnyStringDomain:
  def validate(self, value):
    if not isinstance(value, str):
      raise ValidationException(f'{value} ({type(value)} must be a string')


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

def validateValueWithException(value, domainDefinition=None):
  if domainDefinition and domainDefinition['type'] in AVAILABLE_DOMAINS:
    domainObj = AVAILABLE_DOMAINS[domain['type']]
    if 'kwargs' in domainDefinition:
        domainObj.validate(value, **domainDefinition['kwargs'])
     else:
        domainObj.validate(value)

# -----------------------------------------------------------------------------

def validateValueWithPrint(value, domainDefinition=None, indent=1):
  indentStr = '  '*indent
  errorCount = 0

  if domainDefinition and domainDefinition['type'] in AVAILABLE_DOMAINS:
    domainObj = AVAILABLE_DOMAINS[domain['type']]
    if 'kwargs' in domainDefinition:
        errorCount += domainObj.validate(value, indent=indent, **domainDefinition['kwargs'])
     else:
        errorCount += domainObj.validate(value)

  return errorCount
