#  This runs the a Little Washita Test Problem with variable dz
#  and a constant rain forcing.  The full Jacobian is use and there is no dampening in the
#  overland flow.

tcl_precision = 17

# set runname LW_var_dz

#
# Import the ParFlow TCL package
#
from parflow import Run
LW_var_dz = Run("LW_var_dz", __file__)

LW_var_dz.FileVersion = 4

LW_var_dz.Process.Topology.P = [lindex $argv 0]
LW_var_dz.Process.Topology.Q = [lindex $argv 1]
LW_var_dz.Process.Topology.R = [lindex $argv 2]

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
LW_var_dz.ComputationalGrid.Lower.X = 0.0
LW_var_dz.ComputationalGrid.Lower.Y = 0.0
LW_var_dz.ComputationalGrid.Lower.Z = 0.0

LW_var_dz.ComputationalGrid.NX = 45
LW_var_dz.ComputationalGrid.NY = 32
LW_var_dz.ComputationalGrid.NZ = 25
LW_var_dz.ComputationalGrid.NZ = 10
LW_var_dz.ComputationalGrid.NZ = 6

LW_var_dz.ComputationalGrid.DX = 1000.0
LW_var_dz.ComputationalGrid.DY = 1000.0
#"native" grid resolution is 2m everywhere X NZ=25 for 50m
#computational domain.
LW_var_dz.ComputationalGrid.DZ = 2.0

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
LW_var_dz.GeomInput.Names = 'domaininput'

LW_var_dz.GeomInput.domaininput.GeomName = 'domain'
LW_var_dz.GeomInput.domaininput.InputType = 'Box'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
LW_var_dz.Geom.domain.Lower.X = 0.0
LW_var_dz.Geom.domain.Lower.Y = 0.0
LW_var_dz.Geom.domain.Lower.Z = 0.0

LW_var_dz.Geom.domain.Upper.X = 45000.0
LW_var_dz.Geom.domain.Upper.Y = 32000.0
# this upper is synched to computational grid, not linked w/ Z multipliers
LW_var_dz.Geom.domain.Upper.Z = 12.0
LW_var_dz.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'

#--------------------------------------------
# variable dz assignments
#------------------------------------------
LW_var_dz.Solver.Nonlinear.VariableDz = True
LW_var_dz.dzScale.GeomNames = 'domain'
LW_var_dz.dzScale.Type = 'nzList'
LW_var_dz.dzScale.nzListNumber = 6

#pfset dzScale.Type            nzList
#pfset dzScale.nzListNumber       3
LW_var_dz.Cell.0.dzScale.Value = 1.0
LW_var_dz.Cell.1.dzScale.Value = 1.00
LW_var_dz.Cell.2.dzScale.Value = 1.000
LW_var_dz.Cell.3.dzScale.Value = 1.000
LW_var_dz.Cell.4.dzScale.Value = 1.000
LW_var_dz.Cell.5.dzScale.Value = 0.05

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

LW_var_dz.Geom.Perm.Names = 'domain'

# Values in m/hour


LW_var_dz.Geom.domain.Perm.Type = 'Constant'

LW_var_dz.Geom.domain.Perm.Type = 'TurnBands'
LW_var_dz.Geom.domain.Perm.LambdaX = 5000.0
LW_var_dz.Geom.domain.Perm.LambdaY = 5000.0
LW_var_dz.Geom.domain.Perm.LambdaZ = 50.0
LW_var_dz.Geom.domain.Perm.GeomMean = 0.0001427686

LW_var_dz.Geom.domain.Perm.Sigma = 0.20
LW_var_dz.Geom.domain.Perm.Sigma = 1.20
#pfset Geom.domain.Perm.Sigma   0.48989794
LW_var_dz.Geom.domain.Perm.NumLines = 150
LW_var_dz.Geom.domain.Perm.RZeta = 10.0
LW_var_dz.Geom.domain.Perm.KMax = 100.0000001
LW_var_dz.Geom.domain.Perm.DelK = 0.2
LW_var_dz.Geom.domain.Perm.Seed = 33333
LW_var_dz.Geom.domain.Perm.LogNormal = 'Log'
LW_var_dz.Geom.domain.Perm.StratType = 'Bottom'


LW_var_dz.Perm.TensorType = 'TensorByGeom'

LW_var_dz.Geom.Perm.TensorByGeom.Names = 'domain'

LW_var_dz.Geom.domain.Perm.TensorValX = 1.0d0
LW_var_dz.Geom.domain.Perm.TensorValY = 1.0d0
LW_var_dz.Geom.domain.Perm.TensorValZ = 1.0d0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

LW_var_dz.SpecificStorage.Type = 'Constant'
LW_var_dz.SpecificStorage.GeomNames = 'domain'
LW_var_dz.Geom.domain.SpecificStorage.Value = 1.0e-5
#pfset Geom.domain.SpecificStorage.Value 0.0

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

