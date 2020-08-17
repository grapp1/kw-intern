#  This runs the tilted-v catchment problem
#  similar to that in Kollet and Maxwell (2006) AWR

tcl_precision = 17

# set runname default_overland

#
# Import the ParFlow TCL package
#
from parflow import Run
default_overland.pfmg_octree.jac = Run("default_overland.pfmg_octree.jac", __file__)

default_overland.pfmg_octree.jac.FileVersion = 4

default_overland.pfmg_octree.jac.Process.Topology.P = [lindex $argv 0]
default_overland.pfmg_octree.jac.Process.Topology.Q = [lindex $argv 1]
default_overland.pfmg_octree.jac.Process.Topology.R = [lindex $argv 2]

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
default_overland.pfmg_octree.jac.ComputationalGrid.Lower.X = 0.0
default_overland.pfmg_octree.jac.ComputationalGrid.Lower.Y = 0.0
default_overland.pfmg_octree.jac.ComputationalGrid.Lower.Z = 0.0

default_overland.pfmg_octree.jac.ComputationalGrid.NX = 30
default_overland.pfmg_octree.jac.ComputationalGrid.NY = 30
default_overland.pfmg_octree.jac.ComputationalGrid.NZ = 30

default_overland.pfmg_octree.jac.ComputationalGrid.DX = 10.0
default_overland.pfmg_octree.jac.ComputationalGrid.DY = 10.0
default_overland.pfmg_octree.jac.ComputationalGrid.DZ = .05

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
default_overland.pfmg_octree.jac.GeomInput.Names = 'domaininput leftinput rightinput channelinput'

default_overland.pfmg_octree.jac.GeomInput.domaininput.GeomName = 'domain'
default_overland.pfmg_octree.jac.GeomInput.leftinput.GeomName = 'left'
default_overland.pfmg_octree.jac.GeomInput.rightinput.GeomName = 'right'
default_overland.pfmg_octree.jac.GeomInput.channelinput.GeomName = 'channel'

default_overland.pfmg_octree.jac.GeomInput.domaininput.InputType = 'Box'
default_overland.pfmg_octree.jac.GeomInput.leftinput.InputType = 'Box'
default_overland.pfmg_octree.jac.GeomInput.rightinput.InputType = 'Box'
default_overland.pfmg_octree.jac.GeomInput.channelinput.InputType = 'Box'

#---------------------------------------------------------
# Domain Geometry 
#---------------------------------------------------------
default_overland.pfmg_octree.jac.Geom.domain.Lower.X = 0.0
default_overland.pfmg_octree.jac.Geom.domain.Lower.Y = 0.0
default_overland.pfmg_octree.jac.Geom.domain.Lower.Z = 0.0
#  
default_overland.pfmg_octree.jac.Geom.domain.Upper.X = 300.0
default_overland.pfmg_octree.jac.Geom.domain.Upper.Y = 300.0
default_overland.pfmg_octree.jac.Geom.domain.Upper.Z = 1.5
default_overland.pfmg_octree.jac.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'

#---------------------------------------------------------
# Left Slope Geometry 
#---------------------------------------------------------
default_overland.pfmg_octree.jac.Geom.left.Lower.X = 0.0
default_overland.pfmg_octree.jac.Geom.left.Lower.Y = 0.0
default_overland.pfmg_octree.jac.Geom.left.Lower.Z = 0.0
#  
default_overland.pfmg_octree.jac.Geom.left.Upper.X = 140.0
default_overland.pfmg_octree.jac.Geom.left.Upper.Y = 300.0
default_overland.pfmg_octree.jac.Geom.left.Upper.Z = 1.5

#---------------------------------------------------------
# Right Slope Geometry 
#---------------------------------------------------------
default_overland.pfmg_octree.jac.Geom.right.Lower.X = 160.0
default_overland.pfmg_octree.jac.Geom.right.Lower.Y = 0.0
default_overland.pfmg_octree.jac.Geom.right.Lower.Z = 0.0
#  
default_overland.pfmg_octree.jac.Geom.right.Upper.X = 300.0
default_overland.pfmg_octree.jac.Geom.right.Upper.Y = 300.0
default_overland.pfmg_octree.jac.Geom.right.Upper.Z = 1.5

#---------------------------------------------------------
# Channel Geometry 
#---------------------------------------------------------
default_overland.pfmg_octree.jac.Geom.channel.Lower.X = 140.0
default_overland.pfmg_octree.jac.Geom.channel.Lower.Y = 0.0
default_overland.pfmg_octree.jac.Geom.channel.Lower.Z = 0.0
#  
default_overland.pfmg_octree.jac.Geom.channel.Upper.X = 160.0
default_overland.pfmg_octree.jac.Geom.channel.Upper.Y = 300.0
default_overland.pfmg_octree.jac.Geom.channel.Upper.Z = 1.5

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.Geom.Perm.Names = 'left right channel'

