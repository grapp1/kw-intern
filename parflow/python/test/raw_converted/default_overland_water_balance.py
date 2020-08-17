#  This runs the tilted-v catchment problem
#  similar to that in Kollet and Maxwell (2006) AWR

tcl_precision = 17

# set runname default_overland

#
# Import the ParFlow TCL package
#
from parflow import Run
default_overland_water_balance = Run("default_overland_water_balance", __file__)

default_overland_water_balance.FileVersion = 4

default_overland_water_balance.Process.Topology.P = 1
default_overland_water_balance.Process.Topology.Q = 1
default_overland_water_balance.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
default_overland_water_balance.ComputationalGrid.Lower.X = 0.0
default_overland_water_balance.ComputationalGrid.Lower.Y = 0.0
default_overland_water_balance.ComputationalGrid.Lower.Z = 0.0

default_overland_water_balance.ComputationalGrid.NX = 30
default_overland_water_balance.ComputationalGrid.NY = 30
default_overland_water_balance.ComputationalGrid.NZ = 30

default_overland_water_balance.ComputationalGrid.DX = 10.0
default_overland_water_balance.ComputationalGrid.DY = 10.0
default_overland_water_balance.ComputationalGrid.DZ = .05

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
default_overland_water_balance.GeomInput.Names = 'domaininput leftinput rightinput channelinput'

default_overland_water_balance.GeomInput.domaininput.GeomName = 'domain'
default_overland_water_balance.GeomInput.leftinput.GeomName = 'left'
default_overland_water_balance.GeomInput.rightinput.GeomName = 'right'
default_overland_water_balance.GeomInput.channelinput.GeomName = 'channel'

default_overland_water_balance.GeomInput.domaininput.InputType = 'Box'
default_overland_water_balance.GeomInput.leftinput.InputType = 'Box'
default_overland_water_balance.GeomInput.rightinput.InputType = 'Box'
default_overland_water_balance.GeomInput.channelinput.InputType = 'Box'

#---------------------------------------------------------
# Domain Geometry 
#---------------------------------------------------------
default_overland_water_balance.Geom.domain.Lower.X = 0.0
default_overland_water_balance.Geom.domain.Lower.Y = 0.0
default_overland_water_balance.Geom.domain.Lower.Z = 0.0
#  
default_overland_water_balance.Geom.domain.Upper.X = 300.0
default_overland_water_balance.Geom.domain.Upper.Y = 300.0
default_overland_water_balance.Geom.domain.Upper.Z = 1.5
default_overland_water_balance.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'

#---------------------------------------------------------
# Left Slope Geometry 
#---------------------------------------------------------
default_overland_water_balance.Geom.left.Lower.X = 0.0
default_overland_water_balance.Geom.left.Lower.Y = 0.0
default_overland_water_balance.Geom.left.Lower.Z = 0.0
#  
default_overland_water_balance.Geom.left.Upper.X = 140.0
default_overland_water_balance.Geom.left.Upper.Y = 300.0
default_overland_water_balance.Geom.left.Upper.Z = 1.5

#---------------------------------------------------------
# Right Slope Geometry 
#---------------------------------------------------------
default_overland_water_balance.Geom.right.Lower.X = 160.0
default_overland_water_balance.Geom.right.Lower.Y = 0.0
default_overland_water_balance.Geom.right.Lower.Z = 0.0
#  
default_overland_water_balance.Geom.right.Upper.X = 300.0
default_overland_water_balance.Geom.right.Upper.Y = 300.0
default_overland_water_balance.Geom.right.Upper.Z = 1.5

#---------------------------------------------------------
# Channel Geometry 
#---------------------------------------------------------
default_overland_water_balance.Geom.channel.Lower.X = 140.0
default_overland_water_balance.Geom.channel.Lower.Y = 0.0
default_overland_water_balance.Geom.channel.Lower.Z = 0.0
#  
default_overland_water_balance.Geom.channel.Upper.X = 160.0
default_overland_water_balance.Geom.channel.Upper.Y = 300.0
default_overland_water_balance.Geom.channel.Upper.Z = 1.5

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

