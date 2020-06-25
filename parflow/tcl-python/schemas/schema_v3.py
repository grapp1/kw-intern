# schema_v3.py: defining each set of keys as a class, works with autocomplete

class parflow:
  """Hello, welcome to ParFlow"""
  def __init__(self, runname='runname'):
    self.Process = Process()

class Process:
  """This section describes how processors are
  assigned in order to solve the domain in parallel.
  """
  def __init__(self):
    self.Topology = Topology()


class Topology:
  """Process.Topology.P assigns the process splits in the x direction.
  Process.Topology.Q assigns the process splits in the y direction.
  Process.Topology.R assigns the process splits in the z direction.
  """
  def __init__(self):
    self.P = 1
    self.Q = 1
    self.R = 1





