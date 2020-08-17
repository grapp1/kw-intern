#  This runs the tilted-v catchment problem
#  similar to that in Kollet and Maxwell (2006) AWR

tcl_precision = 17

# set runname flux_overland

#
# Import the ParFlow TCL package
#
from parflow import Run
overland_flux = Run("overland_flux", __file__)

overland_flux.FileVersion = 4

overland_flux.Process.Topology.P = [lindex $argv 0]
overland_flux.Process.Topology.Q = [lindex $argv 1]
overland_flux.Process.Topology.R = [lindex $argv 2]

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
overland_flux.ComputationalGrid.Lower.X = 0.0
overland_flux.ComputationalGrid.Lower.Y = 0.0
overland_flux.ComputationalGrid.Lower.Z = 0.0

overland_flux.ComputationalGrid.NX = 30
overland_flux.ComputationalGrid.NY = 30
overland_flux.ComputationalGrid.NZ = 30

overland_flux.ComputationalGrid.DX = 10.0
overland_flux.ComputationalGrid.DY = 10.0
overland_flux.ComputationalGrid.DZ = .05

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
overland_flux.GeomInput.Names = 'domaininput leftinput rightinput channelinput'

overland_flux.GeomInput.domaininput.GeomName = 'domain'
overland_flux.GeomInput.leftinput.GeomName = 'left'
overland_flux.GeomInput.rightinput.GeomName = 'right'
overland_flux.GeomInput.channelinput.GeomName = 'channel'

overland_flux.GeomInput.domaininput.InputType = 'Box'
overland_flux.GeomInput.leftinput.InputType = 'Box'
overland_flux.GeomInput.rightinput.InputType = 'Box'
overland_flux.GeomInput.channelinput.InputType = 'Box'

#---------------------------------------------------------
# Domain Geometry 
#---------------------------------------------------------
overland_flux.Geom.domain.Lower.X = 0.0
overland_flux.Geom.domain.Lower.Y = 0.0
overland_flux.Geom.domain.Lower.Z = 0.0
#  
overland_flux.Geom.domain.Upper.X = 300.0
overland_flux.Geom.domain.Upper.Y = 300.0
overland_flux.Geom.domain.Upper.Z = 1.5
overland_flux.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'

#---------------------------------------------------------
# Left Slope Geometry 
#---------------------------------------------------------
overland_flux.Geom.left.Lower.X = 0.0
overland_flux.Geom.left.Lower.Y = 0.0
overland_flux.Geom.left.Lower.Z = 0.0
#  
overland_flux.Geom.left.Upper.X = 140.0
overland_flux.Geom.left.Upper.Y = 300.0
overland_flux.Geom.left.Upper.Z = 1.5

#---------------------------------------------------------
# Right Slope Geometry 
#---------------------------------------------------------
overland_flux.Geom.right.Lower.X = 160.0
overland_flux.Geom.right.Lower.Y = 0.0
overland_flux.Geom.right.Lower.Z = 0.0
#  
overland_flux.Geom.right.Upper.X = 300.0
overland_flux.Geom.right.Upper.Y = 300.0
overland_flux.Geom.right.Upper.Z = 1.5

#---------------------------------------------------------
# Channel Geometry 
#---------------------------------------------------------
overland_flux.Geom.channel.Lower.X = 140.0
overland_flux.Geom.channel.Lower.Y = 0.0
overland_flux.Geom.channel.Lower.Z = 0.0
#  
overland_flux.Geom.channel.Upper.X = 160.0
overland_flux.Geom.channel.Upper.Y = 300.0
overland_flux.Geom.channel.Upper.Z = 1.5

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

overland_flux.Geom.Perm.Names = 'left right channel'

# Values in m/hour

# these are examples to make the upper portions of the v heterogeneous
# the following is ignored if the perm.type "Constant" settings are not
# commented out, below.

overland_flux.Geom.left.Perm.Type = 'TurnBands'
overland_flux.Geom.left.Perm.LambdaX = 50.
overland_flux.Geom.left.Perm.LambdaY = 50.
overland_flux.Geom.left.Perm.LambdaZ = 0.5
overland_flux.Geom.left.Perm.GeomMean = 0.01

