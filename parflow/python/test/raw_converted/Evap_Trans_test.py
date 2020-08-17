#  This test runs the tilted V but with time-dependent flux input
#  from a pfb file
#  or regular, uniform fluxes
#  similar to that in Kollet and Maxwell (2006) AWR

#
# Import the ParFlow TCL package
#
from parflow import Run
Evap_Trans_test = Run("Evap_Trans_test", __file__)

Evap_Trans_test.FileVersion = 4

Evap_Trans_test.Process.Topology.P = 1
Evap_Trans_test.Process.Topology.Q = 1
Evap_Trans_test.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
Evap_Trans_test.ComputationalGrid.Lower.X = 0.0
Evap_Trans_test.ComputationalGrid.Lower.Y = 0.0
Evap_Trans_test.ComputationalGrid.Lower.Z = 0.0

Evap_Trans_test.ComputationalGrid.NX = 30
Evap_Trans_test.ComputationalGrid.NY = 30
Evap_Trans_test.ComputationalGrid.NZ = 30

Evap_Trans_test.ComputationalGrid.DX = 10.0
Evap_Trans_test.ComputationalGrid.DY = 10.0
Evap_Trans_test.ComputationalGrid.DZ = .05

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
Evap_Trans_test.GeomInput.Names = 'domaininput leftinput rightinput channelinput'

Evap_Trans_test.GeomInput.domaininput.GeomName = 'domain'
Evap_Trans_test.GeomInput.leftinput.GeomName = 'left'
Evap_Trans_test.GeomInput.rightinput.GeomName = 'right'
Evap_Trans_test.GeomInput.channelinput.GeomName = 'channel'

Evap_Trans_test.GeomInput.domaininput.InputType = 'Box'
Evap_Trans_test.GeomInput.leftinput.InputType = 'Box'
Evap_Trans_test.GeomInput.rightinput.InputType = 'Box'
Evap_Trans_test.GeomInput.channelinput.InputType = 'Box'

#---------------------------------------------------------
# Domain Geometry 
#---------------------------------------------------------
Evap_Trans_test.Geom.domain.Lower.X = 0.0
Evap_Trans_test.Geom.domain.Lower.Y = 0.0
Evap_Trans_test.Geom.domain.Lower.Z = 0.0
#  
Evap_Trans_test.Geom.domain.Upper.X = 300.0
Evap_Trans_test.Geom.domain.Upper.Y = 300.0
Evap_Trans_test.Geom.domain.Upper.Z = 1.5
Evap_Trans_test.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'

#---------------------------------------------------------
# Left Slope Geometry 
#---------------------------------------------------------
Evap_Trans_test.Geom.left.Lower.X = 0.0
Evap_Trans_test.Geom.left.Lower.Y = 0.0
Evap_Trans_test.Geom.left.Lower.Z = 0.0
#  
Evap_Trans_test.Geom.left.Upper.X = 140.0
Evap_Trans_test.Geom.left.Upper.Y = 300.0
Evap_Trans_test.Geom.left.Upper.Z = 1.5

#---------------------------------------------------------
# Right Slope Geometry 
#---------------------------------------------------------
Evap_Trans_test.Geom.right.Lower.X = 160.0
Evap_Trans_test.Geom.right.Lower.Y = 0.0
Evap_Trans_test.Geom.right.Lower.Z = 0.0
#  
Evap_Trans_test.Geom.right.Upper.X = 300.0
Evap_Trans_test.Geom.right.Upper.Y = 300.0
Evap_Trans_test.Geom.right.Upper.Z = 1.5

#---------------------------------------------------------
# Channel Geometry 
#---------------------------------------------------------
Evap_Trans_test.Geom.channel.Lower.X = 140.0
Evap_Trans_test.Geom.channel.Lower.Y = 0.0
Evap_Trans_test.Geom.channel.Lower.Z = 0.0
#  
Evap_Trans_test.Geom.channel.Upper.X = 160.0
Evap_Trans_test.Geom.channel.Upper.Y = 300.0
Evap_Trans_test.Geom.channel.Upper.Z = 1.5

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

Evap_Trans_test.Geom.Perm.Names = 'left right channel'

# Values in m/hour

# these are examples to make the upper portions of the v heterogeneous
# the following is ignored if the perm.type "Constant" settings are not
# commented out, below.