LW_var_dz.Phase.Names = 'water'

LW_var_dz.Phase.water.Density.Type = 'Constant'
LW_var_dz.Phase.water.Density.Value = 1.0

LW_var_dz.Phase.water.Viscosity.Type = 'Constant'
LW_var_dz.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

LW_var_dz.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

LW_var_dz.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

LW_var_dz.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------
LW_var_dz.TimingInfo.BaseUnit = 10.0
LW_var_dz.TimingInfo.StartCount = 0
LW_var_dz.TimingInfo.StartTime = 0.0
LW_var_dz.TimingInfo.StopTime = 200.0
LW_var_dz.TimingInfo.DumpInterval = 20.0
LW_var_dz.TimeStep.Type = 'Constant'
LW_var_dz.TimeStep.Value = 10.0
#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

LW_var_dz.Geom.Porosity.GeomNames = 'domain'

LW_var_dz.Geom.domain.Porosity.Type = 'Constant'
LW_var_dz.Geom.domain.Porosity.Value = 0.25
#pfset Geom.domain.Porosity.Value         0.


#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

LW_var_dz.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

LW_var_dz.Phase.RelPerm.Type = 'VanGenuchten'
LW_var_dz.Phase.RelPerm.GeomNames = 'domain'

LW_var_dz.Geom.domain.RelPerm.Alpha = 1.
LW_var_dz.Geom.domain.RelPerm.Alpha = 1.0
LW_var_dz.Geom.domain.RelPerm.N = 3.
#pfset Geom.domain.RelPerm.NumSamplePoints   10000
#pfset Geom.domain.RelPerm.MinPressureHead   -200
#pfset Geom.domain.RelPerm.InterpolationMethod   "Linear"
#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

LW_var_dz.Phase.Saturation.Type = 'VanGenuchten'
LW_var_dz.Phase.Saturation.GeomNames = 'domain'

LW_var_dz.Geom.domain.Saturation.Alpha = 1.0
LW_var_dz.Geom.domain.Saturation.Alpha = 1.0
LW_var_dz.Geom.domain.Saturation.N = 3.
LW_var_dz.Geom.domain.Saturation.SRes = 0.1
LW_var_dz.Geom.domain.Saturation.SSat = 1.0



#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
LW_var_dz.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
LW_var_dz.Cycle.Names = 'constant rainrec'
LW_var_dz.Cycle.Names = 'constant'
LW_var_dz.Cycle.constant.Names = 'alltime'
LW_var_dz.Cycle.constant.alltime.Length = 10000000
LW_var_dz.Cycle.constant.Repeat = -1

# rainfall and recession time periods are defined here
# rain for 1 hour, recession for 2 hours

LW_var_dz.Cycle.rainrec.Names = 'rain rec'
LW_var_dz.Cycle.rainrec.rain.Length = 10
LW_var_dz.Cycle.rainrec.rec.Length = 20
LW_var_dz.Cycle.rainrec.Repeat = 14

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
LW_var_dz.BCPressure.PatchNames = [pfget Geom.domain.Patches]

LW_var_dz.Patch.x_lower.BCPressure.Type = 'FluxConst'
LW_var_dz.Patch.x_lower.BCPressure.Cycle = 'constant'
LW_var_dz.Patch.x_lower.BCPressure.alltime.Value = 0.0

LW_var_dz.Patch.y_lower.BCPressure.Type = 'FluxConst'
LW_var_dz.Patch.y_lower.BCPressure.Cycle = 'constant'
LW_var_dz.Patch.y_lower.BCPressure.alltime.Value = 0.0

LW_var_dz.Patch.z_lower.BCPressure.Type = 'FluxConst'
LW_var_dz.Patch.z_lower.BCPressure.Cycle = 'constant'
LW_var_dz.Patch.z_lower.BCPressure.alltime.Value = 0.0

LW_var_dz.Patch.x_upper.BCPressure.Type = 'FluxConst'
LW_var_dz.Patch.x_upper.BCPressure.Cycle = 'constant'
LW_var_dz.Patch.x_upper.BCPressure.alltime.Value = 0.0

LW_var_dz.Patch.y_upper.BCPressure.Type = 'FluxConst'
LW_var_dz.Patch.y_upper.BCPressure.Cycle = 'constant'
LW_var_dz.Patch.y_upper.BCPressure.alltime.Value = 0.0

## overland flow boundary condition with very heavy rainfall
LW_var_dz.Patch.z_upper.BCPressure.Type = 'OverlandFlow'
LW_var_dz.Patch.z_upper.BCPressure.Cycle = 'constant'
# constant recharge at 100 mm / y
LW_var_dz.Patch.z_upper.BCPressure.alltime.Value = -0.005

#---------------
# Copy slopes to working dir
#----------------

# file copy -force input/lw.1km.slope_x.10x.pfb .
# file copy -force input/lw.1km.slope_y.10x.pfb .

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