overland_flux.Geom.left.Perm.Sigma = 0.5
overland_flux.Geom.left.Perm.NumLines = 40
overland_flux.Geom.left.Perm.RZeta = 5.0
overland_flux.Geom.left.Perm.KMax = 100.0
overland_flux.Geom.left.Perm.DelK = 0.2
overland_flux.Geom.left.Perm.Seed = 33333
overland_flux.Geom.left.Perm.LogNormal = 'Log'
overland_flux.Geom.left.Perm.StratType = 'Bottom'


overland_flux.Geom.right.Perm.Type = 'TurnBands'
overland_flux.Geom.right.Perm.LambdaX = 50.
overland_flux.Geom.right.Perm.LambdaY = 50.
overland_flux.Geom.right.Perm.LambdaZ = 0.5
overland_flux.Geom.right.Perm.GeomMean = 0.05

overland_flux.Geom.right.Perm.Sigma = 0.5
overland_flux.Geom.right.Perm.NumLines = 40
overland_flux.Geom.right.Perm.RZeta = 5.0
overland_flux.Geom.right.Perm.KMax = 100.0
overland_flux.Geom.right.Perm.DelK = 0.2
overland_flux.Geom.right.Perm.Seed = 13333
overland_flux.Geom.right.Perm.LogNormal = 'Log'
overland_flux.Geom.right.Perm.StratType = 'Bottom'

# hydraulic conductivity is very low, but not zero, top node will have to saturate
# before overland flow can begin and will be driven by hortonian flow
# comment out the left and right settings to make the subsurface heterogeneous using
# turning bands above.  Run time increases quite a bit with a heterogeneous
# subsurface
#

overland_flux.Geom.left.Perm.Type = 'Constant'
overland_flux.Geom.left.Perm.Value = 0.001

overland_flux.Geom.right.Perm.Type = 'Constant'
overland_flux.Geom.right.Perm.Value = 0.01

overland_flux.Geom.channel.Perm.Type = 'Constant'
overland_flux.Geom.channel.Perm.Value = 0.00001

overland_flux.Perm.TensorType = 'TensorByGeom'

overland_flux.Geom.Perm.TensorByGeom.Names = 'domain'

overland_flux.Geom.domain.Perm.TensorValX = 1.0d0
overland_flux.Geom.domain.Perm.TensorValY = 1.0d0
overland_flux.Geom.domain.Perm.TensorValZ = 1.0d0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

overland_flux.SpecificStorage.Type = 'Constant'
overland_flux.SpecificStorage.GeomNames = 'domain'
overland_flux.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

overland_flux.Phase.Names = 'water'

overland_flux.Phase.water.Density.Type = 'Constant'
overland_flux.Phase.water.Density.Value = 1.0

overland_flux.Phase.water.Viscosity.Type = 'Constant'
overland_flux.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

overland_flux.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

overland_flux.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

overland_flux.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

# 
overland_flux.TimingInfo.BaseUnit = 0.1
overland_flux.TimingInfo.StartCount = 0
overland_flux.TimingInfo.StartTime = 0.0
overland_flux.TimingInfo.StopTime = 0.4
overland_flux.TimingInfo.DumpInterval = -1
overland_flux.TimeStep.Type = 'Constant'
overland_flux.TimeStep.Value = 0.1
#  
#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

overland_flux.Geom.Porosity.GeomNames = 'left right channel'

overland_flux.Geom.left.Porosity.Type = 'Constant'
overland_flux.Geom.left.Porosity.Value = 0.25

overland_flux.Geom.right.Porosity.Type = 'Constant'
overland_flux.Geom.right.Porosity.Value = 0.25

overland_flux.Geom.channel.Porosity.Type = 'Constant'
overland_flux.Geom.channel.Porosity.Value = 0.01

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

overland_flux.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

overland_flux.Phase.RelPerm.Type = 'VanGenuchten'
overland_flux.Phase.RelPerm.GeomNames = 'domain'

overland_flux.Geom.domain.RelPerm.Alpha = 6.0
overland_flux.Geom.domain.RelPerm.N = 2.

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