default_overland_water_balance.Geom.Perm.Names = 'left right channel'

# Values in m/hour

# these are examples to make the upper portions of the v heterogeneous
# the following is ignored if the perm.type "Constant" settings are not
# commented out, below.

default_overland_water_balance.Geom.left.Perm.Type = 'TurnBands'
default_overland_water_balance.Geom.left.Perm.LambdaX = 50.
default_overland_water_balance.Geom.left.Perm.LambdaY = 50.
default_overland_water_balance.Geom.left.Perm.LambdaZ = 0.5
default_overland_water_balance.Geom.left.Perm.GeomMean = 0.01

default_overland_water_balance.Geom.left.Perm.Sigma = 0.5
default_overland_water_balance.Geom.left.Perm.NumLines = 40
default_overland_water_balance.Geom.left.Perm.RZeta = 5.0
default_overland_water_balance.Geom.left.Perm.KMax = 100.0
default_overland_water_balance.Geom.left.Perm.DelK = 0.2
default_overland_water_balance.Geom.left.Perm.Seed = 33333
default_overland_water_balance.Geom.left.Perm.LogNormal = 'Log'
default_overland_water_balance.Geom.left.Perm.StratType = 'Bottom'


default_overland_water_balance.Geom.right.Perm.Type = 'TurnBands'
default_overland_water_balance.Geom.right.Perm.LambdaX = 50.
default_overland_water_balance.Geom.right.Perm.LambdaY = 50.
default_overland_water_balance.Geom.right.Perm.LambdaZ = 0.5
default_overland_water_balance.Geom.right.Perm.GeomMean = 0.05

default_overland_water_balance.Geom.right.Perm.Sigma = 0.5
default_overland_water_balance.Geom.right.Perm.NumLines = 40
default_overland_water_balance.Geom.right.Perm.RZeta = 5.0
default_overland_water_balance.Geom.right.Perm.KMax = 100.0
default_overland_water_balance.Geom.right.Perm.DelK = 0.2
default_overland_water_balance.Geom.right.Perm.Seed = 13333
default_overland_water_balance.Geom.right.Perm.LogNormal = 'Log'
default_overland_water_balance.Geom.right.Perm.StratType = 'Bottom'

# hydraulic conductivity is very low, but not zero, top node will have to saturate
# before overland flow can begin and will be driven by hortonian flow
# comment out the left and right settings to make the subsurface heterogeneous using
# turning bands above.  Run time increases quite a bit with a heterogeneous
# subsurface
#

default_overland_water_balance.Geom.left.Perm.Type = 'Constant'
default_overland_water_balance.Geom.left.Perm.Value = 0.001

default_overland_water_balance.Geom.right.Perm.Type = 'Constant'
default_overland_water_balance.Geom.right.Perm.Value = 0.01

default_overland_water_balance.Geom.channel.Perm.Type = 'Constant'
default_overland_water_balance.Geom.channel.Perm.Value = 0.00001

default_overland_water_balance.Perm.TensorType = 'TensorByGeom'

default_overland_water_balance.Geom.Perm.TensorByGeom.Names = 'domain'

default_overland_water_balance.Geom.domain.Perm.TensorValX = 1.0d0
default_overland_water_balance.Geom.domain.Perm.TensorValY = 1.0d0
default_overland_water_balance.Geom.domain.Perm.TensorValZ = 1.0d0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

default_overland_water_balance.SpecificStorage.Type = 'Constant'
default_overland_water_balance.SpecificStorage.GeomNames = 'domain'
default_overland_water_balance.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

default_overland_water_balance.Phase.Names = 'water'

default_overland_water_balance.Phase.water.Density.Type = 'Constant'
default_overland_water_balance.Phase.water.Density.Value = 1.0

default_overland_water_balance.Phase.water.Viscosity.Type = 'Constant'
default_overland_water_balance.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

default_overland_water_balance.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

default_overland_water_balance.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

default_overland_water_balance.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

