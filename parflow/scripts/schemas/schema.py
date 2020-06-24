# schema_v1.py

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

    # def setComputationalGridDefinition(self):
    #     self.ComputationalGrid.Lower.X = 0.0
    #     self.ComputationalGrid.Lower.Y = 0.0
    #     self.ComputationalGrid.Lower.Z = 0.0
    #
    #     self.ComputationalGrid.NX = 1
    #     self.ComputationalGrid.NY = 1
    #     self.ComputationalGrid.NZ = 1
    #
    #     self.ComputationalGrid.DX = 1
    #     self.ComputationalGrid.DY = 1
    #     self.ComputationalGrid.DZ = 1
