#  This runs the basic pfmg test case based off of default richards
#  This run, as written in this input file, should take
#  3 nonlinear iterations.

#
# Import the ParFlow TCL package
#
from parflow import Run
samrai = Run("samrai", __file__)

samrai.FileVersion = 4

P = [lindex $argv 0]
Q = [lindex $argv 1]
R = [lindex $argv 2]

NumPatches = [lindex $argv 3]

samrai.Process.Topology.P = P
samrai.Process.Topology.Q = Q
samrai.Process.Topology.R = R

NumProcs = [expr $P * $Q * $R]

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
samrai.ComputationalGrid.Lower.X = -10.0
samrai.ComputationalGrid.Lower.Y = 10.0
samrai.ComputationalGrid.Lower.Z = 1.0

samrai.ComputationalGrid.DX = 8.8888888888888893
samrai.ComputationalGrid.DY = 10.666666666666666
samrai.ComputationalGrid.DZ = 1.0

samrai.ComputationalGrid.NX = 10
samrai.ComputationalGrid.NY = 10
samrai.ComputationalGrid.NZ = 8

#---------------------------------------------------------
# Processor grid
#---------------------------------------------------------
# if {[expr $NumProcs == 1]} {
#     if {[expr $NumPatches == 1]} {
# 	# {ix = 0, iy = 0, iz = 0, nx = 10, ny = 10, nz = 8, sx = 1, sy = 1, sz = 1, rx = 0, ry = 0, rz = 0, level = 0, process = 0}

# 	
# 	pfset ProcessGrid.NumSubgrids 1
# 	pfset ProcessGrid.0.P 0
# 	pfset ProcessGrid.0.IX 0
# 	pfset ProcessGrid.0.IY 0
# 	pfset ProcessGrid.0.IZ 0
# 	
# 	pfset ProcessGrid.0.NX 10
# 	pfset ProcessGrid.0.NY 10
# 	pfset ProcessGrid.0.NZ 8
#     } elseif {[expr $NumPatches == 2]} {
# 	# {ix = 0, iy = 0, iz = 0, nx = 10, ny = 5, nz = 8, sx = 1, sy = 1, sz = 1, rx = 0, ry = 0, rz = 0, level = 0, process = 0}
# 	# {ix = 0, iy = 5, iz = 0, nx = 10, ny = 5, nz = 8, sx = 1, sy = 1, sz = 1, rx = 0, ry = 0, rz = 0, level = 0, process = 1}
# 	
# 	pfset ProcessGrid.NumSubgrids 2
# 	pfset ProcessGrid.0.P 0
# 	pfset ProcessGrid.0.IX 0
# 	pfset ProcessGrid.0.IY 0
# 	pfset ProcessGrid.0.IZ 0
# 	
# 	pfset ProcessGrid.0.NX 10
# 	pfset ProcessGrid.0.NY 5
# 	pfset ProcessGrid.0.NZ 8
# 	
# 	pfset ProcessGrid.1.P 0
# 	pfset ProcessGrid.1.IX 0
# 	pfset ProcessGrid.1.IY 5
# 	pfset ProcessGrid.1.IZ 0
# 	
# 	pfset ProcessGrid.1.NX 10
# 	pfset ProcessGrid.1.NY 5
# 	pfset ProcessGrid.1.NZ 8
#     } elseif {[expr $NumPatches == 3]} {
# 	
# 	pfset ProcessGrid.NumSubgrids 3
# 	pfset ProcessGrid.0.P 0
# 	pfset ProcessGrid.0.IX 0
# 	pfset ProcessGrid.0.IY 0
# 	pfset ProcessGrid.0.IZ 0
# 	pfset ProcessGrid.0.NX 5
# 	pfset ProcessGrid.0.NY 5
# 	pfset ProcessGrid.0.NZ 8
# 	
# 	pfset ProcessGrid.1.P 0
# 	pfset ProcessGrid.1.IX 0
# 	pfset ProcessGrid.1.IY 5
# 	pfset ProcessGrid.1.IZ 0
# 	pfset ProcessGrid.1.NX 5
# 	pfset ProcessGrid.1.NY 5
# 	pfset ProcessGrid.1.NZ 8

# 	pfset ProcessGrid.2.P 0
# 	pfset ProcessGrid.2.IX 5
# 	pfset ProcessGrid.2.IY 0
# 	pfset ProcessGrid.2.IZ 0
# 	pfset ProcessGrid.2.NX 5
# 	pfset ProcessGrid.2.NY 10
# 	pfset ProcessGrid.2.NZ 8
#     } else {
# 	puts "Invalid processor/number of subgrid option"
# 	exit
#     }
# } elseif {[expr $NumProcs == 2]} {

