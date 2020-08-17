#  This runs the tilted-v catchment problem
#  similar to that in Kollet and Maxwell (2006) AWR

tcl_precision = 17

# set runname default_overland

#
# Import the ParFlow TCL package
#
from parflow import Run
default_overland.pfmg_octree.fulljac = Run("default_overland.pfmg_octree.fulljac", __file__)

default_overland.pfmg_octree.fulljac.FileVersion = 4

default_overland.pfmg_octree.fulljac.Process.Topology.P = [lindex $argv 0]
default_overland.pfmg_octree.fulljac.Process.Topology.Q = [lindex $argv 1]
default_overland.pfmg_octree.fulljac.Process.Topology.R = [lindex $argv 2]

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
default_overland.pfmg_octree.fulljac.ComputationalGrid.Lower.X = 0.0
default_overland.pfmg_octree.fulljac.ComputationalGrid.Lower.Y = 0.0
default_overland.pfmg_octree.fulljac.ComputationalGrid.Lower.Z = 0.0

default_overland.pfmg_octree.fulljac.ComputationalGrid.NX = 30
default_overland.pfmg_octree.fulljac.ComputationalGrid.NY = 30
default_overland.pfmg_octree.fulljac.ComputationalGrid.NZ = 30

default_overland.pfmg_octree.fulljac.ComputationalGrid.DX = 10.0
default_overland.pfmg_octree.fulljac.ComputationalGrid.DY = 10.0
default_overland.pfmg_octree.fulljac.ComputationalGrid.DZ = .05

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
default_overland.pfmg_octree.fulljac.GeomInput.Names = 'domaininput leftinput rightinput channelinput'

default_overland.pfmg_octree.fulljac.GeomInput.domaininput.GeomName = 'domain'
default_overland.pfmg_octree.fulljac.GeomInput.leftinput.GeomName = 'left'
default_overland.pfmg_octree.fulljac.GeomInput.rightinput.GeomName = 'right'
default_overland.pfmg_octree.fulljac.GeomInput.channelinput.GeomName = 'channel'

default_overland.pfmg_octree.fulljac.GeomInput.domaininput.InputType = 'Box'
default_overland.pfmg_octree.fulljac.GeomInput.leftinput.InputType = 'Box'
default_overland.pfmg_octree.fulljac.GeomInput.rightinput.InputType = 'Box'
default_overland.pfmg_octree.fulljac.GeomInput.channelinput.InputType = 'Box'

#---------------------------------------------------------
# Domain Geometry 
#---------------------------------------------------------
default_overland.pfmg_octree.fulljac.Geom.domain.Lower.X = 0.0
default_overland.pfmg_octree.fulljac.Geom.domain.Lower.Y = 0.0
default_overland.pfmg_octree.fulljac.Geom.domain.Lower.Z = 0.0
#  
default_overland.pfmg_octree.fulljac.Geom.domain.Upper.X = 300.0
default_overland.pfmg_octree.fulljac.Geom.domain.Upper.Y = 300.0
default_overland.pfmg_octree.fulljac.Geom.domain.Upper.Z = 1.5
default_overland.pfmg_octree.fulljac.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'

#---------------------------------------------------------
# Left Slope Geometry 
#---------------------------------------------------------
default_overland.pfmg_octree.fulljac.Geom.left.Lower.X = 0.0
default_overland.pfmg_octree.fulljac.Geom.left.Lower.Y = 0.0
default_overland.pfmg_octree.fulljac.Geom.left.Lower.Z = 0.0
#  
default_overland.pfmg_octree.fulljac.Geom.left.Upper.X = 140.0
default_overland.pfmg_octree.fulljac.Geom.left.Upper.Y = 300.0
default_overland.pfmg_octree.fulljac.Geom.left.Upper.Z = 1.5