LW_var_dz.TopoSlopesX.Type = 'PFBFile'
LW_var_dz.TopoSlopesX.GeomNames = 'domain'

LW_var_dz.TopoSlopesX.FileName = 'lw.1km.slope_x.10x.pfb'


#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

LW_var_dz.TopoSlopesY.Type = 'PFBFile'
LW_var_dz.TopoSlopesY.GeomNames = 'domain'

LW_var_dz.TopoSlopesY.FileName = 'lw.1km.slope_y.10x.pfb'

#---------
##  Distribute slopes
#---------

LW_var_dz.ComputationalGrid.NX = 45
LW_var_dz.ComputationalGrid.NY = 32
LW_var_dz.ComputationalGrid.NZ = 6

# Slope files 1D files so distribute with -nz 1
# pfdist -nz 1 lw.1km.slope_x.10x.pfb
# pfdist -nz 1 lw.1km.slope_y.10x.pfb

#---------------------------------------------------------
# Mannings coefficient
#---------------------------------------------------------

LW_var_dz.Mannings.Type = 'Constant'
LW_var_dz.Mannings.GeomNames = 'domain'
LW_var_dz.Mannings.Geom.domain.Value = 0.00005


#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

LW_var_dz.PhaseSources.water.Type = 'Constant'
LW_var_dz.PhaseSources.water.GeomNames = 'domain'
LW_var_dz.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

LW_var_dz.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

LW_var_dz.Solver = 'Richards'
LW_var_dz.Solver.MaxIter = 2500

LW_var_dz.Solver.TerrainFollowingGrid = True


LW_var_dz.Solver.Nonlinear.MaxIter = 80
LW_var_dz.Solver.Nonlinear.ResidualTol = 1e-5
LW_var_dz.Solver.Nonlinear.EtaValue = 0.001


LW_var_dz.Solver.PrintSubsurf = False
LW_var_dz. = 'Solver.Drop 1E_20'
LW_var_dz.Solver.AbsTol = 1E-10


LW_var_dz.Solver.Nonlinear.EtaChoice = 'EtaConstant'
LW_var_dz.Solver.Nonlinear.EtaValue = 0.001
LW_var_dz.Solver.Nonlinear.UseJacobian = True
#pfset Solver.Nonlinear.UseJacobian                       False
LW_var_dz.Solver.Nonlinear.DerivativeEpsilon = 1e-14
LW_var_dz.Solver.Nonlinear.StepTol = 1e-25
LW_var_dz.Solver.Nonlinear.Globalization = 'LineSearch'
LW_var_dz.Solver.Linear.KrylovDimension = 80
LW_var_dz.Solver.Linear.MaxRestarts = 2

LW_var_dz.Solver.Linear.Preconditioner = 'MGSemi'
LW_var_dz.Solver.Linear.Preconditioner = 'PFMG'
LW_var_dz.Solver.Linear.Preconditioner.PCMatrixType = 'FullJacobian'

#pfset Solver.WriteSiloSubsurfData True
#pfset Solver.WriteSiloPressure True
#pfset Solver.WriteSiloSaturation True
#pfset Solver.WriteSiloConcentration True
#pfset Solver.WriteSiloSlopes True
#pfset Solver.WriteSiloMask True

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

# set water table to be at the bottom of the domain, the top layer is initially dry
LW_var_dz.ICPressure.Type = 'HydroStaticPatch'
LW_var_dz.ICPressure.GeomNames = 'domain'
LW_var_dz.Geom.domain.ICPressure.Value = -10.0

LW_var_dz.Geom.domain.ICPressure.RefGeom = 'domain'
LW_var_dz.Geom.domain.ICPressure.RefPatch = 'z_upper'


#spinup key
# True=skim pressures, False = regular (default)
#pfset Solver.Spinup           True
LW_var_dz.Solver.Spinup = False

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

# pfrun $runname
# pfundist $runname
# pfundist lw.1km.slope_x.10x.pfb
# pfundist lw.1km.slope_y.10x.pfb


# source pftest.tcl
passed = 1

# if ![pftestFile $runname.out.perm_x.pfb "Max difference in perm_x" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile $runname.out.perm_y.pfb "Max difference in perm_y" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile $runname.out.perm_z.pfb "Max difference in perm_z" $sig_digits] {
#     set passed 0
# }

# foreach i "00000 00002 00004 00006 00008 00010" {
#     if ![pftestFile $runname.out.press.$i.pfb "Max difference in Pressure for timestep $i" $sig_digits] {
#     set passed 0
# }
#     if ![pftestFile  $runname.out.satur.$i.pfb "Max difference in Saturation for timestep $i" $sig_digits] {
#     set passed 0
# }
# }

# if $passed {
#     puts "LW_var_dz : PASSED"
# } {
#     puts "LW_var_dz : FAILED"
# }




#puts "[exec tail $runname.out.kinsol.log]"
#puts "[exec tail $runname.out.log]"
LW_var_dz.run()
