#  This runs the a Little Washita Test Problem with variable dz
#  and a constant rain forcing.  The full Jacobian is use and there is no dampening in the
#  overland flow.

tcl_precision = 17

from parflow import Run
LWvdz = Run("LWvdz", __file__)

LWvdz.FileVersion = 4

LWvdz.Process.Topology.P = 1
LWvdz.Process.Topology.Q = 1
LWvdz.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
LWvdz.ComputationalGrid.Lower.X = 0.0
LWvdz.ComputationalGrid.Lower.Y = 0.0
LWvdz.ComputationalGrid.Lower.Z = 0.0

LWvdz.ComputationalGrid.NX = 45
LWvdz.ComputationalGrid.NY = 32
LWvdz.ComputationalGrid.NZ = 25
LWvdz.ComputationalGrid.NZ = 10
LWvdz.ComputationalGrid.NZ = 6

LWvdz.ComputationalGrid.DX = 1000.0
LWvdz.ComputationalGrid.DY = 1000.0
#"native" grid resolution is 2m everywhere X NZ=25 for 50m
#computational domain.
LWvdz.ComputationalGrid.DZ = 2.0

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
LWvdz.GeomInput.Names = 'domaininput'

LWvdz.GeomInput.domaininput.GeomName = 'domain'
LWvdz.GeomInput.domaininput.InputType = 'Box'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
LWvdz.Geom.domain.Lower.X = 0.0
LWvdz.Geom.domain.Lower.Y = 0.0
LWvdz.Geom.domain.Lower.Z = 0.0

LWvdz.Geom.domain.Upper.X = 45000.0
LWvdz.Geom.domain.Upper.Y = 32000.0
# this upper is synched to computational grid, not linked w/ Z multipliers
LWvdz.Geom.domain.Upper.Z = 12.0
LWvdz.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'

#--------------------------------------------
# variable dz assignments
#------------------------------------------
LWvdz.Solver.Nonlinear.VariableDz = True
LWvdz.dzScale.GeomNames = 'domain'
LWvdz.dzScale.Type = 'nzList'
LWvdz.dzScale.nzListNumber = 6

#pfset dzScale.Type            nzList
#pfset dzScale.nzListNumber       3
LWvdz.Cell.l0.dzScale.Value = 1.0
LWvdz.Cell.l1.dzScale.Value = 1.00
LWvdz.Cell.l2.dzScale.Value = 1.000
LWvdz.Cell.l3.dzScale.Value = 1.000
LWvdz.Cell.l4.dzScale.Value = 1.000
LWvdz.Cell.l5.dzScale.Value = 0.05

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

LWvdz.Geom.Perm.Names = 'domain'

# Values in m/hour


LWvdz.Geom.domain.Perm.Type = 'Constant'

LWvdz.Geom.domain.Perm.Type = 'TurnBands'
LWvdz.Geom.domain.Perm.LambdaX = 5000.0
LWvdz.Geom.domain.Perm.LambdaY = 5000.0
LWvdz.Geom.domain.Perm.LambdaZ = 50.0
LWvdz.Geom.domain.Perm.GeomMean = 0.0001427686

LWvdz.Geom.domain.Perm.Sigma = 0.20
LWvdz.Geom.domain.Perm.Sigma = 1.20
#pfset Geom.domain.Perm.Sigma   0.48989794
LWvdz.Geom.domain.Perm.NumLines = 150
LWvdz.Geom.domain.Perm.RZeta = 10.0
LWvdz.Geom.domain.Perm.KMax = 100.0000001
LWvdz.Geom.domain.Perm.DelK = 0.2
LWvdz.Geom.domain.Perm.Seed = 33333
LWvdz.Geom.domain.Perm.LogNormal = 'Log'
LWvdz.Geom.domain.Perm.StratType = 'Bottom'


LWvdz.Perm.TensorType = 'TensorByGeom'

LWvdz.Geom.Perm.TensorByGeom.Names = 'domain'

LWvdz.Geom.domain.Perm.TensorValX = 1.0
LWvdz.Geom.domain.Perm.TensorValY = 1.0
LWvdz.Geom.domain.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

