#  This runs the basic pfmg test case based off of default richards

#
# Import the ParFlow TCL package
#
from parflow import Run
samrai_compute_domain = Run("samrai_compute_domain", __file__)

samrai_compute_domain.FileVersion = 4

P = [lindex $argv 0]
Q = [lindex $argv 1]
R = [lindex $argv 2]

NumPatches = [lindex $argv 3]

samrai_compute_domain.Process.Topology.P = P
samrai_compute_domain.Process.Topology.Q = Q
samrai_compute_domain.Process.Topology.R = R

NumProcs = [expr $P * $Q * $R]

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
samrai_compute_domain.ComputationalGrid.Lower.X = -10.0
samrai_compute_domain.ComputationalGrid.Lower.Y = 10.0
samrai_compute_domain.ComputationalGrid.Lower.Z = 1.0

samrai_compute_domain.ComputationalGrid.DX = 8.8888888888888893
samrai_compute_domain.ComputationalGrid.DY = 10.666666666666666
samrai_compute_domain.ComputationalGrid.DZ = 1.0

samrai_compute_domain.ComputationalGrid.NX = 10
samrai_compute_domain.ComputationalGrid.NY = 10
samrai_compute_domain.ComputationalGrid.NZ = 8

#---------------------------------------------------------
# Processor grid
#---------------------------------------------------------

# Compute grid from existing mask file.
mask = [pfload correct_output/samrai.out.mask.pfb]

top = [pfcomputetop $mask]
bottom = [pfcomputebottom $mask]

domain = [pfcomputedomain $top $bottom]

out = [pfprintdomain $domain]

grid_file = [open samrai_grid.tmp.tcl w]
# puts $grid_file $out
# close $grid_file

# Test 2D domain extraction
domain2d = [pfextract2Ddomain $domain]
out = [pfprintdomain $domain2d]
grid_file = [open samrai_grid2D.tmp.tcl w]
# puts $grid_file $out
# close $grid_file

# Note we could execute out stuff directly but put it in a file
# for debugging reasons.

# source samrai_grid.tmp.tcl

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
samrai_compute_domain.GeomInput.Names = 'domain_input background_input source_region_input \'
# 		       concen_region_input"


#---------------------------------------------------------
# Domain Geometry Input
#---------------------------------------------------------
samrai_compute_domain.GeomInput.domain_input.InputType = 'Box'
samrai_compute_domain.GeomInput.domain_input.GeomName = 'domain'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
samrai_compute_domain.Geom.domain.Lower.X = -10.0
samrai_compute_domain.Geom.domain.Lower.Y = 10.0
samrai_compute_domain.Geom.domain.Lower.Z = 1.0

samrai_compute_domain.Geom.domain.Upper.X = 150.0
samrai_compute_domain.Geom.domain.Upper.Y = 170.0
samrai_compute_domain.Geom.domain.Upper.Z = 9.0

samrai_compute_domain.Geom.domain.Patches = 'left right front back bottom top'

#---------------------------------------------------------
# Background Geometry Input
#---------------------------------------------------------
samrai_compute_domain.GeomInput.background_input.InputType = 'Box'
samrai_compute_domain.GeomInput.background_input.GeomName = 'background'

#---------------------------------------------------------
# Background Geometry
#---------------------------------------------------------
samrai_compute_domain.Geom.background.Lower.X = -99999999.0
samrai_compute_domain.Geom.background.Lower.Y = -99999999.0
samrai_compute_domain.Geom.background.Lower.Z = -99999999.0

samrai_compute_domain.Geom.background.Upper.X = 99999999.0
samrai_compute_domain.Geom.background.Upper.Y = 99999999.0
samrai_compute_domain.Geom.background.Upper.Z = 99999999.0


#---------------------------------------------------------
# Source_Region Geometry Input
#---------------------------------------------------------
samrai_compute_domain.GeomInput.source_region_input.InputType = 'Box'
samrai_compute_domain.GeomInput.source_region_input.GeomName = 'source_region'

#---------------------------------------------------------
# Source_Region Geometry
#---------------------------------------------------------
samrai_compute_domain.Geom.source_region.Lower.X = 65.56
samrai_compute_domain.Geom.source_region.Lower.Y = 79.34
samrai_compute_domain.Geom.source_region.Lower.Z = 4.5

