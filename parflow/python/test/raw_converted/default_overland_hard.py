#  This runs the tilted-v catchment problem
#  similar to that in Kollet and Maxwell (2006) AWR

tcl_precision = 17

# set runname default_overland

#
# Import the ParFlow TCL package
#
from parflow import Run
default_overland_hard = Run("default_overland_hard", __file__)

default_overland_hard.FileVersion = 4

default_overland_hard.Process.Topology.P = 1
default_overland_hard.Process.Topology.Q = 1
default_overland_hard.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
default_overland_hard.ComputationalGrid.Lower.X = 0.0
default_overland_hard.ComputationalGrid.Lower.Y = 0.0
default_overland_hard.ComputationalGrid.Lower.Z = 0.0

default_overland_hard.ComputationalGrid.NX = 30
default_overland_hard.ComputationalGrid.NY = 30
default_overland_hard.ComputationalGrid.NZ = 30

default_overland_hard.ComputationalGrid.DX = 10.0
default_overland_hard.ComputationalGrid.DY = 10.0
default_overland_hard.ComputationalGrid.DZ = .05

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
default_overland_hard.GeomInput.Names = 'domaininput leftinput rightinput channelinput'

default_overland_hard.GeomInput.domaininput.GeomName = 'domain'
default_overland_hard.GeomInput.leftinput.GeomName = 'left'
default_overland_hard.GeomInput.rightinput.GeomName = 'right'
default_overland_hard.GeomInput.channelinput.GeomName = 'channel'

default_overland_hard.GeomInput.domaininput.InputType = 'Box'
default_overland_hard.GeomInput.leftinput.InputType = 'Box'
default_overland_hard.GeomInput.rightinput.InputType = 'Box'
default_overland_hard.GeomInput.channelinput.InputType = 'Box'

#---------------------------------------------------------
# Domain Geometry 
#---------------------------------------------------------
default_overland_hard.Geom.domain.Lower.X = 0.0
default_overland_hard.Geom.domain.Lower.Y = 0.0
default_overland_hard.Geom.domain.Lower.Z = 0.0
#  
default_overland_hard.Geom.domain.Upper.X = 300.0
default_overland_hard.Geom.domain.Upper.Y = 300.0
default_overland_hard.Geom.domain.Upper.Z = 1.5
default_overland_hard.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'

#---------------------------------------------------------
# Left Slope Geometry 
#---------------------------------------------------------
default_overland_hard.Geom.left.Lower.X = 0.0
default_overland_hard.Geom.left.Lower.Y = 0.0
default_overland_hard.Geom.left.Lower.Z = 0.0
#  
default_overland_hard.Geom.left.Upper.X = 140.0
default_overland_hard.Geom.left.Upper.Y = 300.0
default_overland_hard.Geom.left.Upper.Z = 1.5

#---------------------------------------------------------
# Right Slope Geometry 
#---------------------------------------------------------
default_overland_hard.Geom.right.Lower.X = 160.0
default_overland_hard.Geom.right.Lower.Y = 0.0
default_overland_hard.Geom.right.Lower.Z = 0.0
#  
default_overland_hard.Geom.right.Upper.X = 300.0
default_overland_hard.Geom.right.Upper.Y = 300.0
default_overland_hard.Geom.right.Upper.Z = 1.5

#---------------------------------------------------------
# Channel Geometry 
#---------------------------------------------------------
default_overland_hard.Geom.channel.Lower.X = 140.0
default_overland_hard.Geom.channel.Lower.Y = 0.0
default_overland_hard.Geom.channel.Lower.Z = 0.0
#  
default_overland_hard.Geom.channel.Upper.X = 160.0
default_overland_hard.Geom.channel.Upper.Y = 300.0
default_overland_hard.Geom.channel.Upper.Z = 1.5

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

default_overland_hard.Geom.Perm.Names = 'left right channel'

# Values in m/hour

# these are examples to make the upper portions of the v heterogeneous
# the following is ignored if the perm.type "Constant" settings are not
# commented out, below.