#     if {[expr $NumPatches == 2]} {
# 	
# 	pfset ProcessGrid.NumSubgrids 2
# 	pfset ProcessGrid.0.P 0
# 	pfset ProcessGrid.0.IX 0
# 	pfset ProcessGrid.0.IY 0
# 	pfset ProcessGrid.0.IZ 0
# 	pfset ProcessGrid.0.NX 10
# 	pfset ProcessGrid.0.NY 5
# 	pfset ProcessGrid.0.NZ 8
# 	
# 	pfset ProcessGrid.1.P 1
# 	pfset ProcessGrid.1.IX 0
# 	pfset ProcessGrid.1.IY 5
# 	pfset ProcessGrid.1.IZ 0
# 	pfset ProcessGrid.1.NX 10
# 	pfset ProcessGrid.1.NY 5
# 	pfset ProcessGrid.1.NZ 8

#     } elseif {[expr $NumPatches == 3]} {
# 	
# 	pfset ProcessGrid.NumSubgrids 3
# 	pfset ProcessGrid.0.P 0
# 	pfset ProcessGrid.0.IX 0
# 	pfset ProcessGrid.0.IY 0
# 	pfset ProcessGrid.0.IZ 0
# 	pfset ProcessGrid.0.NX 5
# 	pfset ProcessGrid.0.NY 5
# 	pfset ProcessGrid.0.NZ 8
# 	
# 	pfset ProcessGrid.1.P 0
# 	pfset ProcessGrid.1.IX 0
# 	pfset ProcessGrid.1.IY 5
# 	pfset ProcessGrid.1.IZ 0
# 	pfset ProcessGrid.1.NX 5
# 	pfset ProcessGrid.1.NY 5
# 	pfset ProcessGrid.1.NZ 8

# 	pfset ProcessGrid.2.P 1
# 	pfset ProcessGrid.2.IX 5
# 	pfset ProcessGrid.2.IY 0
# 	pfset ProcessGrid.2.IZ 0
# 	pfset ProcessGrid.2.NX 5
# 	pfset ProcessGrid.2.NY 10
# 	pfset ProcessGrid.2.NZ 8
#     } elseif {[expr $NumPatches == 4]} {
# 	pfset ProcessGrid.NumSubgrids 4
# 	pfset ProcessGrid.0.P 0
# 	pfset ProcessGrid.0.IX 0
# 	pfset ProcessGrid.0.IY 0
# 	pfset ProcessGrid.0.IZ 0
# 	pfset ProcessGrid.0.NX 5
# 	pfset ProcessGrid.0.NY 5
# 	pfset ProcessGrid.0.NZ 8
# 	
# 	pfset ProcessGrid.1.P 0
# 	pfset ProcessGrid.1.IX 0
# 	pfset ProcessGrid.1.IY 5
# 	pfset ProcessGrid.1.IZ 0
# 	pfset ProcessGrid.1.NX 5
# 	pfset ProcessGrid.1.NY 5
# 	pfset ProcessGrid.1.NZ 8

# 	pfset ProcessGrid.2.P 1
# 	pfset ProcessGrid.2.IX 5
# 	pfset ProcessGrid.2.IY 0
# 	pfset ProcessGrid.2.IZ 0
# 	pfset ProcessGrid.2.NX 5
# 	pfset ProcessGrid.2.NY 5
# 	pfset ProcessGrid.2.NZ 8


# 	pfset ProcessGrid.3.P 1
# 	pfset ProcessGrid.3.IX 5
# 	pfset ProcessGrid.3.IY 5
# 	pfset ProcessGrid.3.IZ 0
# 	pfset ProcessGrid.3.NX 5
# 	pfset ProcessGrid.3.NY 5
# 	pfset ProcessGrid.3.NZ 8
#     } else {

# 	puts "Invalid processor/number of subgrid option"
# 	exit
#     }
# } else {
#     puts "Invalid processor/number of subgrid option"
#     exit
# }

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
samrai.GeomInput.Names = 'domain_input background_input source_region_input \'
# 		       concen_region_input"


#---------------------------------------------------------
# Domain Geometry Input
#---------------------------------------------------------
samrai.GeomInput.domain_input.InputType = 'Box'
samrai.GeomInput.domain_input.GeomName = 'domain'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
samrai.Geom.domain.Lower.X = -10.0
samrai.Geom.domain.Lower.Y = 10.0
samrai.Geom.domain.Lower.Z = 1.0