LWvdz.SpecificStorage.Type = 'Constant'
LWvdz.SpecificStorage.GeomNames = 'domain'
LWvdz.Geom.domain.SpecificStorage.Value = 1.0e-5
#pfset Geom.domain.SpecificStorage.Value 0.0

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

LWvdz.Phase.Names = 'water'

LWvdz.Phase.water.Density.Type = 'Constant'
LWvdz.Phase.water.Density.Value = 1.0

LWvdz.Phase.water.Viscosity.Type = 'Constant'
LWvdz.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

LWvdz.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

LWvdz.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

LWvdz.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------
LWvdz.TimingInfo.BaseUnit = 10.0
LWvdz.TimingInfo.StartCount = 0
LWvdz.TimingInfo.StartTime = 0.0
LWvdz.TimingInfo.StopTime = 200.0
LWvdz.TimingInfo.DumpInterval = 20.0
LWvdz.TimeStep.Type = 'Constant'
LWvdz.TimeStep.Value = 10.0
#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

LWvdz.Geom.Porosity.GeomNames = 'domain'

LWvdz.Geom.domain.Porosity.Type = 'Constant'
LWvdz.Geom.domain.Porosity.Value = 0.25
#pfset Geom.domain.Porosity.Value         0.


#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

LWvdz.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

LWvdz.Phase.RelPerm.Type = 'VanGenuchten'
LWvdz.Phase.RelPerm.GeomNames = 'domain'

LWvdz.Geom.domain.RelPerm.Alpha = 1.
LWvdz.Geom.domain.RelPerm.Alpha = 1.0
LWvdz.Geom.domain.RelPerm.N = 3.
#pfset Geom.domain.RelPerm.NumSamplePoints   10000
#pfset Geom.domain.RelPerm.MinPressureHead   -200
#pfset Geom.domain.RelPerm.InterpolationMethod   "Linear"
#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

LWvdz.Phase.Saturation.Type = 'VanGenuchten'
LWvdz.Phase.Saturation.GeomNames = 'domain'

LWvdz.Geom.domain.Saturation.Alpha = 1.0
LWvdz.Geom.domain.Saturation.Alpha = 1.0
LWvdz.Geom.domain.Saturation.N = 3.
LWvdz.Geom.domain.Saturation.SRes = 0.1
LWvdz.Geom.domain.Saturation.SSat = 1.0



#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
LWvdz.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
LWvdz.Cycle.Names = 'constant rainrec'
# LWvdz.Cycle.Names = 'constant'
LWvdz.Cycle.constant.Names = 'alltime'
LWvdz.Cycle.constant.alltime.Length = 10000000
LWvdz.Cycle.constant.Repeat = -1

# rainfall and recession time periods are defined here
# rain for 1 hour, recession for 2 hours

LWvdz.Cycle.rainrec.Names = 'rain rec'
LWvdz.Cycle.rainrec.rain.Length = 10
LWvdz.Cycle.rainrec.rec.Length = 20
LWvdz.Cycle.rainrec.Repeat = 14

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
LWvdz.BCPressure.PatchNames = LWvdz.Geom.domain.Patches

LWvdz.Patch.x_lower.BCPressure.Type = 'FluxConst'
LWvdz.Patch.x_lower.BCPressure.Cycle = 'constant'
LWvdz.Patch.x_lower.BCPressure.alltime.Value = 0.0

LWvdz.Patch.y_lower.BCPressure.Type = 'FluxConst'
LWvdz.Patch.y_lower.BCPressure.Cycle = 'constant'
LWvdz.Patch.y_lower.BCPressure.alltime.Value = 0.0

LWvdz.Patch.z_lower.BCPressure.Type = 'FluxConst'
LWvdz.Patch.z_lower.BCPressure.Cycle = 'constant'
LWvdz.Patch.z_lower.BCPressure.alltime.Value = 0.0

LWvdz.Patch.x_upper.BCPressure.Type = 'FluxConst'
LWvdz.Patch.x_upper.BCPressure.Cycle = 'constant'
LWvdz.Patch.x_upper.BCPressure.alltime.Value = 0.0