samrai_compute_domain.Geom.source_region.Upper.X = 74.44
samrai_compute_domain.Geom.source_region.Upper.Y = 89.99
samrai_compute_domain.Geom.source_region.Upper.Z = 5.5


#---------------------------------------------------------
# Concen_Region Geometry Input
#---------------------------------------------------------
samrai_compute_domain.GeomInput.concen_region_input.InputType = 'Box'
samrai_compute_domain.GeomInput.concen_region_input.GeomName = 'concen_region'

#---------------------------------------------------------
# Concen_Region Geometry
#---------------------------------------------------------
samrai_compute_domain.Geom.concen_region.Lower.X = 60.0
samrai_compute_domain.Geom.concen_region.Lower.Y = 80.0
samrai_compute_domain.Geom.concen_region.Lower.Z = 4.0

samrai_compute_domain.Geom.concen_region.Upper.X = 80.0
samrai_compute_domain.Geom.concen_region.Upper.Y = 100.0
samrai_compute_domain.Geom.concen_region.Upper.Z = 6.0

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
samrai_compute_domain.Geom.Perm.Names = 'background'

samrai_compute_domain.Geom.background.Perm.Type = 'Constant'
samrai_compute_domain.Geom.background.Perm.Value = 4.0

samrai_compute_domain.Perm.TensorType = 'TensorByGeom'

samrai_compute_domain.Geom.Perm.TensorByGeom.Names = 'background'

samrai_compute_domain.Geom.background.Perm.TensorValX = 1.0
samrai_compute_domain.Geom.background.Perm.TensorValY = 1.0
samrai_compute_domain.Geom.background.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

samrai_compute_domain.SpecificStorage.Type = 'Constant'
samrai_compute_domain.SpecificStorage.GeomNames = 'domain'
samrai_compute_domain.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

samrai_compute_domain.Phase.Names = 'water'

samrai_compute_domain.Phase.water.Density.Type = 'Constant'
samrai_compute_domain.Phase.water.Density.Value = 1.0

samrai_compute_domain.Phase.water.Viscosity.Type = 'Constant'
samrai_compute_domain.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
samrai_compute_domain.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------
samrai_compute_domain.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

samrai_compute_domain.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

samrai_compute_domain.TimingInfo.BaseUnit = 1.0
samrai_compute_domain.TimingInfo.StartCount = 0
samrai_compute_domain.TimingInfo.StartTime = 0.0
samrai_compute_domain.TimingInfo.StopTime = 0.010
samrai_compute_domain.TimingInfo.DumpInterval = -1
samrai_compute_domain.TimeStep.Type = 'Constant'
samrai_compute_domain.TimeStep.Value = 0.001

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

samrai_compute_domain.Geom.Porosity.GeomNames = 'background'

samrai_compute_domain.Geom.background.Porosity.Type = 'Constant'
samrai_compute_domain.Geom.background.Porosity.Value = 1.0

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
samrai_compute_domain.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

samrai_compute_domain.Phase.RelPerm.Type = 'VanGenuchten'
samrai_compute_domain.Phase.RelPerm.GeomNames = 'domain'
samrai_compute_domain.Geom.domain.RelPerm.Alpha = 0.005
samrai_compute_domain.Geom.domain.RelPerm.N = 2.0

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

samrai_compute_domain.Phase.Saturation.Type = 'VanGenuchten'
samrai_compute_domain.Phase.Saturation.GeomNames = 'domain'
samrai_compute_domain.Geom.domain.Saturation.Alpha = 0.005
samrai_compute_domain.Geom.domain.Saturation.N = 2.0
samrai_compute_domain.Geom.domain.Saturation.SRes = 0.2
samrai_compute_domain.Geom.domain.Saturation.SSat = 0.99

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
samrai_compute_domain.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
samrai_compute_domain.Cycle.Names = 'constant'
samrai_compute_domain.Cycle.constant.Names = 'alltime'
samrai_compute_domain.Cycle.constant.alltime.Length = 1
samrai_compute_domain.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
samrai_compute_domain.BCPressure.PatchNames = 'left right front back bottom top'