samrai.Geom.domain.Upper.X = 150.0
samrai.Geom.domain.Upper.Y = 170.0
samrai.Geom.domain.Upper.Z = 9.0

samrai.Geom.domain.Patches = 'left right front back bottom top'

#---------------------------------------------------------
# Background Geometry Input
#---------------------------------------------------------
samrai.GeomInput.background_input.InputType = 'Box'
samrai.GeomInput.background_input.GeomName = 'background'

#---------------------------------------------------------
# Background Geometry
#---------------------------------------------------------
samrai.Geom.background.Lower.X = -99999999.0
samrai.Geom.background.Lower.Y = -99999999.0
samrai.Geom.background.Lower.Z = -99999999.0

samrai.Geom.background.Upper.X = 99999999.0
samrai.Geom.background.Upper.Y = 99999999.0
samrai.Geom.background.Upper.Z = 99999999.0


#---------------------------------------------------------
# Source_Region Geometry Input
#---------------------------------------------------------
samrai.GeomInput.source_region_input.InputType = 'Box'
samrai.GeomInput.source_region_input.GeomName = 'source_region'

#---------------------------------------------------------
# Source_Region Geometry
#---------------------------------------------------------
samrai.Geom.source_region.Lower.X = 65.56
samrai.Geom.source_region.Lower.Y = 79.34
samrai.Geom.source_region.Lower.Z = 4.5

samrai.Geom.source_region.Upper.X = 74.44
samrai.Geom.source_region.Upper.Y = 89.99
samrai.Geom.source_region.Upper.Z = 5.5


#---------------------------------------------------------
# Concen_Region Geometry Input
#---------------------------------------------------------
samrai.GeomInput.concen_region_input.InputType = 'Box'
samrai.GeomInput.concen_region_input.GeomName = 'concen_region'

#---------------------------------------------------------
# Concen_Region Geometry
#---------------------------------------------------------
samrai.Geom.concen_region.Lower.X = 60.0
samrai.Geom.concen_region.Lower.Y = 80.0
samrai.Geom.concen_region.Lower.Z = 4.0

samrai.Geom.concen_region.Upper.X = 80.0
samrai.Geom.concen_region.Upper.Y = 100.0
samrai.Geom.concen_region.Upper.Z = 6.0

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
samrai.Geom.Perm.Names = 'background'

samrai.Geom.background.Perm.Type = 'Constant'
samrai.Geom.background.Perm.Value = 4.0

samrai.Perm.TensorType = 'TensorByGeom'

samrai.Geom.Perm.TensorByGeom.Names = 'background'

samrai.Geom.background.Perm.TensorValX = 1.0
samrai.Geom.background.Perm.TensorValY = 1.0
samrai.Geom.background.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

samrai.SpecificStorage.Type = 'Constant'
samrai.SpecificStorage.GeomNames = 'domain'
samrai.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

samrai.Phase.Names = 'water'

samrai.Phase.water.Density.Type = 'Constant'
samrai.Phase.water.Density.Value = 1.0

samrai.Phase.water.Viscosity.Type = 'Constant'
samrai.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
samrai.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------
samrai.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

samrai.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

samrai.TimingInfo.BaseUnit = 1.0
samrai.TimingInfo.StartCount = 0
samrai.TimingInfo.StartTime = 0.0
samrai.TimingInfo.StopTime = 0.010
samrai.TimingInfo.DumpInterval = -1
samrai.TimeStep.Type = 'Constant'
samrai.TimeStep.Value = 0.001

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

samrai.Geom.Porosity.GeomNames = 'background'

samrai.Geom.background.Porosity.Type = 'Constant'
samrai.Geom.background.Porosity.Value = 1.0

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
samrai.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

samrai.Phase.RelPerm.Type = 'VanGenuchten'
samrai.Phase.RelPerm.GeomNames = 'domain'
samrai.Geom.domain.RelPerm.Alpha = 0.005
samrai.Geom.domain.RelPerm.N = 2.0

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

samrai.Phase.Saturation.Type = 'VanGenuchten'
samrai.Phase.Saturation.GeomNames = 'domain'
samrai.Geom.domain.Saturation.Alpha = 0.005
samrai.Geom.domain.Saturation.N = 2.0
samrai.Geom.domain.Saturation.SRes = 0.2
samrai.Geom.domain.Saturation.SSat = 0.99

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
samrai.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
samrai.Cycle.Names = 'constant'
samrai.Cycle.constant.Names = 'alltime'
samrai.Cycle.constant.alltime.Length = 1
samrai.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
samrai.BCPressure.PatchNames = 'left right front back bottom top'