#---------------------------------------------------------
# Right Slope Geometry 
#---------------------------------------------------------
default_overland.pfmg_octree.fulljac.Geom.right.Lower.X = 160.0
default_overland.pfmg_octree.fulljac.Geom.right.Lower.Y = 0.0
default_overland.pfmg_octree.fulljac.Geom.right.Lower.Z = 0.0
#  
default_overland.pfmg_octree.fulljac.Geom.right.Upper.X = 300.0
default_overland.pfmg_octree.fulljac.Geom.right.Upper.Y = 300.0
default_overland.pfmg_octree.fulljac.Geom.right.Upper.Z = 1.5

#---------------------------------------------------------
# Channel Geometry 
#---------------------------------------------------------
default_overland.pfmg_octree.fulljac.Geom.channel.Lower.X = 140.0
default_overland.pfmg_octree.fulljac.Geom.channel.Lower.Y = 0.0
default_overland.pfmg_octree.fulljac.Geom.channel.Lower.Z = 0.0
#  
default_overland.pfmg_octree.fulljac.Geom.channel.Upper.X = 160.0
default_overland.pfmg_octree.fulljac.Geom.channel.Upper.Y = 300.0
default_overland.pfmg_octree.fulljac.Geom.channel.Upper.Z = 1.5

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.Geom.Perm.Names = 'left right channel'

# Values in m/hour

# these are examples to make the upper portions of the v heterogeneous
# the following is ignored if the perm.type "Constant" settings are not
# commented out, below.

default_overland.pfmg_octree.fulljac.Geom.left.Perm.Type = 'TurnBands'
default_overland.pfmg_octree.fulljac.Geom.left.Perm.LambdaX = 50.
default_overland.pfmg_octree.fulljac.Geom.left.Perm.LambdaY = 50.
default_overland.pfmg_octree.fulljac.Geom.left.Perm.LambdaZ = 0.5
default_overland.pfmg_octree.fulljac.Geom.left.Perm.GeomMean = 0.01

default_overland.pfmg_octree.fulljac.Geom.left.Perm.Sigma = 0.5
default_overland.pfmg_octree.fulljac.Geom.left.Perm.NumLines = 40
default_overland.pfmg_octree.fulljac.Geom.left.Perm.RZeta = 5.0
default_overland.pfmg_octree.fulljac.Geom.left.Perm.KMax = 100.0
default_overland.pfmg_octree.fulljac.Geom.left.Perm.DelK = 0.2
default_overland.pfmg_octree.fulljac.Geom.left.Perm.Seed = 33333
default_overland.pfmg_octree.fulljac.Geom.left.Perm.LogNormal = 'Log'
default_overland.pfmg_octree.fulljac.Geom.left.Perm.StratType = 'Bottom'


default_overland.pfmg_octree.fulljac.Geom.right.Perm.Type = 'TurnBands'
default_overland.pfmg_octree.fulljac.Geom.right.Perm.LambdaX = 50.
default_overland.pfmg_octree.fulljac.Geom.right.Perm.LambdaY = 50.
default_overland.pfmg_octree.fulljac.Geom.right.Perm.LambdaZ = 0.5
default_overland.pfmg_octree.fulljac.Geom.right.Perm.GeomMean = 0.05

default_overland.pfmg_octree.fulljac.Geom.right.Perm.Sigma = 0.5
default_overland.pfmg_octree.fulljac.Geom.right.Perm.NumLines = 40
default_overland.pfmg_octree.fulljac.Geom.right.Perm.RZeta = 5.0
default_overland.pfmg_octree.fulljac.Geom.right.Perm.KMax = 100.0
default_overland.pfmg_octree.fulljac.Geom.right.Perm.DelK = 0.2
default_overland.pfmg_octree.fulljac.Geom.right.Perm.Seed = 13333
default_overland.pfmg_octree.fulljac.Geom.right.Perm.LogNormal = 'Log'
default_overland.pfmg_octree.fulljac.Geom.right.Perm.StratType = 'Bottom'