Evap_Trans_test.Geom.left.Perm.Type = 'TurnBands'
Evap_Trans_test.Geom.left.Perm.LambdaX = 50.
Evap_Trans_test.Geom.left.Perm.LambdaY = 50.
Evap_Trans_test.Geom.left.Perm.LambdaZ = 0.5
Evap_Trans_test.Geom.left.Perm.GeomMean = 0.01

Evap_Trans_test.Geom.left.Perm.Sigma = 0.5
Evap_Trans_test.Geom.left.Perm.NumLines = 40
Evap_Trans_test.Geom.left.Perm.RZeta = 5.0
Evap_Trans_test.Geom.left.Perm.KMax = 100.0
Evap_Trans_test.Geom.left.Perm.DelK = 0.2
Evap_Trans_test.Geom.left.Perm.Seed = 33333
Evap_Trans_test.Geom.left.Perm.LogNormal = 'Log'
Evap_Trans_test.Geom.left.Perm.StratType = 'Bottom'


Evap_Trans_test.Geom.right.Perm.Type = 'TurnBands'
Evap_Trans_test.Geom.right.Perm.LambdaX = 50.
Evap_Trans_test.Geom.right.Perm.LambdaY = 50.
Evap_Trans_test.Geom.right.Perm.LambdaZ = 0.5
Evap_Trans_test.Geom.right.Perm.GeomMean = 0.05

Evap_Trans_test.Geom.right.Perm.Sigma = 0.5
Evap_Trans_test.Geom.right.Perm.NumLines = 40
Evap_Trans_test.Geom.right.Perm.RZeta = 5.0
Evap_Trans_test.Geom.right.Perm.KMax = 100.0
Evap_Trans_test.Geom.right.Perm.DelK = 0.2
Evap_Trans_test.Geom.right.Perm.Seed = 13333
Evap_Trans_test.Geom.right.Perm.LogNormal = 'Log'
Evap_Trans_test.Geom.right.Perm.StratType = 'Bottom'

# hydraulic conductivity is very low, but not zero, top node will have to saturate
# before overland flow can begin and will be driven by hortonian flow
# comment out the left and right settings to make the subsurface heterogeneous using
# turning bands above.  Run time increases quite a bit with a heterogeneous
# subsurface
#

Evap_Trans_test.Geom.left.Perm.Type = 'Constant'
Evap_Trans_test.Geom.left.Perm.Value = 0.001

Evap_Trans_test.Geom.right.Perm.Type = 'Constant'
Evap_Trans_test.Geom.right.Perm.Value = 0.01

Evap_Trans_test.Geom.channel.Perm.Type = 'Constant'
Evap_Trans_test.Geom.channel.Perm.Value = 0.00001

Evap_Trans_test.Perm.TensorType = 'TensorByGeom'

Evap_Trans_test.Geom.Perm.TensorByGeom.Names = 'domain'

Evap_Trans_test.Geom.domain.Perm.TensorValX = 1.0d0
Evap_Trans_test.Geom.domain.Perm.TensorValY = 1.0d0
Evap_Trans_test.Geom.domain.Perm.TensorValZ = 1.0d0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

Evap_Trans_test.SpecificStorage.Type = 'Constant'
Evap_Trans_test.SpecificStorage.GeomNames = 'domain'
Evap_Trans_test.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

Evap_Trans_test.Phase.Names = 'water'

Evap_Trans_test.Phase.water.Density.Type = 'Constant'
Evap_Trans_test.Phase.water.Density.Value = 1.0

Evap_Trans_test.Phase.water.Viscosity.Type = 'Constant'
Evap_Trans_test.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

Evap_Trans_test.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

Evap_Trans_test.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

Evap_Trans_test.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

# run for 2 hours @ 6min timesteps
# 
Evap_Trans_test.TimingInfo.BaseUnit = 0.1
Evap_Trans_test.TimingInfo.StartCount = 0
Evap_Trans_test.TimingInfo.StartTime = 0.0
Evap_Trans_test.TimingInfo.StopTime = 0.3
Evap_Trans_test.TimingInfo.DumpInterval = -1
Evap_Trans_test.TimeStep.Type = 'Constant'
Evap_Trans_test.TimeStep.Value = 0.1
#  
#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

Evap_Trans_test.Geom.Porosity.GeomNames = 'left right channel'

Evap_Trans_test.Geom.left.Porosity.Type = 'Constant'
Evap_Trans_test.Geom.left.Porosity.Value = 0.25