# 
default_overland_water_balance.TimingInfo.BaseUnit = 0.1
default_overland_water_balance.TimingInfo.StartCount = 0
default_overland_water_balance.TimingInfo.StartTime = 0.0
default_overland_water_balance.TimingInfo.StopTime = 2.0
default_overland_water_balance.TimingInfo.DumpInterval = -1
default_overland_water_balance.TimeStep.Type = 'Constant'
default_overland_water_balance.TimeStep.Value = 0.1
#  
#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

default_overland_water_balance.Geom.Porosity.GeomNames = 'left right channel'

default_overland_water_balance.Geom.left.Porosity.Type = 'Constant'
default_overland_water_balance.Geom.left.Porosity.Value = 0.25

default_overland_water_balance.Geom.right.Porosity.Type = 'Constant'
default_overland_water_balance.Geom.right.Porosity.Value = 0.25

default_overland_water_balance.Geom.channel.Porosity.Type = 'Constant'
default_overland_water_balance.Geom.channel.Porosity.Value = 0.01

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

default_overland_water_balance.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

default_overland_water_balance.Phase.RelPerm.Type = 'VanGenuchten'
default_overland_water_balance.Phase.RelPerm.GeomNames = 'domain'

default_overland_water_balance.Geom.domain.RelPerm.Alpha = 6.0
default_overland_water_balance.Geom.domain.RelPerm.N = 2.

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

default_overland_water_balance.Phase.Saturation.Type = 'VanGenuchten'
default_overland_water_balance.Phase.Saturation.GeomNames = 'domain'

default_overland_water_balance.Geom.domain.Saturation.Alpha = 6.0
default_overland_water_balance.Geom.domain.Saturation.N = 2.
default_overland_water_balance.Geom.domain.Saturation.SRes = 0.2
default_overland_water_balance.Geom.domain.Saturation.SSat = 1.0



#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
default_overland_water_balance.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
default_overland_water_balance.Cycle.Names = 'constant rainrec'
default_overland_water_balance.Cycle.constant.Names = 'alltime'
default_overland_water_balance.Cycle.constant.alltime.Length = 1
default_overland_water_balance.Cycle.constant.Repeat = -1

# rainfall and recession time periods are defined here
# rain for 1 hour, recession for 2 hours

default_overland_water_balance.Cycle.rainrec.Names = 'rain rec'
default_overland_water_balance.Cycle.rainrec.rain.Length = 1
default_overland_water_balance.Cycle.rainrec.rec.Length = 2
default_overland_water_balance.Cycle.rainrec.Repeat = -1
#  
#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
default_overland_water_balance.BCPressure.PatchNames = [pfget Geom.domain.Patches]

default_overland_water_balance.Patch.x_lower.BCPressure.Type = 'FluxConst'
default_overland_water_balance.Patch.x_lower.BCPressure.Cycle = 'constant'
default_overland_water_balance.Patch.x_lower.BCPressure.alltime.Value = 0.0

default_overland_water_balance.Patch.y_lower.BCPressure.Type = 'FluxConst'
default_overland_water_balance.Patch.y_lower.BCPressure.Cycle = 'constant'
default_overland_water_balance.Patch.y_lower.BCPressure.alltime.Value = 0.0

default_overland_water_balance.Patch.z_lower.BCPressure.Type = 'FluxConst'
default_overland_water_balance.Patch.z_lower.BCPressure.Cycle = 'constant'
default_overland_water_balance.Patch.z_lower.BCPressure.alltime.Value = 0.0

default_overland_water_balance.Patch.x_upper.BCPressure.Type = 'FluxConst'
default_overland_water_balance.Patch.x_upper.BCPressure.Cycle = 'constant'
default_overland_water_balance.Patch.x_upper.BCPressure.alltime.Value = 0.0

default_overland_water_balance.Patch.y_upper.BCPressure.Type = 'FluxConst'
default_overland_water_balance.Patch.y_upper.BCPressure.Cycle = 'constant'
default_overland_water_balance.Patch.y_upper.BCPressure.alltime.Value = 0.0

## overland flow boundary condition with very heavy rainfall then slight ET
default_overland_water_balance.Patch.z_upper.BCPressure.Type = 'OverlandFlow'
#pfset Patch.z-upper.BCPressure.Cycle		      "rainrec"
#pfset Patch.z-upper.BCPressure.rain.Value	      -0.05
#pfset Patch.z-upper.BCPressure.rec.Value	      0.000001
#pfset Patch.z-upper.BCPressure.rec.Value	      -0.05