# hydraulic conductivity is very low, but not zero, top node will have to saturate
# before overland flow can begin and will be driven by hortonian flow
# comment out the left and right settings to make the subsurface heterogeneous using
# turning bands above.  Run time increases quite a bit with a heterogeneous
# subsurface
#

default_overland.pfmg_octree.fulljac.Geom.left.Perm.Type = 'Constant'
default_overland.pfmg_octree.fulljac.Geom.left.Perm.Value = 0.001

default_overland.pfmg_octree.fulljac.Geom.right.Perm.Type = 'Constant'
default_overland.pfmg_octree.fulljac.Geom.right.Perm.Value = 0.01

default_overland.pfmg_octree.fulljac.Geom.channel.Perm.Type = 'Constant'
default_overland.pfmg_octree.fulljac.Geom.channel.Perm.Value = 0.00001

default_overland.pfmg_octree.fulljac.Perm.TensorType = 'TensorByGeom'

default_overland.pfmg_octree.fulljac.Geom.Perm.TensorByGeom.Names = 'domain'

default_overland.pfmg_octree.fulljac.Geom.domain.Perm.TensorValX = 1.0d0
default_overland.pfmg_octree.fulljac.Geom.domain.Perm.TensorValY = 1.0d0
default_overland.pfmg_octree.fulljac.Geom.domain.Perm.TensorValZ = 1.0d0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.SpecificStorage.Type = 'Constant'
default_overland.pfmg_octree.fulljac.SpecificStorage.GeomNames = 'domain'
default_overland.pfmg_octree.fulljac.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.Phase.Names = 'water'

default_overland.pfmg_octree.fulljac.Phase.water.Density.Type = 'Constant'
default_overland.pfmg_octree.fulljac.Phase.water.Density.Value = 1.0

default_overland.pfmg_octree.fulljac.Phase.water.Viscosity.Type = 'Constant'
default_overland.pfmg_octree.fulljac.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

# 
default_overland.pfmg_octree.fulljac.TimingInfo.BaseUnit = 0.1
default_overland.pfmg_octree.fulljac.TimingInfo.StartCount = 0
default_overland.pfmg_octree.fulljac.TimingInfo.StartTime = 0.0
default_overland.pfmg_octree.fulljac.TimingInfo.StopTime = 0.4
default_overland.pfmg_octree.fulljac.TimingInfo.DumpInterval = -1
default_overland.pfmg_octree.fulljac.TimeStep.Type = 'Constant'
default_overland.pfmg_octree.fulljac.TimeStep.Value = 0.1
#  
#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.Geom.Porosity.GeomNames = 'left right channel'

default_overland.pfmg_octree.fulljac.Geom.left.Porosity.Type = 'Constant'
default_overland.pfmg_octree.fulljac.Geom.left.Porosity.Value = 0.25

default_overland.pfmg_octree.fulljac.Geom.right.Porosity.Type = 'Constant'
default_overland.pfmg_octree.fulljac.Geom.right.Porosity.Value = 0.25

default_overland.pfmg_octree.fulljac.Geom.channel.Porosity.Type = 'Constant'
default_overland.pfmg_octree.fulljac.Geom.channel.Porosity.Value = 0.01

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.Phase.RelPerm.Type = 'VanGenuchten'
default_overland.pfmg_octree.fulljac.Phase.RelPerm.GeomNames = 'domain'

default_overland.pfmg_octree.fulljac.Geom.domain.RelPerm.Alpha = 6.0
default_overland.pfmg_octree.fulljac.Geom.domain.RelPerm.N = 2.

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

default_overland.pfmg_octree.fulljac.Phase.Saturation.Type = 'VanGenuchten'
default_overland.pfmg_octree.fulljac.Phase.Saturation.GeomNames = 'domain'