Evap_Trans_test.Geom.right.Porosity.Type = 'Constant'
Evap_Trans_test.Geom.right.Porosity.Value = 0.25

Evap_Trans_test.Geom.channel.Porosity.Type = 'Constant'
Evap_Trans_test.Geom.channel.Porosity.Value = 0.01

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

Evap_Trans_test.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

Evap_Trans_test.Phase.RelPerm.Type = 'VanGenuchten'
Evap_Trans_test.Phase.RelPerm.GeomNames = 'domain'

Evap_Trans_test.Geom.domain.RelPerm.Alpha = 6.0
Evap_Trans_test.Geom.domain.RelPerm.N = 2.

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

Evap_Trans_test.Phase.Saturation.Type = 'VanGenuchten'
Evap_Trans_test.Phase.Saturation.GeomNames = 'domain'

Evap_Trans_test.Geom.domain.Saturation.Alpha = 6.0
Evap_Trans_test.Geom.domain.Saturation.N = 2.
Evap_Trans_test.Geom.domain.Saturation.SRes = 0.2
Evap_Trans_test.Geom.domain.Saturation.SSat = 1.0



#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
Evap_Trans_test.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
Evap_Trans_test.Cycle.Names = 'constant rainrec'
Evap_Trans_test.Cycle.constant.Names = 'alltime'
Evap_Trans_test.Cycle.constant.alltime.Length = 1
Evap_Trans_test.Cycle.constant.Repeat = -1

# rainfall and recession time periods are defined here
# rain for 1 hour, recession for 2 hours

Evap_Trans_test.Cycle.rainrec.Names = 'rain rec'
Evap_Trans_test.Cycle.rainrec.rain.Length = 1
Evap_Trans_test.Cycle.rainrec.rec.Length = 2
Evap_Trans_test.Cycle.rainrec.Repeat = -1
#  
#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
Evap_Trans_test.BCPressure.PatchNames = [pfget Geom.domain.Patches]

Evap_Trans_test.Patch.x_lower.BCPressure.Type = 'FluxConst'
Evap_Trans_test.Patch.x_lower.BCPressure.Cycle = 'constant'
Evap_Trans_test.Patch.x_lower.BCPressure.alltime.Value = 0.0

Evap_Trans_test.Patch.y_lower.BCPressure.Type = 'FluxConst'
Evap_Trans_test.Patch.y_lower.BCPressure.Cycle = 'constant'
Evap_Trans_test.Patch.y_lower.BCPressure.alltime.Value = 0.0

Evap_Trans_test.Patch.z_lower.BCPressure.Type = 'FluxConst'
Evap_Trans_test.Patch.z_lower.BCPressure.Cycle = 'constant'
Evap_Trans_test.Patch.z_lower.BCPressure.alltime.Value = 0.0

Evap_Trans_test.Patch.x_upper.BCPressure.Type = 'FluxConst'
Evap_Trans_test.Patch.x_upper.BCPressure.Cycle = 'constant'
Evap_Trans_test.Patch.x_upper.BCPressure.alltime.Value = 0.0

Evap_Trans_test.Patch.y_upper.BCPressure.Type = 'FluxConst'
Evap_Trans_test.Patch.y_upper.BCPressure.Cycle = 'constant'
Evap_Trans_test.Patch.y_upper.BCPressure.alltime.Value = 0.0

## overland flow boundary condition with very heavy rainfall then slight ET
Evap_Trans_test.Patch.z_upper.BCPressure.Type = 'OverlandFlow'
Evap_Trans_test.Patch.z_upper.BCPressure.Cycle = 'constant'
#pfset Patch.z-upper.BCPressure.alltime.Value	      -0.5
Evap_Trans_test.Patch.z_upper.BCPressure.alltime.Value = 0.0
Evap_Trans_test.Patch.z_upper.BCPressure.rec.Value = 0.0000

# use tcl to write the file that we want for the fluxes
Evap_Trans_test.Solver.EvapTransFile = True
Evap_Trans_test.Solver.EvapTrans.FileName = 'evap.trans.test.pfb'

fileId = [open evap.trans.test.sa w 0600]
# puts $fileId "30 30 30"
# for {set kk 0} {$kk < 30} {incr kk} {
# for {set jj 0} {$jj < 30} {incr jj} {
# for {set ii 0} {$ii < 30} {incr ii} {
# if {$kk==29}  {
# 	set flux [expr (0.5 / 0.05)]
# } {
# 	set flux 0.0 }
# puts $fileId $flux