default_overland_water_balance.Patch.z_upper.BCPressure.Cycle = 'constant'
default_overland_water_balance.Patch.z_upper.BCPressure.alltime.Value = 0.000001


#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

default_overland_water_balance.TopoSlopesX.Type = 'Constant'
default_overland_water_balance.TopoSlopesX.GeomNames = 'left right channel'
#pfset TopoSlopesX.Geom.left.Value -0.005
#pfset TopoSlopesX.Geom.right.Value 0.005
default_overland_water_balance.TopoSlopesX.Geom.left.Value = 0.0
default_overland_water_balance.TopoSlopesX.Geom.right.Value = 0.0
default_overland_water_balance.TopoSlopesX.Geom.channel.Value = 0.00

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------


default_overland_water_balance.TopoSlopesY.Type = 'Constant'
default_overland_water_balance.TopoSlopesY.GeomNames = 'left right channel'
#pfset TopoSlopesY.Geom.left.Value 0.001
#pfset TopoSlopesY.Geom.right.Value 0.001
#pfset TopoSlopesY.Geom.channel.Value 0.001

default_overland_water_balance.TopoSlopesY.Geom.left.Value = 0.00
default_overland_water_balance.TopoSlopesY.Geom.right.Value = 0.00
default_overland_water_balance.TopoSlopesY.Geom.channel.Value = 0.00


#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

default_overland_water_balance.Mannings.Type = 'Constant'
default_overland_water_balance.Mannings.GeomNames = 'left right channel'
default_overland_water_balance.Mannings.Geom.left.Value = 5.e-6
default_overland_water_balance.Mannings.Geom.right.Value = 5.e-6
default_overland_water_balance.Mannings.Geom.channel.Value = 1.e-6

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

default_overland_water_balance.PhaseSources.water.Type = 'Constant'
default_overland_water_balance.PhaseSources.water.GeomNames = 'domain'
default_overland_water_balance.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

default_overland_water_balance.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

default_overland_water_balance.Solver = 'Richards'
default_overland_water_balance.Solver.MaxIter = 2500

default_overland_water_balance.Solver.Nonlinear.MaxIter = 300
default_overland_water_balance.Solver.Nonlinear.ResidualTol = 1e-9
default_overland_water_balance.Solver.Nonlinear.EtaChoice = 'Walker1'
default_overland_water_balance.Solver.Nonlinear.EtaChoice = 'EtaConstant'
default_overland_water_balance.Solver.Nonlinear.EtaValue = 0.001
default_overland_water_balance.Solver.Nonlinear.UseJacobian = False
default_overland_water_balance.Solver.Nonlinear.DerivativeEpsilon = 1e-16
default_overland_water_balance.Solver.Nonlinear.StepTol = 1e-10
default_overland_water_balance.Solver.Nonlinear.Globalization = 'LineSearch'
default_overland_water_balance.Solver.Linear.KrylovDimension = 20
default_overland_water_balance.Solver.Linear.MaxRestart = 2

default_overland_water_balance.Solver.Linear.Preconditioner = 'MGSemi'
default_overland_water_balance.Solver.Linear.Preconditioner.MGSemi.MaxIter = 1
default_overland_water_balance.Solver.Linear.Preconditioner.MGSemi.MaxLevels = 10
default_overland_water_balance.Solver.PrintSubsurf = False
default_overland_water_balance. = 'Solver.Drop 1E_20'
default_overland_water_balance.Solver.AbsTol = 1E-12
#  
default_overland_water_balance.Solver.WriteSiloSubsurfData = True
default_overland_water_balance.Solver.WriteSiloPressure = True
default_overland_water_balance.Solver.WriteSiloSaturation = True
default_overland_water_balance.Solver.WriteSiloConcentration = True
default_overland_water_balance.Solver.WriteSiloSlopes = True
default_overland_water_balance.Solver.WriteSiloMask = True
default_overland_water_balance.Solver.WriteSiloEvapTrans = True
default_overland_water_balance.Solver.WriteSiloMannings = True
default_overland_water_balance.Solver.WriteSiloSpecificStorage = True

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