default_overland_hard.Geom.left.Perm.Type = 'TurnBands'
default_overland_hard.Geom.left.Perm.LambdaX = 50.
default_overland_hard.Geom.left.Perm.LambdaY = 50.
default_overland_hard.Geom.left.Perm.LambdaZ = 0.5
default_overland_hard.Geom.left.Perm.GeomMean = 0.01

default_overland_hard.Geom.left.Perm.Sigma = 0.5
default_overland_hard.Geom.left.Perm.NumLines = 40
default_overland_hard.Geom.left.Perm.RZeta = 5.0
default_overland_hard.Geom.left.Perm.KMax = 100.0
default_overland_hard.Geom.left.Perm.DelK = 0.2
default_overland_hard.Geom.left.Perm.Seed = 33333
default_overland_hard.Geom.left.Perm.LogNormal = 'Log'
default_overland_hard.Geom.left.Perm.StratType = 'Bottom'


default_overland_hard.Geom.right.Perm.Type = 'TurnBands'
default_overland_hard.Geom.right.Perm.LambdaX = 50.
default_overland_hard.Geom.right.Perm.LambdaY = 50.
default_overland_hard.Geom.right.Perm.LambdaZ = 0.5
default_overland_hard.Geom.right.Perm.GeomMean = 0.05

default_overland_hard.Geom.right.Perm.Sigma = 0.5
default_overland_hard.Geom.right.Perm.NumLines = 40
default_overland_hard.Geom.right.Perm.RZeta = 5.0
default_overland_hard.Geom.right.Perm.KMax = 100.0
default_overland_hard.Geom.right.Perm.DelK = 0.2
default_overland_hard.Geom.right.Perm.Seed = 13333
default_overland_hard.Geom.right.Perm.LogNormal = 'Log'
default_overland_hard.Geom.right.Perm.StratType = 'Bottom'

# hydraulic conductivity is very low, but not zero, top node will have to saturate
# before overland flow can begin and will be driven by hortonian flow
# comment out the left and right settings to make the subsurface heterogeneous using
# turning bands above.  Run time increases quite a bit with a heterogeneous
# subsurface
#

#pfset Geom.left.Perm.Type            Constant
default_overland_hard.Geom.left.Perm.Value = 0.001

#pfset Geom.right.Perm.Type            Constant
default_overland_hard.Geom.right.Perm.Value = 0.01

default_overland_hard.Geom.channel.Perm.Type = 'Constant'
default_overland_hard.Geom.channel.Perm.Value = 0.00001

default_overland_hard.Perm.TensorType = 'TensorByGeom'

default_overland_hard.Geom.Perm.TensorByGeom.Names = 'domain'

default_overland_hard.Geom.domain.Perm.TensorValX = 1.0d0
default_overland_hard.Geom.domain.Perm.TensorValY = 1.0d0
default_overland_hard.Geom.domain.Perm.TensorValZ = 1.0d0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

default_overland_hard.SpecificStorage.Type = 'Constant'
default_overland_hard.SpecificStorage.GeomNames = 'domain'
default_overland_hard.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

default_overland_hard.Phase.Names = 'water'

default_overland_hard.Phase.water.Density.Type = 'Constant'
default_overland_hard.Phase.water.Density.Value = 1.0

default_overland_hard.Phase.water.Viscosity.Type = 'Constant'
default_overland_hard.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

default_overland_hard.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

default_overland_hard.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

default_overland_hard.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

# 
default_overland_hard.TimingInfo.BaseUnit = 0.1
default_overland_hard.TimingInfo.StartCount = 0
default_overland_hard.TimingInfo.StartTime = 0.0
default_overland_hard.TimingInfo.StopTime = 1.0
default_overland_hard.TimingInfo.DumpInterval = -1
default_overland_hard.TimeStep.Type = 'Constant'
default_overland_hard.TimeStep.Value = 0.1
#  
#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

default_overland_hard.Geom.Porosity.GeomNames = 'left right channel'