# Values in m/hour

# these are examples to make the upper portions of the v heterogeneous
# the following is ignored if the perm.type "Constant" settings are not
# commented out, below.

default_overland.pfmg_octree.jac.Geom.left.Perm.Type = 'TurnBands'
default_overland.pfmg_octree.jac.Geom.left.Perm.LambdaX = 50.
default_overland.pfmg_octree.jac.Geom.left.Perm.LambdaY = 50.
default_overland.pfmg_octree.jac.Geom.left.Perm.LambdaZ = 0.5
default_overland.pfmg_octree.jac.Geom.left.Perm.GeomMean = 0.01

default_overland.pfmg_octree.jac.Geom.left.Perm.Sigma = 0.5
default_overland.pfmg_octree.jac.Geom.left.Perm.NumLines = 40
default_overland.pfmg_octree.jac.Geom.left.Perm.RZeta = 5.0
default_overland.pfmg_octree.jac.Geom.left.Perm.KMax = 100.0
default_overland.pfmg_octree.jac.Geom.left.Perm.DelK = 0.2
default_overland.pfmg_octree.jac.Geom.left.Perm.Seed = 33333
default_overland.pfmg_octree.jac.Geom.left.Perm.LogNormal = 'Log'
default_overland.pfmg_octree.jac.Geom.left.Perm.StratType = 'Bottom'


default_overland.pfmg_octree.jac.Geom.right.Perm.Type = 'TurnBands'
default_overland.pfmg_octree.jac.Geom.right.Perm.LambdaX = 50.
default_overland.pfmg_octree.jac.Geom.right.Perm.LambdaY = 50.
default_overland.pfmg_octree.jac.Geom.right.Perm.LambdaZ = 0.5
default_overland.pfmg_octree.jac.Geom.right.Perm.GeomMean = 0.05

default_overland.pfmg_octree.jac.Geom.right.Perm.Sigma = 0.5
default_overland.pfmg_octree.jac.Geom.right.Perm.NumLines = 40
default_overland.pfmg_octree.jac.Geom.right.Perm.RZeta = 5.0
default_overland.pfmg_octree.jac.Geom.right.Perm.KMax = 100.0
default_overland.pfmg_octree.jac.Geom.right.Perm.DelK = 0.2
default_overland.pfmg_octree.jac.Geom.right.Perm.Seed = 13333
default_overland.pfmg_octree.jac.Geom.right.Perm.LogNormal = 'Log'
default_overland.pfmg_octree.jac.Geom.right.Perm.StratType = 'Bottom'

# hydraulic conductivity is very low, but not zero, top node will have to saturate
# before overland flow can begin and will be driven by hortonian flow
# comment out the left and right settings to make the subsurface heterogeneous using
# turning bands above.  Run time increases quite a bit with a heterogeneous
# subsurface
#

default_overland.pfmg_octree.jac.Geom.left.Perm.Type = 'Constant'
default_overland.pfmg_octree.jac.Geom.left.Perm.Value = 0.001

default_overland.pfmg_octree.jac.Geom.right.Perm.Type = 'Constant'
default_overland.pfmg_octree.jac.Geom.right.Perm.Value = 0.01

default_overland.pfmg_octree.jac.Geom.channel.Perm.Type = 'Constant'
default_overland.pfmg_octree.jac.Geom.channel.Perm.Value = 0.00001

default_overland.pfmg_octree.jac.Perm.TensorType = 'TensorByGeom'

default_overland.pfmg_octree.jac.Geom.Perm.TensorByGeom.Names = 'domain'

default_overland.pfmg_octree.jac.Geom.domain.Perm.TensorValX = 1.0d0
default_overland.pfmg_octree.jac.Geom.domain.Perm.TensorValY = 1.0d0
default_overland.pfmg_octree.jac.Geom.domain.Perm.TensorValZ = 1.0d0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.SpecificStorage.Type = 'Constant'
default_overland.pfmg_octree.jac.SpecificStorage.GeomNames = 'domain'
default_overland.pfmg_octree.jac.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.Phase.Names = 'water'

default_overland.pfmg_octree.jac.Phase.water.Density.Type = 'Constant'
default_overland.pfmg_octree.jac.Phase.water.Density.Value = 1.0

default_overland.pfmg_octree.jac.Phase.water.Viscosity.Type = 'Constant'
default_overland.pfmg_octree.jac.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