# }
# }
# }

# close $fileId

# load/setup flux files
file1 = [pfload -sa evap.trans.test.sa]
# pfsetgrid {30 30 30} {0.0 0.0 0.0} {10.0 10.0 0.05} $file1
# pfsave $file1 -pfb evap.trans.test.pfb
# pfsave $file1 -silo evap.trans.test.silo

# pfdist "evap.trans.test.pfb"

file2 = [pfload evap.trans.test.pfb]
# pfsave $file2 -sa test.txt

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

Evap_Trans_test.TopoSlopesX.Type = 'Constant'
Evap_Trans_test.TopoSlopesX.GeomNames = 'left right channel'
Evap_Trans_test.TopoSlopesX.Geom.left.Value = -0.005
Evap_Trans_test.TopoSlopesX.Geom.right.Value = 0.005
Evap_Trans_test.TopoSlopesX.Geom.channel.Value = 0.00

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------


Evap_Trans_test.TopoSlopesY.Type = 'Constant'
Evap_Trans_test.TopoSlopesY.GeomNames = 'left right channel'
Evap_Trans_test.TopoSlopesY.Geom.left.Value = 0.001
Evap_Trans_test.TopoSlopesY.Geom.right.Value = 0.001
Evap_Trans_test.TopoSlopesY.Geom.channel.Value = 0.001

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

Evap_Trans_test.Mannings.Type = 'Constant'
Evap_Trans_test.Mannings.GeomNames = 'left right channel'
Evap_Trans_test.Mannings.Geom.left.Value = 5.e-6
Evap_Trans_test.Mannings.Geom.right.Value = 5.e-6
Evap_Trans_test.Mannings.Geom.channel.Value = 1.e-6

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

Evap_Trans_test.PhaseSources.water.Type = 'Constant'
Evap_Trans_test.PhaseSources.water.GeomNames = 'domain'
Evap_Trans_test.PhaseSources.water.Geom.domain.Value = 0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

Evap_Trans_test.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

Evap_Trans_test.Solver = 'Richards'
Evap_Trans_test.Solver.MaxIter = 2500

Evap_Trans_test.Solver.Nonlinear.MaxIter = 300
Evap_Trans_test.Solver.Nonlinear.ResidualTol = 1e-4
Evap_Trans_test.Solver.Nonlinear.EtaChoice = 'Walker1'
Evap_Trans_test.Solver.Nonlinear.EtaChoice = 'EtaConstant'
Evap_Trans_test.Solver.Nonlinear.EtaValue = 0.001
Evap_Trans_test.Solver.Nonlinear.UseJacobian = False
Evap_Trans_test.Solver.Nonlinear.DerivativeEpsilon = 1e-16
Evap_Trans_test.Solver.Nonlinear.StepTol = 1e-10
Evap_Trans_test.Solver.Nonlinear.Globalization = 'LineSearch'
Evap_Trans_test.Solver.Linear.KrylovDimension = 20
Evap_Trans_test.Solver.Linear.MaxRestart = 2

Evap_Trans_test.Solver.Linear.Preconditioner = 'MGSemi'
Evap_Trans_test.Solver.Linear.Preconditioner.MGSemi.MaxIter = 1
Evap_Trans_test.Solver.Linear.Preconditioner.MGSemi.MaxLevels = 10
Evap_Trans_test.Solver.PrintSubsurf = False
Evap_Trans_test. = 'Solver.Drop 1E_20'
Evap_Trans_test.Solver.AbsTol = 1E-12
#  

Evap_Trans_test.Solver.WriteSiloSubsurfData = True
Evap_Trans_test.Solver.WriteSiloPressure = True
Evap_Trans_test.Solver.WriteSiloSaturation = True

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

# set water table to be at the bottom of the domain, the top layer is initially dry
Evap_Trans_test.ICPressure.Type = 'HydroStaticPatch'
Evap_Trans_test.ICPressure.GeomNames = 'domain'
Evap_Trans_test.Geom.domain.ICPressure.Value = -3.0

Evap_Trans_test.Geom.domain.ICPressure.RefGeom = 'domain'
Evap_Trans_test.Geom.domain.ICPressure.RefPatch = 'z_upper'

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

# pfrun evaptransfiletest1
# pfundist evaptransfiletest1

Evap_Trans_test.run()
