#  This runs the basic pfmg test case based off of default richards
#  This run, as written in this input file, should take
#  3 nonlinear iterations.

#
# Import the ParFlow TCL package
#
from parflow import Run
pfmg = Run("pfmg", __file__)

pfmg.FileVersion = 4

pfmg.Process.Topology.P = 1
pfmg.Process.Topology.Q = 1
pfmg.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
pfmg.ComputationalGrid.Lower.X = -10.0
pfmg.ComputationalGrid.Lower.Y = 10.0
pfmg.ComputationalGrid.Lower.Z = 1.0

pfmg.ComputationalGrid.DX = 8.8888888888888893
pfmg.ComputationalGrid.DY = 10.666666666666666
pfmg.ComputationalGrid.DZ = 1.0

pfmg.ComputationalGrid.NX = 10
pfmg.ComputationalGrid.NY = 10
pfmg.ComputationalGrid.NZ = 8

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
pfmg.GeomInput.Names = 'domain_input background_input source_region_input concen_region_input'


#---------------------------------------------------------
# Domain Geometry Input
#---------------------------------------------------------
pfmg.GeomInput.domain_input.InputType = 'Box'
pfmg.GeomInput.domain_input.GeomName = 'domain'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
pfmg.Geom.domain.Lower.X = -10.0
pfmg.Geom.domain.Lower.Y = 10.0
pfmg.Geom.domain.Lower.Z = 1.0

pfmg.Geom.domain.Upper.X = 150.0
pfmg.Geom.domain.Upper.Y = 170.0
pfmg.Geom.domain.Upper.Z = 9.0

pfmg.Geom.domain.Patches = 'left right front back bottom top'

#---------------------------------------------------------
# Background Geometry Input
#---------------------------------------------------------
pfmg.GeomInput.background_input.InputType = 'Box'
pfmg.GeomInput.background_input.GeomName = 'background'

#---------------------------------------------------------
# Background Geometry
#---------------------------------------------------------
pfmg.Geom.background.Lower.X = -99999999.0
pfmg.Geom.background.Lower.Y = -99999999.0
pfmg.Geom.background.Lower.Z = -99999999.0

pfmg.Geom.background.Upper.X = 99999999.0
pfmg.Geom.background.Upper.Y = 99999999.0
pfmg.Geom.background.Upper.Z = 99999999.0


#---------------------------------------------------------
# Source_Region Geometry Input
#---------------------------------------------------------
pfmg.GeomInput.source_region_input.InputType = 'Box'
pfmg.GeomInput.source_region_input.GeomName = 'source_region'

#---------------------------------------------------------
# Source_Region Geometry
#---------------------------------------------------------
pfmg.Geom.source_region.Lower.X = 65.56
pfmg.Geom.source_region.Lower.Y = 79.34
pfmg.Geom.source_region.Lower.Z = 4.5

pfmg.Geom.source_region.Upper.X = 74.44
pfmg.Geom.source_region.Upper.Y = 89.99
pfmg.Geom.source_region.Upper.Z = 5.5


#---------------------------------------------------------
# Concen_Region Geometry Input
#---------------------------------------------------------
pfmg.GeomInput.concen_region_input.InputType = 'Box'
pfmg.GeomInput.concen_region_input.GeomName = 'concen_region'

#---------------------------------------------------------
# Concen_Region Geometry
#---------------------------------------------------------
pfmg.Geom.concen_region.Lower.X = 60.0
pfmg.Geom.concen_region.Lower.Y = 80.0
pfmg.Geom.concen_region.Lower.Z = 4.0

pfmg.Geom.concen_region.Upper.X = 80.0
pfmg.Geom.concen_region.Upper.Y = 100.0
pfmg.Geom.concen_region.Upper.Z = 6.0

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
pfmg.Geom.Perm.Names = 'background'

pfmg.Geom.background.Perm.Type = 'Constant'
pfmg.Geom.background.Perm.Value = 4.0

pfmg.Perm.TensorType = 'TensorByGeom'

pfmg.Geom.Perm.TensorByGeom.Names = 'background'

pfmg.Geom.background.Perm.TensorValX = 1.0
pfmg.Geom.background.Perm.TensorValY = 1.0
pfmg.Geom.background.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

pfmg.SpecificStorage.Type = 'Constant'
pfmg.SpecificStorage.GeomNames = 'domain'
pfmg.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

pfmg.Phase.Names = 'water'

pfmg.Phase.water.Density.Type = 'Constant'
pfmg.Phase.water.Density.Value = 1.0

pfmg.Phase.water.Viscosity.Type = 'Constant'
pfmg.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
pfmg.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------
pfmg.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

pfmg.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

pfmg.TimingInfo.BaseUnit = 1.0
pfmg.TimingInfo.StartCount = 0
pfmg.TimingInfo.StartTime = 0.0
pfmg.TimingInfo.StopTime = 0.010
pfmg.TimingInfo.DumpInterval = -1
pfmg.TimeStep.Type = 'Constant'
pfmg.TimeStep.Value = 0.001

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