samrai_compute_domain.Patch.left.BCPressure.Type = 'DirEquilRefPatch'
samrai_compute_domain.Patch.left.BCPressure.Cycle = 'constant'
samrai_compute_domain.Patch.left.BCPressure.RefGeom = 'domain'
samrai_compute_domain.Patch.left.BCPressure.RefPatch = 'bottom'
samrai_compute_domain.Patch.left.BCPressure.alltime.Value = 5.0

samrai_compute_domain.Patch.right.BCPressure.Type = 'DirEquilRefPatch'
samrai_compute_domain.Patch.right.BCPressure.Cycle = 'constant'
samrai_compute_domain.Patch.right.BCPressure.RefGeom = 'domain'
samrai_compute_domain.Patch.right.BCPressure.RefPatch = 'bottom'
samrai_compute_domain.Patch.right.BCPressure.alltime.Value = 3.0

samrai_compute_domain.Patch.front.BCPressure.Type = 'FluxConst'
samrai_compute_domain.Patch.front.BCPressure.Cycle = 'constant'
samrai_compute_domain.Patch.front.BCPressure.alltime.Value = 0.0

samrai_compute_domain.Patch.back.BCPressure.Type = 'FluxConst'
samrai_compute_domain.Patch.back.BCPressure.Cycle = 'constant'
samrai_compute_domain.Patch.back.BCPressure.alltime.Value = 0.0

samrai_compute_domain.Patch.bottom.BCPressure.Type = 'FluxConst'
samrai_compute_domain.Patch.bottom.BCPressure.Cycle = 'constant'
samrai_compute_domain.Patch.bottom.BCPressure.alltime.Value = 0.0

samrai_compute_domain.Patch.top.BCPressure.Type = 'FluxConst'
samrai_compute_domain.Patch.top.BCPressure.Cycle = 'constant'
samrai_compute_domain.Patch.top.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

samrai_compute_domain.TopoSlopesX.Type = 'Constant'
samrai_compute_domain.TopoSlopesX.GeomNames = ''

samrai_compute_domain.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

samrai_compute_domain.TopoSlopesY.Type = 'Constant'
samrai_compute_domain.TopoSlopesY.GeomNames = ''

samrai_compute_domain.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

samrai_compute_domain.Mannings.Type = 'Constant'
samrai_compute_domain.Mannings.GeomNames = ''
samrai_compute_domain.Mannings.Geom.domain.Value = 0.

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

samrai_compute_domain.ICPressure.Type = 'HydroStaticPatch'
samrai_compute_domain.ICPressure.GeomNames = 'domain'
samrai_compute_domain.Geom.domain.ICPressure.Value = 3.0
samrai_compute_domain.Geom.domain.ICPressure.RefGeom = 'domain'
samrai_compute_domain.Geom.domain.ICPressure.RefPatch = 'bottom'

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

samrai_compute_domain.PhaseSources.water.Type = 'Constant'
samrai_compute_domain.PhaseSources.water.GeomNames = 'background'
samrai_compute_domain.PhaseSources.water.Geom.background.Value = 0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

samrai_compute_domain.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------
samrai_compute_domain.Solver = 'Richards'
samrai_compute_domain.Solver.MaxIter = 5

samrai_compute_domain.Solver.Nonlinear.MaxIter = 10
samrai_compute_domain.Solver.Nonlinear.ResidualTol = 1e-9
samrai_compute_domain.Solver.Nonlinear.EtaChoice = 'EtaConstant'
samrai_compute_domain.Solver.Nonlinear.EtaValue = 1e-5
samrai_compute_domain.Solver.Nonlinear.UseJacobian = True
samrai_compute_domain.Solver.Nonlinear.DerivativeEpsilon = 1e-2

samrai_compute_domain.Solver.Linear.KrylovDimension = 10

samrai_compute_domain.Solver.Linear.Preconditioner = 'PFMGOctree'

samrai_compute_domain.Solver.Linear.Preconditioner.PFMGOctree.BoxSizePowerOf2 = 2

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
samrai_compute_domain.run()
