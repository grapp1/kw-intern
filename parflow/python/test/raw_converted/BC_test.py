#  This runs the tilted-v catchment problem
#  similar to that in Kollet and Maxwell (2006) AWR

#
# Import the ParFlow TCL package
#
from parflow import Run
BC_test = Run("BC_test", __file__)

BC_test.FileVersion = 4

BC_test.Process.Topology.P = 1
BC_test.Process.Topology.Q = 2
BC_test.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
BC_test.ComputationalGrid.Lower.X = 0.0
BC_test.ComputationalGrid.Lower.Y = 0.0
BC_test.ComputationalGrid.Lower.Z = 0.0

BC_test.ComputationalGrid.NX = 30
BC_test.ComputationalGrid.NY = 30
BC_test.ComputationalGrid.NZ = 30

BC_test.ComputationalGrid.DX = 10.0
BC_test.ComputationalGrid.DY = 10.0
BC_test.ComputationalGrid.DZ = .05

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
BC_test.GeomInput.Names = 'domaininput leftinput rightinput channelinput'

BC_test.GeomInput.domaininput.GeomName = 'domain'
BC_test.GeomInput.leftinput.GeomName = 'left'
BC_test.GeomInput.rightinput.GeomName = 'right'
BC_test.GeomInput.channelinput.GeomName = 'channel'

BC_test.GeomInput.domaininput.InputType = 'Box'
BC_test.GeomInput.leftinput.InputType = 'Box'
BC_test.GeomInput.rightinput.InputType = 'Box'
BC_test.GeomInput.channelinput.InputType = 'Box'

#---------------------------------------------------------
# Domain Geometry 
#---------------------------------------------------------
BC_test.Geom.domain.Lower.X = 0.0
BC_test.Geom.domain.Lower.Y = 0.0
BC_test.Geom.domain.Lower.Z = 0.0
#  
BC_test.Geom.domain.Upper.X = 300.0
BC_test.Geom.domain.Upper.Y = 300.0
BC_test.Geom.domain.Upper.Z = 1.5
BC_test.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'

#---------------------------------------------------------
# Left Slope Geometry 
#---------------------------------------------------------
BC_test.Geom.left.Lower.X = 0.0
BC_test.Geom.left.Lower.Y = 0.0
BC_test.Geom.left.Lower.Z = 0.0
#  
BC_test.Geom.left.Upper.X = 140.0
BC_test.Geom.left.Upper.Y = 300.0
BC_test.Geom.left.Upper.Z = 1.5

#---------------------------------------------------------
# Right Slope Geometry 
#---------------------------------------------------------
BC_test.Geom.right.Lower.X = 160.0
BC_test.Geom.right.Lower.Y = 0.0
BC_test.Geom.right.Lower.Z = 0.0
#  
BC_test.Geom.right.Upper.X = 300.0
BC_test.Geom.right.Upper.Y = 300.0
BC_test.Geom.right.Upper.Z = 1.5

#---------------------------------------------------------
# Channel Geometry 
#---------------------------------------------------------
BC_test.Geom.channel.Lower.X = 140.0
BC_test.Geom.channel.Lower.Y = 0.0
BC_test.Geom.channel.Lower.Z = 0.0
#  
BC_test.Geom.channel.Upper.X = 160.0
BC_test.Geom.channel.Upper.Y = 300.0
BC_test.Geom.channel.Upper.Z = 1.5

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

BC_test.Geom.Perm.Names = 'left right channel'

# Values in m/hour

# these are examples to make the upper portions of the v heterogeneous
# the following is ignored if the perm.type "Constant" settings are not
# commented out, below.

BC_test.Geom.left.Perm.Type = 'TurnBands'
BC_test.Geom.left.Perm.LambdaX = 50.
BC_test.Geom.left.Perm.LambdaY = 50.
BC_test.Geom.left.Perm.LambdaZ = 0.5
BC_test.Geom.left.Perm.GeomMean = 0.01

BC_test.Geom.left.Perm.Sigma = 0.5
BC_test.Geom.left.Perm.NumLines = 40
BC_test.Geom.left.Perm.RZeta = 5.0
BC_test.Geom.left.Perm.KMax = 100.0
BC_test.Geom.left.Perm.DelK = 0.2
BC_test.Geom.left.Perm.Seed = 33333
BC_test.Geom.left.Perm.LogNormal = 'Log'
BC_test.Geom.left.Perm.StratType = 'Bottom'


BC_test.Geom.right.Perm.Type = 'TurnBands'
BC_test.Geom.right.Perm.LambdaX = 50.
BC_test.Geom.right.Perm.LambdaY = 50.
BC_test.Geom.right.Perm.LambdaZ = 0.5
BC_test.Geom.right.Perm.GeomMean = 0.05

