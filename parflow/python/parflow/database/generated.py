r'''
--- DO NOT EDIT ---
File automatically generated - any manual change will be lost
Generated on 2020/06/30 - 19:21:43
'''
from .core import PFDBObj

# ------------------------------------------------------------------------------

class Process(PFDBObj):
  '''
  run.Process input options are: Topology
  '''
  def __init__(self):
    self.Topology = Topology()

# ------------------------------------------------------------------------------

class Topology(PFDBObj):
  '''
  [Type: int] This section describes how processors are assigned in order to solve the domain in parallel.
    - P allocates the number of processes to the grid-cells in x.
    - Q allocates the number of processes to the grid-cells in y.
    - R allocates the number of processes to the grid-cells in z.
  Please note R should always be 1 if you are running with Solver Richards unless you are running a totally saturated domain (solver IMPES).'
  '''
  def __init__(self):
    self.P = 1
    self.Q = 1
    self.R = 1
    self._details = {
      "P": {
        "help": "[Type: int] P allocates the number of processes to the grid-cells in x.\n",
        "default": 1,
        "domain": {
          "type": "IntRangeDomain",
          "minValue": 1
        }
      },
      "Q": {
        "help": "[Type: int] Q allocates the number of processes to the grid-cells in y.\n",
        "default": 1,
        "domain": {
          "type": "IntRangeDomain",
          "minValue": 1
        }
      },
      "R": {
        "help": "[Type: int] R allocates the number of processes to the grid-cells in z. Please note R should always be 1 if you are running with Solver Richards unless you are running a totally saturated domain (solver IMPES).\n",
        "default": 1,
        "domain": {
          "type": "IntRangeDomain",
          "minValue": 1
        }
      }
    }

# ------------------------------------------------------------------------------

class GeomInput(PFDBObj):
  '''
  Write something meaningful...
  '''
  def __init__(self):
    self.Names = None
    self._details = {
      "Names": {
        "help": "List of names to use for defining geometry regions\n",
        "domain": {
          "type": "AnyStringDomain"
        },
        "valueHandler": "GeometryNameHandler"
      }
    }

# ------------------------------------------------------------------------------

class Geom(PFDBObj):
  '''
  Geometry instance
  '''
  def __init__(self):
    self.Name = None
    self.X = 0
    self.Y = 1
    self.Z = 2
    self._details = {
      "Name": {
        "help": "Name of the geometry"
      },
      "X": {
        "help": "X geometry",
        "default": 0
      },
      "Y": {
        "help": "Y geometry",
        "default": 1
      },
      "Z": {
        "help": "Z geometry",
        "default": 2
      }
    }
