r'''
This module aims to gather all kind of value handler you would like to
enable inside Parflow run.

A value handler is responsible to process the user input and returned
a possibly modified version of it while maybe affecting that container
object along the way.
'''

import sys
from . import generated

# -----------------------------------------------------------------------------

class ValueHandlerException(Exception):
  '''
  Basic parflow exception used for ValueHandlers to report error
  '''
  pass

# -----------------------------------------------------------------------------


class ChildrenHandler:
  def decorate(self, value, container, className=None, **kwargs):
    klass = getattr(generated, className)
    if isinstance(value, str):
      names = value.split(' ')
      valideNames = []
      for name in names:
        if len(name):
          valideNames.append(name)
          container.__dict__[name] = klass()

      return valideNames

    if hasattr(value, '__iter__'):
      valideNames = []
      for name in value:
        if len(name):
          valideNames.append(name)
          container.__dict__[name] = klass()

      return valideNames

    raise ValueHandlerException(
        f'{value} is not of the expected type for GeometryNameHandler')

# -----------------------------------------------------------------------------
# Helper map with an instance of each Value handler
# -----------------------------------------------------------------------------

AVAILABLE_HANDLERS = {}

def getHandler(className):
  if className in AVAILABLE_HANDLERS:
    return AVAILABLE_HANDLERS[className]

  if hasattr(sys.modules[__name__], className):
    klass = getattr(sys.modules[__name__], className)
    instance = klass()
    AVAILABLE_HANDLERS[className] = instance
    return instance

  print(f'Could not find valueHandler: "{className}"')

  return None

# -----------------------------------------------------------------------------
# API meant to be used outside of this module
# -----------------------------------------------------------------------------

def decorateValue(value, container=None, valueHandler=None):
  if valueHandler == None or 'type' not in valueHandler:
    return value

  className = valueHandler["type"]
  handler = getHandler(className)

  if handler:
    return handler.decorate(value, container, **valueHandler)

  return value