BC_test.Geom.right.Perm.Sigma = 0.5
BC_test.Geom.right.Perm.NumLines = 40
BC_test.Geom.right.Perm.RZeta = 5.0
BC_test.Geom.right.Perm.KMax = 100.0
BC_test.Geom.right.Perm.DelK = 0.2
BC_test.Geom.right.Perm.Seed = 13333
BC_test.Geom.right.Perm.LogNormal = 'Log'
BC_test.Geom.right.Perm.StratType = 'Bottom'

# hydraulic conductivity is very low, but not zero, top node will have to saturate
# before overland flow can begin and will be driven by hortonian flow
# comment out the left and right settings to make the subsurface heterogeneous using
# turning bands above.  Run time increases quite a bit with a heterogeneous
# subsurface
#

BC_test.Geom.left.Perm.Type = 'Constant'
BC_test.Geom.left.Perm.Value = 0.001

BC_test.Geom.right.Perm.Type = 'Constant'
BC_test.Geom.right.Perm.Value = 0.01

BC_test.Geom.channel.Perm.Type = 'Constant'
BC_test.Geom.channel.Perm.Value = 0.00001

BC_test.Perm.TensorType = 'TensorByGeom'

BC_test.Geom.Perm.TensorByGeom.Names = 'domain'

BC_test.Geom.domain.Perm.TensorValX = 1.0d0
BC_test.Geom.domain.Perm.TensorValY = 1.0d0
BC_test.Geom.domain.Perm.TensorValZ = 1.0d0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

BC_test.SpecificStorage.Type = 'Constant'
BC_test.SpecificStorage.GeomNames = 'domain'
BC_test.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

BC_test.Phase.Names = 'water'

BC_test.Phase.water.Density.Type = 'Constant'
BC_test.Phase.water.Density.Value = 1.0

BC_test.Phase.water.Viscosity.Type = 'Constant'
BC_test.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

BC_test.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

BC_test.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

BC_test.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

# run for 2 hours @ 6min timesteps
# 
BC_test.TimingInfo.BaseUnit = 0.1
BC_test.TimingInfo.StartCount = 0
BC_test.TimingInfo.StartTime = 0.0
BC_test.TimingInfo.StopTime = 0.3
BC_test.TimingInfo.DumpInterval = -1
BC_test.TimeStep.Type = 'Constant'
BC_test.TimeStep.Value = 0.1
#  
#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

BC_test.Geom.Porosity.GeomNames = 'left right channel'

BC_test.Geom.left.Porosity.Type = 'Constant'
BC_test.Geom.left.Porosity.Value = 0.25

BC_test.Geom.right.Porosity.Type = 'Constant'
BC_test.Geom.right.Porosity.Value = 0.25

BC_test.Geom.channel.Porosity.Type = 'Constant'
BC_test.Geom.channel.Porosity.Value = 0.01

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

BC_test.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

BC_test.Phase.RelPerm.Type = 'VanGenuchten'
BC_test.Phase.RelPerm.GeomNames = 'domain'

BC_test.Geom.domain.RelPerm.Alpha = 6.0
BC_test.Geom.domain.RelPerm.N = 2.

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

BC_test.Phase.Saturation.Type = 'VanGenuchten'
BC_test.Phase.Saturation.GeomNames = 'domain'

BC_test.Geom.domain.Saturation.Alpha = 6.0
BC_test.Geom.domain.Saturation.N = 2.
BC_test.Geom.domain.Saturation.SRes = 0.2
BC_test.Geom.domain.Saturation.SSat = 1.0



#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
BC_test.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
BC_test.Cycle.Names = 'constant rainrec'
BC_test.Cycle.constant.Names = 'alltime'
BC_test.Cycle.constant.alltime.Length = 1
BC_test.Cycle.constant.Repeat = -1

# rainfall and recession time periods are defined here
# rain for 1 hour, recession for 2 hours

BC_test.Cycle.rainrec.Names = 'rain rec'
BC_test.Cycle.rainrec.rain.Length = 1
BC_test.Cycle.rainrec.rec.Length = 2
BC_test.Cycle.rainrec.Repeat = -1
#  
#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
BC_test.BCPressure.PatchNames = [pfget Geom.domain.Patches]

BC_test.Patch.x_lower.BCPressure.Type = 'FluxConst'
BC_test.Patch.x_lower.BCPressure.Cycle = 'constant'
BC_test.Patch.x_lower.BCPressure.alltime.Value = 0.0

BC_test.Patch.y_lower.BCPressure.Type = 'FluxConst'
BC_test.Patch.y_lower.BCPressure.Cycle = 'constant'
BC_test.Patch.y_lower.BCPressure.alltime.Value = 0.0

BC_test.Patch.z_lower.BCPressure.Type = 'FluxConst'
BC_test.Patch.z_lower.BCPressure.Cycle = 'constant'
BC_test.Patch.z_lower.BCPressure.alltime.Value = 0.0

BC_test.Patch.x_upper.BCPressure.Type = 'FluxConst'
BC_test.Patch.x_upper.BCPressure.Cycle = 'constant'
BC_test.Patch.x_upper.BCPressure.alltime.Value = 0.0

