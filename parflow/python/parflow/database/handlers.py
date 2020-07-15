r'''
This module aims to gather all kind of value handler you would like to
enable inside Parflow run.

A value handler is responsible to process the user input and returned
a possibly modified version of it while maybe affecting that container
object along the way.
'''

import sys
from . import generated
from . import TerminalColors as term
from . import TerminalSymbols as termSymbol

# -----------------------------------------------------------------------------

class ValueHandlerException(Exception):
  '''
  Basic parflow exception used for ValueHandlers to report error
  '''
  pass

# -----------------------------------------------------------------------------


class ChildrenHandler:
  def decorate(self, value, container, className=None, location='.', **kwargs):
    klass = getattr(generated, className)
    destination_containers = container.getObjsFromLocation(location)
    # print(container.__class__)

    if isinstance(value, str):
      names = value.split(' ')
      valideNames = []
      for name in names:
        if len(name):
          # print(f' - {name} => {className} in {destination_container.__class__}')
          valideNames.append(name)
          for destination_container in destination_containers:
            destination_container.__dict__[name] = klass(destination_container)

      return valideNames

    if hasattr(value, '__iter__'):
      valideNames = []
      for name in value:
        if len(name):
          valideNames.append(name)
          # print(f' - {name} => {className} in {destination_container.__class__}')
          for destination_container in destination_containers:
            destination_container.__dict__[name] = klass(destination_container)

      return valideNames

    raise ValueHandlerException(
        f'{value} is not of the expected type for GeometryNameHandler')

# -----------------------------------------------------------------------------
# Helper map with an instance of each Value handler
# -----------------------------------------------------------------------------

AVAILABLE_HANDLERS = {}

def getHandler(className, printError=True):
  if className in AVAILABLE_HANDLERS:
    return AVAILABLE_HANDLERS[className]

  if hasattr(sys.modules[__name__], className):
    klass = getattr(sys.modules[__name__], className)
    instance = klass()
    AVAILABLE_HANDLERS[className] = instance
    return instance

  if printError:
    print(f'{term.FAIL}{termSymbol.ko}{term.ENDC} Could not find handler: "{className}"')

  return None

# -----------------------------------------------------------------------------
# API meant to be used outside of this module
# -----------------------------------------------------------------------------

def decorateValue(value, container=None, handlers=None):
  '''
  handlers = {
      GeomInputUpdater: {
        type: 'ChildrenHandler',
        className: 'GeomInputItemValue',
        location: '../..'
      },
      GeomUpdater: {
        type: 'ChildrenHandler',
        className: 'GeomItem',
        location: '../../Geom'
      },
      ChildrenHandler: {
        className: 'GeomInputLocal'
      }
  }
  '''
  if handlers == None:
    return value

  return_value = value

  for handler_classname in handlers:
    handler = getHandler(handler_classname, False)

    if not handler and 'type' in handlers[handler_classname]:
      handler = getHandler(handlers[handler_classname]['type'])
    else:
      getHandler(handler_classname)

    if handler:
      handler_kwargs = handlers[handler_classname]
      if isinstance(handler_kwargs, str):
        return_value = handler.decorate(value, container)
      else:
        return_value = handler.decorate(value, container, **handler_kwargs)

  return return_value