default_overland_hard.Geom.left.Porosity.Type = 'Constant'
default_overland_hard.Geom.left.Porosity.Value = 0.25

default_overland_hard.Geom.right.Porosity.Type = 'Constant'
default_overland_hard.Geom.right.Porosity.Value = 0.25

default_overland_hard.Geom.channel.Porosity.Type = 'Constant'
default_overland_hard.Geom.channel.Porosity.Value = 0.01

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

default_overland_hard.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

default_overland_hard.Phase.RelPerm.Type = 'VanGenuchten'
default_overland_hard.Phase.RelPerm.GeomNames = 'domain'

default_overland_hard.Geom.domain.RelPerm.Alpha = 6.0
default_overland_hard.Geom.domain.RelPerm.N = 2.

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

default_overland_hard.Phase.Saturation.Type = 'VanGenuchten'
default_overland_hard.Phase.Saturation.GeomNames = 'domain'

default_overland_hard.Geom.domain.Saturation.Alpha = 6.0
default_overland_hard.Geom.domain.Saturation.N = 2.
default_overland_hard.Geom.domain.Saturation.SRes = 0.2
default_overland_hard.Geom.domain.Saturation.SSat = 1.0



#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
default_overland_hard.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
default_overland_hard.Cycle.Names = 'constant rainrec'
default_overland_hard.Cycle.constant.Names = 'alltime'
default_overland_hard.Cycle.constant.alltime.Length = 1
default_overland_hard.Cycle.constant.Repeat = -1

# rainfall and recession time periods are defined here
# rain for 1 hour, recession for 2 hours

default_overland_hard.Cycle.rainrec.Names = 'rain rec'
default_overland_hard.Cycle.rainrec.rain.Length = 10
default_overland_hard.Cycle.rainrec.rec.Length = 10
default_overland_hard.Cycle.rainrec.Repeat = -1
#  
#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
default_overland_hard.BCPressure.PatchNames = [pfget Geom.domain.Patches]

default_overland_hard.Patch.x_lower.BCPressure.Type = 'FluxConst'
default_overland_hard.Patch.x_lower.BCPressure.Cycle = 'constant'
default_overland_hard.Patch.x_lower.BCPressure.alltime.Value = 0.0

default_overland_hard.Patch.y_lower.BCPressure.Type = 'FluxConst'
default_overland_hard.Patch.y_lower.BCPressure.Cycle = 'constant'
default_overland_hard.Patch.y_lower.BCPressure.alltime.Value = 0.0

default_overland_hard.Patch.z_lower.BCPressure.Type = 'FluxConst'
default_overland_hard.Patch.z_lower.BCPressure.Cycle = 'constant'
default_overland_hard.Patch.z_lower.BCPressure.alltime.Value = 0.0

default_overland_hard.Patch.x_upper.BCPressure.Type = 'FluxConst'
default_overland_hard.Patch.x_upper.BCPressure.Cycle = 'constant'
default_overland_hard.Patch.x_upper.BCPressure.alltime.Value = 0.0

default_overland_hard.Patch.y_upper.BCPressure.Type = 'FluxConst'
default_overland_hard.Patch.y_upper.BCPressure.Cycle = 'constant'
default_overland_hard.Patch.y_upper.BCPressure.alltime.Value = 0.0

## overland flow boundary condition with very heavy rainfall then slight ET
default_overland_hard.Patch.z_upper.BCPressure.Type = 'OverlandFlow'
default_overland_hard.Patch.z_upper.BCPressure.Cycle = 'rainrec'
default_overland_hard.Patch.z_upper.BCPressure.rain.Value = -0.05
default_overland_hard.Patch.z_upper.BCPressure.rec.Value = 0.000001

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

default_overland_hard.TopoSlopesX.Type = 'Constant'
default_overland_hard.TopoSlopesX.GeomNames = 'left right channel'
default_overland_hard.TopoSlopesX.Geom.left.Value = -0.005
default_overland_hard.TopoSlopesX.Geom.right.Value = 0.005
default_overland_hard.TopoSlopesX.Geom.channel.Value = 0.00

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------