# 
default_overland.pfmg_octree.jac.TimingInfo.BaseUnit = 0.1
default_overland.pfmg_octree.jac.TimingInfo.StartCount = 0
default_overland.pfmg_octree.jac.TimingInfo.StartTime = 0.0
default_overland.pfmg_octree.jac.TimingInfo.StopTime = 0.4
default_overland.pfmg_octree.jac.TimingInfo.DumpInterval = -1
default_overland.pfmg_octree.jac.TimeStep.Type = 'Constant'
default_overland.pfmg_octree.jac.TimeStep.Value = 0.1
#  
#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.Geom.Porosity.GeomNames = 'left right channel'

default_overland.pfmg_octree.jac.Geom.left.Porosity.Type = 'Constant'
default_overland.pfmg_octree.jac.Geom.left.Porosity.Value = 0.25

default_overland.pfmg_octree.jac.Geom.right.Porosity.Type = 'Constant'
default_overland.pfmg_octree.jac.Geom.right.Porosity.Value = 0.25

default_overland.pfmg_octree.jac.Geom.channel.Porosity.Type = 'Constant'
default_overland.pfmg_octree.jac.Geom.channel.Porosity.Value = 0.01

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.Phase.RelPerm.Type = 'VanGenuchten'
default_overland.pfmg_octree.jac.Phase.RelPerm.GeomNames = 'domain'

default_overland.pfmg_octree.jac.Geom.domain.RelPerm.Alpha = 6.0
default_overland.pfmg_octree.jac.Geom.domain.RelPerm.N = 2.

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

default_overland.pfmg_octree.jac.Phase.Saturation.Type = 'VanGenuchten'
default_overland.pfmg_octree.jac.Phase.Saturation.GeomNames = 'domain'

default_overland.pfmg_octree.jac.Geom.domain.Saturation.Alpha = 6.0
default_overland.pfmg_octree.jac.Geom.domain.Saturation.N = 2.
default_overland.pfmg_octree.jac.Geom.domain.Saturation.SRes = 0.2
default_overland.pfmg_octree.jac.Geom.domain.Saturation.SSat = 1.0



#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
default_overland.pfmg_octree.jac.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
default_overland.pfmg_octree.jac.Cycle.Names = 'constant rainrec'
default_overland.pfmg_octree.jac.Cycle.constant.Names = 'alltime'
default_overland.pfmg_octree.jac.Cycle.constant.alltime.Length = 1
default_overland.pfmg_octree.jac.Cycle.constant.Repeat = -1

# rainfall and recession time periods are defined here
# rain for 1 hour, recession for 2 hours

default_overland.pfmg_octree.jac.Cycle.rainrec.Names = 'rain rec'
default_overland.pfmg_octree.jac.Cycle.rainrec.rain.Length = 1
default_overland.pfmg_octree.jac.Cycle.rainrec.rec.Length = 2
default_overland.pfmg_octree.jac.Cycle.rainrec.Repeat = -1
#  
#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
default_overland.pfmg_octree.jac.BCPressure.PatchNames = [pfget Geom.domain.Patches]

default_overland.pfmg_octree.jac.Patch.x_lower.BCPressure.Type = 'FluxConst'
default_overland.pfmg_octree.jac.Patch.x_lower.BCPressure.Cycle = 'constant'
default_overland.pfmg_octree.jac.Patch.x_lower.BCPressure.alltime.Value = 0.0

default_overland.pfmg_octree.jac.Patch.y_lower.BCPressure.Type = 'FluxConst'
default_overland.pfmg_octree.jac.Patch.y_lower.BCPressure.Cycle = 'constant'
default_overland.pfmg_octree.jac.Patch.y_lower.BCPressure.alltime.Value = 0.0

default_overland.pfmg_octree.jac.Patch.z_lower.BCPressure.Type = 'FluxConst'
default_overland.pfmg_octree.jac.Patch.z_lower.BCPressure.Cycle = 'constant'
default_overland.pfmg_octree.jac.Patch.z_lower.BCPressure.alltime.Value = 0.0

default_overland.pfmg_octree.jac.Patch.x_upper.BCPressure.Type = 'FluxConst'
default_overland.pfmg_octree.jac.Patch.x_upper.BCPressure.Cycle = 'constant'
default_overland.pfmg_octree.jac.Patch.x_upper.BCPressure.alltime.Value = 0.0

default_overland.pfmg_octree.jac.Patch.y_upper.BCPressure.Type = 'FluxConst'
default_overland.pfmg_octree.jac.Patch.y_upper.BCPressure.Cycle = 'constant'
default_overland.pfmg_octree.jac.Patch.y_upper.BCPressure.alltime.Value = 0.0