default_overland.pfmg_octree.fulljac.Geom.domain.Saturation.Alpha = 6.0
default_overland.pfmg_octree.fulljac.Geom.domain.Saturation.N = 2.
default_overland.pfmg_octree.fulljac.Geom.domain.Saturation.SRes = 0.2
default_overland.pfmg_octree.fulljac.Geom.domain.Saturation.SSat = 1.0



#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
default_overland.pfmg_octree.fulljac.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
default_overland.pfmg_octree.fulljac.Cycle.Names = 'constant rainrec'
default_overland.pfmg_octree.fulljac.Cycle.constant.Names = 'alltime'
default_overland.pfmg_octree.fulljac.Cycle.constant.alltime.Length = 1
default_overland.pfmg_octree.fulljac.Cycle.constant.Repeat = -1

# rainfall and recession time periods are defined here
# rain for 1 hour, recession for 2 hours

default_overland.pfmg_octree.fulljac.Cycle.rainrec.Names = 'rain rec'
default_overland.pfmg_octree.fulljac.Cycle.rainrec.rain.Length = 1
default_overland.pfmg_octree.fulljac.Cycle.rainrec.rec.Length = 2
default_overland.pfmg_octree.fulljac.Cycle.rainrec.Repeat = -1
#  
#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
default_overland.pfmg_octree.fulljac.BCPressure.PatchNames = [pfget Geom.domain.Patches]

default_overland.pfmg_octree.fulljac.Patch.x_lower.BCPressure.Type = 'FluxConst'
default_overland.pfmg_octree.fulljac.Patch.x_lower.BCPressure.Cycle = 'constant'
default_overland.pfmg_octree.fulljac.Patch.x_lower.BCPressure.alltime.Value = 0.0

default_overland.pfmg_octree.fulljac.Patch.y_lower.BCPressure.Type = 'FluxConst'
default_overland.pfmg_octree.fulljac.Patch.y_lower.BCPressure.Cycle = 'constant'
default_overland.pfmg_octree.fulljac.Patch.y_lower.BCPressure.alltime.Value = 0.0

default_overland.pfmg_octree.fulljac.Patch.z_lower.BCPressure.Type = 'FluxConst'
default_overland.pfmg_octree.fulljac.Patch.z_lower.BCPressure.Cycle = 'constant'
default_overland.pfmg_octree.fulljac.Patch.z_lower.BCPressure.alltime.Value = 0.0

default_overland.pfmg_octree.fulljac.Patch.x_upper.BCPressure.Type = 'FluxConst'
default_overland.pfmg_octree.fulljac.Patch.x_upper.BCPressure.Cycle = 'constant'
default_overland.pfmg_octree.fulljac.Patch.x_upper.BCPressure.alltime.Value = 0.0

default_overland.pfmg_octree.fulljac.Patch.y_upper.BCPressure.Type = 'FluxConst'
default_overland.pfmg_octree.fulljac.Patch.y_upper.BCPressure.Cycle = 'constant'
default_overland.pfmg_octree.fulljac.Patch.y_upper.BCPressure.alltime.Value = 0.0

## overland flow boundary condition with very heavy rainfall then slight ET
default_overland.pfmg_octree.fulljac.Patch.z_upper.BCPressure.Type = 'OverlandFlow'
default_overland.pfmg_octree.fulljac.Patch.z_upper.BCPressure.Cycle = 'rainrec'
default_overland.pfmg_octree.fulljac.Patch.z_upper.BCPressure.rain.Value = -0.05
default_overland.pfmg_octree.fulljac.Patch.z_upper.BCPressure.rec.Value = 0.000001

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

default_overland.pfmg_octree.fulljac.TopoSlopesX.Type = 'Constant'
default_overland.pfmg_octree.fulljac.TopoSlopesX.GeomNames = 'left right channel'
default_overland.pfmg_octree.fulljac.TopoSlopesX.Geom.left.Value = -0.005
default_overland.pfmg_octree.fulljac.TopoSlopesX.Geom.right.Value = 0.005
default_overland.pfmg_octree.fulljac.TopoSlopesX.Geom.channel.Value = 0.00

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------