overland_flux.Phase.Saturation.Type = 'VanGenuchten'
overland_flux.Phase.Saturation.GeomNames = 'domain'

overland_flux.Geom.domain.Saturation.Alpha = 6.0
overland_flux.Geom.domain.Saturation.N = 2.
overland_flux.Geom.domain.Saturation.SRes = 0.2
overland_flux.Geom.domain.Saturation.SSat = 1.0



#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
overland_flux.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
overland_flux.Cycle.Names = 'constant rainrec'
overland_flux.Cycle.constant.Names = 'alltime'
overland_flux.Cycle.constant.alltime.Length = 1
overland_flux.Cycle.constant.Repeat = -1

# rainfall and recession time periods are defined here
# rain for 1 hour, recession for 2 hours

overland_flux.Cycle.rainrec.Names = 'rain rec'
overland_flux.Cycle.rainrec.rain.Length = 2
overland_flux.Cycle.rainrec.rec.Length = 2
overland_flux.Cycle.rainrec.Repeat = -1
#  
#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
overland_flux.BCPressure.PatchNames = [pfget Geom.domain.Patches]

overland_flux.Patch.x_lower.BCPressure.Type = 'FluxConst'
overland_flux.Patch.x_lower.BCPressure.Cycle = 'constant'
overland_flux.Patch.x_lower.BCPressure.alltime.Value = 0.0

overland_flux.Patch.y_lower.BCPressure.Type = 'FluxConst'
overland_flux.Patch.y_lower.BCPressure.Cycle = 'constant'
overland_flux.Patch.y_lower.BCPressure.alltime.Value = 0.0

overland_flux.Patch.z_lower.BCPressure.Type = 'FluxConst'
overland_flux.Patch.z_lower.BCPressure.Cycle = 'constant'
overland_flux.Patch.z_lower.BCPressure.alltime.Value = 0.0

overland_flux.Patch.x_upper.BCPressure.Type = 'FluxConst'
overland_flux.Patch.x_upper.BCPressure.Cycle = 'constant'
overland_flux.Patch.x_upper.BCPressure.alltime.Value = 0.0

overland_flux.Patch.y_upper.BCPressure.Type = 'FluxConst'
overland_flux.Patch.y_upper.BCPressure.Cycle = 'constant'
overland_flux.Patch.y_upper.BCPressure.alltime.Value = 0.0

## overland flow boundary condition with very heavy rainfall then slight ET
overland_flux.Patch.z_upper.BCPressure.Type = 'OverlandFlow'
overland_flux.Patch.z_upper.BCPressure.Cycle = 'rainrec'
overland_flux.Patch.z_upper.BCPressure.rain.Value = -0.05
overland_flux.Patch.z_upper.BCPressure.rain.Value = 0.0
overland_flux.Patch.z_upper.BCPressure.rec.Value = 0.000

overland_flux.Solver.EvapTransFileTransient = True
overland_flux.Solver.EvapTrans.FileName = 'Forcing'

fileId = [open flux.rain.sa w]
# puts $fileId "30 30 30"
# for { set kk 0 } { $kk < 30 } { incr kk } {
# for { set jj 0 } { $jj < 30 } { incr jj } {
# for { set ii 0 } { $ii < 30 } { incr ii } {

# 	if {$kk == 29} {
# 		# convert from 0.05 m / h of rainfall to flux 1/t units; not negative positive flip
# 		# and divide by dz
# 		puts $fileId [expr (0.05/0.05)] 
# 	} else {
# 		puts $fileId "0.0"  }
# }
# }
# }

# close $fileId

fileId = [open flux.rec.sa w]
# puts $fileId "30 30 30"
# for { set kk 0 } { $kk < 30 } { incr kk } {
# for { set jj 0 } { $jj < 30 } { incr jj } {
# for { set ii 0 } { $ii < 30 } { incr ii } {

# 		puts $fileId "0.0" 
# }
# }
# }

# close $fileId