BC_test.Patch.y_upper.BCPressure.Type = 'FluxConst'
BC_test.Patch.y_upper.BCPressure.Cycle = 'constant'
BC_test.Patch.y_upper.BCPressure.alltime.Value = 0.0

## overland flow boundary condition with very heavy rainfall then slight ET
BC_test.Patch.z_upper.BCPressure.Type = 'OverlandFlow'
BC_test.Patch.z_upper.BCPressure.Cycle = 'constant'
BC_test.Patch.z_upper.BCPressure.alltime.Value = -0.5
BC_test.Patch.z_upper.BCPressure.rec.Value = 0.000001

## overland flow boundary condition file read in test
BC_test.Patch.z_upper.BCPressure.Type = 'OverlandFlowPFB'
#pfset Patch.z-upper.BCPressure.Type		      FluxFile
BC_test.Patch.z_upper.BCPressure.Cycle = 'rainrec'
BC_test.Patch.z_upper.BCPressure.rain.FileName = 'bc.flux.test.1.pfb'
BC_test.Patch.z_upper.BCPressure.rec.FileName = 'bc.flux.test.0.pfb'

# load/setup flux files
file1 = [pfload -sa bc.flux.test.1.sa]
# pfsetgrid {30 30 30} {0.0 0.0 0.0} {10.0 10.0 0.05} $file1
# pfsave $file1 -pfb bc.flux.test.1.pfb
# pfsave $file1 -silo bc.flux.test.1.silo

file0 = [pfload -sa bc.flux.test.0.sa]
# pfsetgrid {30 30 30} {0.0 0.0 0.0} {10.0 10.0 0.05} $file0
# pfsave $file1 -pfb  bc.flux.test.0.pfb 
# pfsave $file1 -silo bc.flux.test.0.silo 

# pfdist "bc.flux.test.1.pfb"
# pfdist "bc.flux.test.0.pfb"

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

BC_test.TopoSlopesX.Type = 'Constant'
BC_test.TopoSlopesX.GeomNames = 'left right channel'
BC_test.TopoSlopesX.Geom.left.Value = -0.005
BC_test.TopoSlopesX.Geom.right.Value = 0.005
BC_test.TopoSlopesX.Geom.channel.Value = 0.00

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------


BC_test.TopoSlopesY.Type = 'Constant'
BC_test.TopoSlopesY.GeomNames = 'left right channel'
BC_test.TopoSlopesY.Geom.left.Value = 0.001
BC_test.TopoSlopesY.Geom.right.Value = 0.001
BC_test.TopoSlopesY.Geom.channel.Value = 0.001

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

BC_test.Mannings.Type = 'Constant'
BC_test.Mannings.GeomNames = 'left right channel'
BC_test.Mannings.Geom.left.Value = 5.e-6
BC_test.Mannings.Geom.right.Value = 5.e-6
BC_test.Mannings.Geom.channel.Value = 1.e-6

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

BC_test.PhaseSources.water.Type = 'Constant'
BC_test.PhaseSources.water.GeomNames = 'domain'
BC_test.PhaseSources.water.Geom.domain.Value = 0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

BC_test.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

BC_test.Solver = 'Richards'
BC_test.Solver.MaxIter = 2500

BC_test.Solver.Nonlinear.MaxIter = 300
BC_test.Solver.Nonlinear.ResidualTol = 1e-4
BC_test.Solver.Nonlinear.EtaChoice = 'Walker1'
BC_test.Solver.Nonlinear.EtaChoice = 'EtaConstant'
BC_test.Solver.Nonlinear.EtaValue = 0.001
BC_test.Solver.Nonlinear.UseJacobian = False
BC_test.Solver.Nonlinear.DerivativeEpsilon = 1e-16
BC_test.Solver.Nonlinear.StepTol = 1e-10
BC_test.Solver.Nonlinear.Globalization = 'LineSearch'
BC_test.Solver.Linear.KrylovDimension = 20
BC_test.Solver.Linear.MaxRestart = 2

BC_test.Solver.Linear.Preconditioner = 'MGSemi'
BC_test.Solver.Linear.Preconditioner.MGSemi.MaxIter = 1
BC_test.Solver.Linear.Preconditioner.MGSemi.MaxLevels = 10
BC_test.Solver.PrintSubsurf = False
BC_test. = 'Solver.Drop 1E_20'
BC_test.Solver.AbsTol = 1E-12
#  

BC_test.Solver.WriteSiloSubsurfData = True
BC_test.Solver.WriteSiloPressure = True
BC_test.Solver.WriteSiloSaturation = True

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

# set water table to be at the bottom of the domain, the top layer is initially dry
BC_test.ICPressure.Type = 'HydroStaticPatch'
BC_test.ICPressure.GeomNames = 'domain'
BC_test.Geom.domain.ICPressure.Value = -3.0

BC_test.Geom.domain.ICPressure.RefGeom = 'domain'
BC_test.Geom.domain.ICPressure.RefPatch = 'z_upper'

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

# pfrun default_over
# pfundist default_over

BC_test.run()