default_overland.pfmg_octree.fulljac.TopoSlopesY.Type = 'Constant'
default_overland.pfmg_octree.fulljac.TopoSlopesY.GeomNames = 'left right channel'
default_overland.pfmg_octree.fulljac.TopoSlopesY.Geom.left.Value = 0.001
default_overland.pfmg_octree.fulljac.TopoSlopesY.Geom.right.Value = 0.001
default_overland.pfmg_octree.fulljac.TopoSlopesY.Geom.channel.Value = 0.001

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

default_overland.pfmg_octree.fulljac.Mannings.Type = 'Constant'
default_overland.pfmg_octree.fulljac.Mannings.GeomNames = 'left right channel'
default_overland.pfmg_octree.fulljac.Mannings.Geom.left.Value = 5.e-6
default_overland.pfmg_octree.fulljac.Mannings.Geom.right.Value = 5.e-6
default_overland.pfmg_octree.fulljac.Mannings.Geom.channel.Value = 1.e-6

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.PhaseSources.water.Type = 'Constant'
default_overland.pfmg_octree.fulljac.PhaseSources.water.GeomNames = 'domain'
default_overland.pfmg_octree.fulljac.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.fulljac.Solver = 'Richards'
default_overland.pfmg_octree.fulljac.Solver.MaxIter = 2500

default_overland.pfmg_octree.fulljac.Solver.Nonlinear.MaxIter = 20
default_overland.pfmg_octree.fulljac.Solver.Nonlinear.ResidualTol = 1e-9
default_overland.pfmg_octree.fulljac.Solver.Nonlinear.EtaChoice = 'EtaConstant'
default_overland.pfmg_octree.fulljac.Solver.Nonlinear.EtaValue = 0.01
default_overland.pfmg_octree.fulljac.Solver.Nonlinear.UseJacobian = True
default_overland.pfmg_octree.fulljac.Solver.Nonlinear.DerivativeEpsilon = 1e-8
default_overland.pfmg_octree.fulljac.Solver.Nonlinear.StepTol = 1e-20
default_overland.pfmg_octree.fulljac.Solver.Nonlinear.Globalization = 'LineSearch'
default_overland.pfmg_octree.fulljac.Solver.Linear.KrylovDimension = 20
default_overland.pfmg_octree.fulljac.Solver.Linear.MaxRestart = 2

default_overland.pfmg_octree.fulljac.Solver.Linear.Preconditioner = 'PFMGOctree'
default_overland.pfmg_octree.fulljac.Solver.Linear.Preconditioner.PCMatrixType = 'FullJacobian'
default_overland.pfmg_octree.fulljac.Solver.PrintSubsurf = False
default_overland.pfmg_octree.fulljac. = 'Solver.Drop 1E_20'
default_overland.pfmg_octree.fulljac.Solver.AbsTol = 1E-9
#  
default_overland.pfmg_octree.fulljac.Solver.WriteSiloSubsurfData = True
default_overland.pfmg_octree.fulljac.Solver.WriteSiloPressure = True
default_overland.pfmg_octree.fulljac.Solver.WriteSiloSaturation = True
default_overland.pfmg_octree.fulljac.Solver.WriteSiloConcentration = True

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

# set water table to be at the bottom of the domain, the top layer is initially dry
default_overland.pfmg_octree.fulljac.ICPressure.Type = 'HydroStaticPatch'
default_overland.pfmg_octree.fulljac.ICPressure.GeomNames = 'domain'
default_overland.pfmg_octree.fulljac.Geom.domain.ICPressure.Value = -3.0

default_overland.pfmg_octree.fulljac.Geom.domain.ICPressure.RefGeom = 'domain'
default_overland.pfmg_octree.fulljac.Geom.domain.ICPressure.RefPatch = 'z_upper'

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

# pfrun $runname
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
default_overland.pfmg_octree.fulljac.run()