# set water table to be at the bottom of the domain, the top layer is initially dry
default_overland_water_balance.ICPressure.Type = 'HydroStaticPatch'
default_overland_water_balance.ICPressure.GeomNames = 'domain'
default_overland_water_balance.Geom.domain.ICPressure.Value = -3.0

default_overland_water_balance.Geom.domain.ICPressure.RefGeom = 'domain'
default_overland_water_balance.Geom.domain.ICPressure.RefPatch = 'z_upper'

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

# set slope_x [pfload $runname.out.slope_x.silo]
# set slope_y [pfload $runname.out.slope_y.silo]
# set mannings [pfload $runname.out.mannings.silo]
# set specific_storage [pfload $runname.out.specific_storage.silo]
# set porosity [pfload $runname.out.porosity.silo]

mask = [pfload default_overland.out.mask.silo]
top = [pfcomputetop $mask]

surface_area_of_domain = [expr [pfget ComputationalGrid.DX] * [pfget ComputationalGrid.DY] * [pfget ComputationalGrid.NX] * [pfget ComputationalGrid.NY]]

# running sum of all runoff over all time
sum_surface_runoff = 0.0

prev_total_water_balance = 0.0
# for {set i 0} {$i <= 20} {incr i} {
#     puts "======================================================"
#     puts "Timestep $i"
#     puts "======================================================"
#     set total_water_balance 0.0

#     set filename [format "%s.out.press.%05d.pfb" $runname $i]
#     set pressure [pfload $filename]
#     set surface_storage [pfsurfacestorage $top $pressure]
#     set total_surface_storage [pfsum $surface_storage]
#     puts "Surface storage : $total_surface_storage"
#     set total_water_balance [expr $total_water_balance + $total_surface_storage]

#     set filename [format "%s.out.satur.%05d.pfb" $runname $i]
#     set saturation [pfload $filename]

#     set subsurface_storage [pfsubsurfacestorage $mask $porosity $pressure $saturation $specific_storage]
#     set total_subsurface_storage [pfsum $subsurface_storage]
#     puts "Subsurface storage : $total_subsurface_storage"
#     set total_water_balance [expr $total_water_balance + $total_subsurface_storage]

#     set surface_runoff [pfsurfacerunoff $top $slope_x $slope_y $mannings $pressure]
#     pfsave $surface_runoff -silo "surface_runoff.$i.silo"
#     set total_surface_runoff [pfsum $surface_runoff]
#     puts "Surface runoff : $total_surface_runoff"
#     set sum_surface_runoff [expr $sum_surface_runoff + $total_surface_runoff]
#     set total_water_balance [expr $total_water_balance + $sum_surface_runoff]

#     if { $i > 0 } {
# 	set filename [format "%s.out.evaptrans.%05d.silo" $runname $i]
# 	set evaptrans [pfload $filename]
# 	set total_evaptrans [pfsum $evaptrans]
# 	puts "EvapTrans : $total_evaptrans"
# 	set total_water_balance [expr $total_water_balance + $total_evaptrans]
#     }

#    puts [format "Rain flux %f" [expr [pfget Patch.z-upper.BCPressure.rain.Value] * $surface_area_of_domain * [pfget TimeStep.Value]]]
#    puts [format "Rec flux %f" [expr [pfget Patch.z-upper.BCPressure.rec.Value] * $surface_area_of_domain * [pfget TimeStep.Value]]]

#     puts [format "Boundary flux %f" [expr [pfget Patch.z-upper.BCPressure.alltime.Value] * $surface_area_of_domain * [pfget TimeStep.Value]]]

#     puts "Total water balance : $total_water_balance"

#     if { $i > 0 } {
# 	puts [format "\tdifference from prev : %f" [expr $total_water_balance - $prev_total_water_balance]]
#     }

#     set prev_total_water_balance [expr $total_water_balance]
# }


# if $passed {
#     puts "$runname : PASSED"
# } {
#     puts "$runname : FAILED"
# }

default_overland_water_balance.run()
