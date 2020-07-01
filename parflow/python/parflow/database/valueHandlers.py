r'''
This module aims to gather all kind of value handler you would like to
enable inside Parflow run.

A value handler is responsible to process the user input and returned
a possibly modified version of it while maybe affecting that container
object along the way.
'''

# -----------------------------------------------------------------------------

class ValueHandlerException(Exception):
  '''
  Basic parflow exception used for ValueHandlers to report error
  '''
  pass

# -----------------------------------------------------------------------------

class GeometryNameHandler:
  def decorate(self, value, container):
    from .generated import GeomInputItem
    if isinstance(value, str):
      names = value.split(' ')
      valideNames = []
      for name in names:
        if len(name):
          valideNames.append(name)
          obj = GeomInputItem()
          obj.Name = name
          container.__dict__[name] = obj

      return valideNames

    if hasattr(value, '__iter__'):
      valideNames = []
      for name in value:
        if len(name):
          valideNames.append(name)
          obj = GeomInputItem()
          obj.Name = name
          container.__dict__[name] = obj

      return valideNames

    raise ValueHandlerException(
        f'{value} is not of the expected type for GeometryNameHandler')

# -----------------------------------------------------------------------------
# Helper map with an instance of each Value handler
# -----------------------------------------------------------------------------

AVAILABLE_HANDLERS = {
  'GeometryNameHandler': GeometryNameHandler(),
}

# -----------------------------------------------------------------------------
# API meant to be used outside of this module
# -----------------------------------------------------------------------------

def decorateValue(value, container=None, handlerName=None):
  if not handlerName or handlerName not in AVAILABLE_HANDLERS:
    return value

  handler = AVAILABLE_HANDLERS[handlerName]
  return handler.decorate(value, container)