samrai.Patch.left.BCPressure.Type = 'DirEquilRefPatch'
samrai.Patch.left.BCPressure.Cycle = 'constant'
samrai.Patch.left.BCPressure.RefGeom = 'domain'
samrai.Patch.left.BCPressure.RefPatch = 'bottom'
samrai.Patch.left.BCPressure.alltime.Value = 5.0

samrai.Patch.right.BCPressure.Type = 'DirEquilRefPatch'
samrai.Patch.right.BCPressure.Cycle = 'constant'
samrai.Patch.right.BCPressure.RefGeom = 'domain'
samrai.Patch.right.BCPressure.RefPatch = 'bottom'
samrai.Patch.right.BCPressure.alltime.Value = 3.0

samrai.Patch.front.BCPressure.Type = 'FluxConst'
samrai.Patch.front.BCPressure.Cycle = 'constant'
samrai.Patch.front.BCPressure.alltime.Value = 0.0

samrai.Patch.back.BCPressure.Type = 'FluxConst'
samrai.Patch.back.BCPressure.Cycle = 'constant'
samrai.Patch.back.BCPressure.alltime.Value = 0.0

samrai.Patch.bottom.BCPressure.Type = 'FluxConst'
samrai.Patch.bottom.BCPressure.Cycle = 'constant'
samrai.Patch.bottom.BCPressure.alltime.Value = 0.0

samrai.Patch.top.BCPressure.Type = 'FluxConst'
samrai.Patch.top.BCPressure.Cycle = 'constant'
samrai.Patch.top.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

samrai.TopoSlopesX.Type = 'Constant'
samrai.TopoSlopesX.GeomNames = ''

samrai.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

samrai.TopoSlopesY.Type = 'Constant'
samrai.TopoSlopesY.GeomNames = ''

samrai.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

samrai.Mannings.Type = 'Constant'
samrai.Mannings.GeomNames = ''
samrai.Mannings.Geom.domain.Value = 0.

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

samrai.ICPressure.Type = 'HydroStaticPatch'
samrai.ICPressure.GeomNames = 'domain'
samrai.Geom.domain.ICPressure.Value = 3.0
samrai.Geom.domain.ICPressure.RefGeom = 'domain'
samrai.Geom.domain.ICPressure.RefPatch = 'bottom'

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

samrai.PhaseSources.water.Type = 'Constant'
samrai.PhaseSources.water.GeomNames = 'background'
samrai.PhaseSources.water.Geom.background.Value = 0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

samrai.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------
samrai.Solver = 'Richards'
samrai.Solver.MaxIter = 5

samrai.Solver.Nonlinear.MaxIter = 10
samrai.Solver.Nonlinear.ResidualTol = 1e-9
samrai.Solver.Nonlinear.EtaChoice = 'EtaConstant'
samrai.Solver.Nonlinear.EtaValue = 1e-5
samrai.Solver.Nonlinear.UseJacobian = True
samrai.Solver.Nonlinear.DerivativeEpsilon = 1e-2

samrai.Solver.Linear.KrylovDimension = 10

samrai.Solver.Linear.Preconditioner = 'PFMGOctree'

samrai.Solver.Linear.Preconditioner.PFMGOctree.BoxSizePowerOf2 = 2

#pfset Solver.Linear.Preconditioner.PFMG.MaxIter          1
#pfset Solver.Linear.Preconditioner.PFMG.NumPreRelax      100
#pfset Solver.Linear.Preconditioner.PFMG.NumPostRelax     100
#pfset Solver.Linear.Preconditioner.PFMG.Smoother         100

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------
# pfrun samrai
# pfundist samrai

#
# Tests 
#
# source pftest.tcl
passed = 1

# if ![pftestFile samrai.out.perm_x.pfb "Max difference in perm_x" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile samrai.out.perm_y.pfb "Max difference in perm_y" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile samrai.out.perm_z.pfb "Max difference in perm_z" $sig_digits] {
#     set passed 0
# }

# foreach i "00000 00001 00002 00003 00004 00005" {
#     if ![pftestFile samrai.out.press.$i.pfb "Max difference in Pressure for timestep $i" $sig_digits] {
#     set passed 0
# }
#     if ![pftestFile samrai.out.satur.$i.pfb "Max difference in Saturation for timestep $i" $sig_digits] {
#     set passed 0
# }
# }


# if $passed {
#     puts "samrai : PASSED"
# } {
#     puts "samrai : FAILED"
# }
samrai.run()