default_overland_hard.TopoSlopesY.Type = 'Constant'
default_overland_hard.TopoSlopesY.GeomNames = 'left right channel'
default_overland_hard.TopoSlopesY.Geom.left.Value = 0.001
default_overland_hard.TopoSlopesY.Geom.right.Value = 0.001
default_overland_hard.TopoSlopesY.Geom.channel.Value = 0.001

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

default_overland_hard.Mannings.Type = 'Constant'
default_overland_hard.Mannings.GeomNames = 'left right channel'
default_overland_hard.Mannings.Geom.left.Value = 5.e-6
default_overland_hard.Mannings.Geom.right.Value = 5.e-6
default_overland_hard.Mannings.Geom.channel.Value = 1.e-6

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

default_overland_hard.PhaseSources.water.Type = 'Constant'
default_overland_hard.PhaseSources.water.GeomNames = 'domain'
default_overland_hard.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

default_overland_hard.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

default_overland_hard.Solver = 'Richards'
default_overland_hard.Solver.MaxIter = 2500

default_overland_hard.Solver.Nonlinear.MaxIter = 20
default_overland_hard.Solver.Nonlinear.ResidualTol = 1e-9
default_overland_hard.Solver.Nonlinear.EtaChoice = 'EtaConstant'
default_overland_hard.Solver.Nonlinear.EtaValue = 0.01
default_overland_hard.Solver.Nonlinear.UseJacobian = False
default_overland_hard.Solver.Nonlinear.DerivativeEpsilon = 1e-8
default_overland_hard.Solver.Nonlinear.StepTol = 1e-20
default_overland_hard.Solver.Nonlinear.Globalization = 'LineSearch'
default_overland_hard.Solver.Linear.KrylovDimension = 20
default_overland_hard.Solver.Linear.MaxRestart = 2

default_overland_hard.Solver.Linear.Preconditioner = 'PFMG'
default_overland_hard.Solver.Linear.Preconditioner.MGSemi.MaxIter = 1
default_overland_hard.Solver.Linear.Preconditioner.MGSemi.MaxLevels = 10
default_overland_hard.Solver.PrintSubsurf = False
default_overland_hard. = 'Solver.Drop 1E_20'
default_overland_hard.Solver.AbsTol = 1E-9
#  
default_overland_hard.Solver.WriteSiloSubsurfData = True
default_overland_hard.Solver.WriteSiloPressure = True
default_overland_hard.Solver.WriteSiloSaturation = True
default_overland_hard.Solver.WriteSiloConcentration = True

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

# set water table to be at the bottom of the domain, the top layer is initially dry
default_overland_hard.ICPressure.Type = 'HydroStaticPatch'
default_overland_hard.ICPressure.GeomNames = 'domain'
default_overland_hard.Geom.domain.ICPressure.Value = -3.0

default_overland_hard.Geom.domain.ICPressure.RefGeom = 'domain'
default_overland_hard.Geom.domain.ICPressure.RefPatch = 'z_upper'

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

# pfwritedb $runname
# exit
# pfundist $runname

#
# Tests 
#
# source pftest.tcl
passed = 1

#
# SGS this test fails with 6 sigdigits
#
sig_digits = 5

# if ![pftestFile $runname.out.perm_x.pfb "Max difference in perm_x" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile $runname.out.perm_y.pfb "Max difference in perm_y" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile $runname.out.perm_z.pfb "Max difference in perm_z" $sig_digits] {
#     set passed 0
# }

# foreach i "00000 00001 00002 00003 00004" {
#     if ![pftestFile $runname.out.press.$i.pfb "Max difference in Pressure for timestep $i" $sig_digits] {
# 	set passed 0
#     }
#     if ![pftestFile $runname.out.satur.$i.pfb "Max difference in Saturation for timestep $i" $sig_digits] {
# 	set passed 0
#     }
# }


# if $passed {
#     puts "$runname : PASSED"
# } {
#     puts "$runname : FAILED"
# }
default_overland_hard.run()
