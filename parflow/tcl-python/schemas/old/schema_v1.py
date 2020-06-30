# schema_v1.py: initial building with DotMap (does not work with autocomplete)

from dotmap import DotMap

class parflow(DotMap):

    """Hello, welcome to ParFlow"""

    def __init__(self, runname='runname'):
        super().__init__(self)
        self.runname = runname

    def setProcessTopology(self):
        """This section describes how processors are
        assigned in order to solve the domain in parallel.

        Process.Topology.P assigns the process splits in the x direction.
        Process.Topology.Q assigns the process splits in the y direction.
        Process.Topology.R assigns the process splits in the z direction."""
        self.Process.Topology.P = 1
        self.Process.Topology.Q = 1
        self.Process.Topology.R = 1