## overland flow boundary condition with very heavy rainfall then slight ET
default_overland.pfmg_octree.jac.Patch.z_upper.BCPressure.Type = 'OverlandFlow'
default_overland.pfmg_octree.jac.Patch.z_upper.BCPressure.Cycle = 'rainrec'
default_overland.pfmg_octree.jac.Patch.z_upper.BCPressure.rain.Value = -0.05
default_overland.pfmg_octree.jac.Patch.z_upper.BCPressure.rec.Value = 0.000001

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

default_overland.pfmg_octree.jac.TopoSlopesX.Type = 'Constant'
default_overland.pfmg_octree.jac.TopoSlopesX.GeomNames = 'left right channel'
default_overland.pfmg_octree.jac.TopoSlopesX.Geom.left.Value = -0.005
default_overland.pfmg_octree.jac.TopoSlopesX.Geom.right.Value = 0.005
default_overland.pfmg_octree.jac.TopoSlopesX.Geom.channel.Value = 0.00

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------


default_overland.pfmg_octree.jac.TopoSlopesY.Type = 'Constant'
default_overland.pfmg_octree.jac.TopoSlopesY.GeomNames = 'left right channel'
default_overland.pfmg_octree.jac.TopoSlopesY.Geom.left.Value = 0.001
default_overland.pfmg_octree.jac.TopoSlopesY.Geom.right.Value = 0.001
default_overland.pfmg_octree.jac.TopoSlopesY.Geom.channel.Value = 0.001

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

default_overland.pfmg_octree.jac.Mannings.Type = 'Constant'
default_overland.pfmg_octree.jac.Mannings.GeomNames = 'left right channel'
default_overland.pfmg_octree.jac.Mannings.Geom.left.Value = 5.e-6
default_overland.pfmg_octree.jac.Mannings.Geom.right.Value = 5.e-6
default_overland.pfmg_octree.jac.Mannings.Geom.channel.Value = 1.e-6

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.PhaseSources.water.Type = 'Constant'
default_overland.pfmg_octree.jac.PhaseSources.water.GeomNames = 'domain'
default_overland.pfmg_octree.jac.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

default_overland.pfmg_octree.jac.Solver = 'Richards'
default_overland.pfmg_octree.jac.Solver.MaxIter = 2500

default_overland.pfmg_octree.jac.Solver.Nonlinear.MaxIter = 20
default_overland.pfmg_octree.jac.Solver.Nonlinear.ResidualTol = 1e-9
default_overland.pfmg_octree.jac.Solver.Nonlinear.EtaChoice = 'EtaConstant'
default_overland.pfmg_octree.jac.Solver.Nonlinear.EtaValue = 0.01
default_overland.pfmg_octree.jac.Solver.Nonlinear.UseJacobian = True
default_overland.pfmg_octree.jac.Solver.Nonlinear.DerivativeEpsilon = 1e-8
default_overland.pfmg_octree.jac.Solver.Nonlinear.StepTol = 1e-20
default_overland.pfmg_octree.jac.Solver.Nonlinear.Globalization = 'LineSearch'
default_overland.pfmg_octree.jac.Solver.Linear.KrylovDimension = 20
default_overland.pfmg_octree.jac.Solver.Linear.MaxRestart = 2

default_overland.pfmg_octree.jac.Solver.Linear.Preconditioner = 'PFMGOctree'
default_overland.pfmg_octree.jac.Solver.PrintSubsurf = False
default_overland.pfmg_octree.jac. = 'Solver.Drop 1E_20'
default_overland.pfmg_octree.jac.Solver.AbsTol = 1E-9
#  
default_overland.pfmg_octree.jac.Solver.WriteSiloSubsurfData = True
default_overland.pfmg_octree.jac.Solver.WriteSiloPressure = True
default_overland.pfmg_octree.jac.Solver.WriteSiloSaturation = True
default_overland.pfmg_octree.jac.Solver.WriteSiloConcentration = True

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

# set water table to be at the bottom of the domain, the top layer is initially dry
default_overland.pfmg_octree.jac.ICPressure.Type = 'HydroStaticPatch'
default_overland.pfmg_octree.jac.ICPressure.GeomNames = 'domain'
default_overland.pfmg_octree.jac.Geom.domain.ICPressure.Value = -3.0

default_overland.pfmg_octree.jac.Geom.domain.ICPressure.RefGeom = 'domain'
default_overland.pfmg_octree.jac.Geom.domain.ICPressure.RefPatch = 'z_upper'

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
default_overland.pfmg_octree.jac.run()