flux = [pfload -sa flux.rain.sa]
# pfsetgrid {30 30 30} {0.0 0.0 0.0} {10.0 10.0 0.05} $flux
# pfsave $flux -pfb Forcing.00000.pfb 
# pfsave $flux -silo Forcing.00000.silo 
# pfsave $flux -pfb Forcing.00001.pfb 
# pfsave $flux -pfb Forcing.00002.pfb 
flux = [pfload -sa flux.rec.sa]
# pfsetgrid {30 30 30} {0.0 0.0 0.0} {10.0 10.0 0.05} $flux
# pfsave $flux -pfb Forcing.00003.pfb 
# pfsave $flux -pfb Forcing.00004.pfb 
# pfsave $flux -pfb Forcing.00005.pfb 

# pfdist  Forcing.00000.pfb 
# pfdist  Forcing.00001.pfb 
# pfdist  Forcing.00002.pfb 
# pfdist  Forcing.00003.pfb 
# pfdist  Forcing.00004.pfb 
# pfdist  Forcing.00005.pfb 



#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

overland_flux.TopoSlopesX.Type = 'Constant'
overland_flux.TopoSlopesX.GeomNames = 'left right channel'
overland_flux.TopoSlopesX.Geom.left.Value = -0.005
overland_flux.TopoSlopesX.Geom.right.Value = 0.005
overland_flux.TopoSlopesX.Geom.channel.Value = 0.00

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------


overland_flux.TopoSlopesY.Type = 'Constant'
overland_flux.TopoSlopesY.GeomNames = 'left right channel'
overland_flux.TopoSlopesY.Geom.left.Value = 0.001
overland_flux.TopoSlopesY.Geom.right.Value = 0.001
overland_flux.TopoSlopesY.Geom.channel.Value = 0.001

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

overland_flux.Mannings.Type = 'Constant'
overland_flux.Mannings.GeomNames = 'left right channel'
overland_flux.Mannings.Geom.left.Value = 5.e-6
overland_flux.Mannings.Geom.right.Value = 5.e-6
overland_flux.Mannings.Geom.channel.Value = 1.e-6

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

overland_flux.PhaseSources.water.Type = 'Constant'
overland_flux.PhaseSources.water.GeomNames = 'domain'
overland_flux.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

overland_flux.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

overland_flux.Solver = 'Richards'
overland_flux.Solver.MaxIter = 2500
overland_flux.OverlandFlowDiffusive = 0


overland_flux.Solver.Nonlinear.MaxIter = 20
overland_flux.Solver.Nonlinear.ResidualTol = 1e-9
overland_flux.Solver.Nonlinear.EtaChoice = 'EtaConstant'
overland_flux.Solver.Nonlinear.EtaValue = 0.01
overland_flux.Solver.Nonlinear.UseJacobian = False
overland_flux.Solver.Nonlinear.UseJacobian = True
overland_flux.Solver.Nonlinear.DerivativeEpsilon = 1e-8
overland_flux.Solver.Nonlinear.StepTol = 1e-20
overland_flux.Solver.Nonlinear.Globalization = 'LineSearch'
overland_flux.Solver.Linear.KrylovDimension = 20
overland_flux.Solver.Linear.MaxRestart = 2

overland_flux.Solver.Linear.Preconditioner = 'PFMGOctree'
overland_flux.Solver.Linear.Preconditioner = 'PFMG'
#pfset Solver.Linear.Preconditioner                       MGSemi 
overland_flux.Solver.Linear.Preconditioner.PCMatrixType = 'FullJacobian'
overland_flux.Solver.PrintSubsurf = False
overland_flux. = 'Solver.Drop 1E_20'
overland_flux.Solver.AbsTol = 1E-9
#  
overland_flux.Solver.WriteSiloSubsurfData = True
overland_flux.Solver.WriteSiloPressure = True
overland_flux.Solver.WriteSiloSaturation = True
overland_flux.Solver.WriteSiloConcentration = True

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

# set water table to be at the bottom of the domain, the top layer is initially dry
overland_flux.ICPressure.Type = 'HydroStaticPatch'
overland_flux.ICPressure.GeomNames = 'domain'
overland_flux.Geom.domain.ICPressure.Value = -3.0

overland_flux.Geom.domain.ICPressure.RefGeom = 'domain'
overland_flux.Geom.domain.ICPressure.RefPatch = 'z_upper'

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

# pfrun $runname
# pfundist $runname


overland_flux.run()