LWvdz.Patch.y_upper.BCPressure.Type = 'FluxConst'
LWvdz.Patch.y_upper.BCPressure.Cycle = 'constant'
LWvdz.Patch.y_upper.BCPressure.alltime.Value = 0.0

## overland flow boundary condition with very heavy rainfall
LWvdz.Patch.z_upper.BCPressure.Type = 'OverlandFlow'
LWvdz.Patch.z_upper.BCPressure.Cycle = 'constant'
# constant recharge at 100 mm / y
LWvdz.Patch.z_upper.BCPressure.alltime.Value = -0.005

#---------------
# Copy slopes to working dir
#----------------

# file copy -force input/lw.1km.slope_x.10x.pfb .
# file copy -force input/lw.1km.slope_y.10x.pfb .

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

LWvdz.TopoSlopesX.Type = 'PFBFile'
LWvdz.TopoSlopesX.GeomNames = 'domain'

LWvdz.TopoSlopesX.FileName = 'lw.1km.slope_x.10x.pfb'


#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

LWvdz.TopoSlopesY.Type = 'PFBFile'
LWvdz.TopoSlopesY.GeomNames = 'domain'

LWvdz.TopoSlopesY.FileName = 'lw.1km.slope_y.10x.pfb'

#---------
##  Distribute slopes
#---------

LWvdz.ComputationalGrid.NX = 45
LWvdz.ComputationalGrid.NY = 32
LWvdz.ComputationalGrid.NZ = 6

# Slope files 1D files so distribute with -nz 1
# pfdist -nz 1 lw.1km.slope_x.10x.pfb
# pfdist -nz 1 lw.1km.slope_y.10x.pfb

#---------------------------------------------------------
# Mannings coefficient
#---------------------------------------------------------

LWvdz.Mannings.Type = 'Constant'
LWvdz.Mannings.GeomNames = 'domain'
LWvdz.Mannings.Geom.domain.Value = 0.00005


#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

LWvdz.PhaseSources.water.Type = 'Constant'
LWvdz.PhaseSources.water.GeomNames = 'domain'
LWvdz.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

LWvdz.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

LWvdz.Solver = 'Richards'
LWvdz.Solver.MaxIter = 2500

LWvdz.Solver.TerrainFollowingGrid = True


LWvdz.Solver.Nonlinear.MaxIter = 80
LWvdz.Solver.Nonlinear.ResidualTol = 1e-5
LWvdz.Solver.Nonlinear.EtaValue = 0.001


LWvdz.Solver.PrintSubsurf = False
LWvdz.Solver.Drop = 1E-20
LWvdz.Solver.AbsTol = 1E-10


LWvdz.Solver.Nonlinear.EtaChoice = 'EtaConstant'
LWvdz.Solver.Nonlinear.EtaValue = 0.001
LWvdz.Solver.Nonlinear.UseJacobian = True
#pfset Solver.Nonlinear.UseJacobian                       False
LWvdz.Solver.Nonlinear.DerivativeEpsilon = 1e-14
LWvdz.Solver.Nonlinear.StepTol = 1e-25
LWvdz.Solver.Nonlinear.Globalization = 'LineSearch'
LWvdz.Solver.Linear.KrylovDimension = 80
LWvdz.Solver.Linear.MaxRestarts = 2

LWvdz.Solver.Linear.Preconditioner = 'MGSemi'
LWvdz.Solver.Linear.Preconditioner = 'PFMG'
LWvdz.Solver.Linear.Preconditioner.PCMatrixType = 'FullJacobian'

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
LWvdz.ICPressure.Type = 'HydroStaticPatch'
LWvdz.ICPressure.GeomNames = 'domain'
LWvdz.Geom.domain.ICPressure.Value = -10.0

LWvdz.Geom.domain.ICPressure.RefGeom = 'domain'
LWvdz.Geom.domain.ICPressure.RefPatch = 'z_upper'


#spinup key
# True=skim pressures, False = regular (default)
#pfset Solver.Spinup           True
LWvdz.Solver.Spinup = False

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

LWvdz.run()