pfmg.Geom.Porosity.GeomNames = 'background'

pfmg.Geom.background.Porosity.Type = 'Constant'
pfmg.Geom.background.Porosity.Value = 1.0

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
pfmg.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

pfmg.Phase.RelPerm.Type = 'VanGenuchten'
pfmg.Phase.RelPerm.GeomNames = 'domain'
pfmg.Geom.domain.RelPerm.Alpha = 0.005
pfmg.Geom.domain.RelPerm.N = 2.0

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

pfmg.Phase.Saturation.Type = 'VanGenuchten'
pfmg.Phase.Saturation.GeomNames = 'domain'
pfmg.Geom.domain.Saturation.Alpha = 0.005
pfmg.Geom.domain.Saturation.N = 2.0
pfmg.Geom.domain.Saturation.SRes = 0.2
pfmg.Geom.domain.Saturation.SSat = 0.99

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
pfmg.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
pfmg.Cycle.Names = 'constant'
pfmg.Cycle.constant.Names = 'alltime'
pfmg.Cycle.constant.alltime.Length = 1
pfmg.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
pfmg.BCPressure.PatchNames = 'left right front back bottom top'

pfmg.Patch.left.BCPressure.Type = 'DirEquilRefPatch'
pfmg.Patch.left.BCPressure.Cycle = 'constant'
pfmg.Patch.left.BCPressure.RefGeom = 'domain'
pfmg.Patch.left.BCPressure.RefPatch = 'bottom'
pfmg.Patch.left.BCPressure.alltime.Value = 5.0

pfmg.Patch.right.BCPressure.Type = 'DirEquilRefPatch'
pfmg.Patch.right.BCPressure.Cycle = 'constant'
pfmg.Patch.right.BCPressure.RefGeom = 'domain'
pfmg.Patch.right.BCPressure.RefPatch = 'bottom'
pfmg.Patch.right.BCPressure.alltime.Value = 3.0

pfmg.Patch.front.BCPressure.Type = 'FluxConst'
pfmg.Patch.front.BCPressure.Cycle = 'constant'
pfmg.Patch.front.BCPressure.alltime.Value = 0.0

pfmg.Patch.back.BCPressure.Type = 'FluxConst'
pfmg.Patch.back.BCPressure.Cycle = 'constant'
pfmg.Patch.back.BCPressure.alltime.Value = 0.0

pfmg.Patch.bottom.BCPressure.Type = 'FluxConst'
pfmg.Patch.bottom.BCPressure.Cycle = 'constant'
pfmg.Patch.bottom.BCPressure.alltime.Value = 0.0

pfmg.Patch.top.BCPressure.Type = 'FluxConst'
pfmg.Patch.top.BCPressure.Cycle = 'constant'
pfmg.Patch.top.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

pfmg.TopoSlopesX.Type = 'Constant'
pfmg.TopoSlopesX.GeomNames = 'domain'

pfmg.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

pfmg.TopoSlopesY.Type = 'Constant'
pfmg.TopoSlopesY.GeomNames = 'domain'

pfmg.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

pfmg.Mannings.Type = 'Constant'
pfmg.Mannings.GeomNames = 'domain'
pfmg.Mannings.Geom.domain.Value = 0.

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

pfmg.ICPressure.Type = 'HydroStaticPatch'
pfmg.ICPressure.GeomNames = 'domain'
pfmg.Geom.domain.ICPressure.Value = 3.0
pfmg.Geom.domain.ICPressure.RefGeom = 'domain'
pfmg.Geom.domain.ICPressure.RefPatch = 'bottom'

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

pfmg.PhaseSources.water.Type = 'Constant'
pfmg.PhaseSources.water.GeomNames = 'background'
pfmg.PhaseSources.water.Geom.background.Value = 0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

pfmg.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------
pfmg.Solver = 'Richards'
pfmg.Solver.MaxIter = 5

pfmg.Solver.Nonlinear.MaxIter = 10
pfmg.Solver.Nonlinear.ResidualTol = 1e-9
pfmg.Solver.Nonlinear.EtaChoice = 'EtaConstant'
pfmg.Solver.Nonlinear.EtaValue = 1e-5
pfmg.Solver.Nonlinear.UseJacobian = True
pfmg.Solver.Nonlinear.DerivativeEpsilon = 1e-2

pfmg.Solver.Linear.KrylovDimension = 10

pfmg.Solver.Linear.Preconditioner = 'PFMG'
pfmg.Solver.Linear.Preconditioner.PFMG.Smoother = 'WJacobi'

#pfset Solver.Linear.Preconditioner.PFMG.MaxIter          1
#pfset Solver.Linear.Preconditioner.PFMG.NumPreRelax      100
#pfset Solver.Linear.Preconditioner.PFMG.NumPostRelax     100


#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

pfmg.run()
