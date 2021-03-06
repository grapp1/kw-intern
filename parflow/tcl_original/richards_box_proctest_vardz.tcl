# This runs a test case with the Richards' solver
# with a simple flow domain and different BCs on the top.
# The domain geometry is purposefully smaller than the computational grid
# making more than 1/2 the domain inactive in Y.  When run with topology
# 1 2 1 this will test PF behavior for inactive processors, for different BCs
# and solver configurations.

set runname richards_ptest_vdz
set tcl_precision 17

# Import the ParFlow TCL package
#
lappend auto_path $env(PARFLOW_DIR)/bin
package require parflow
namespace import Parflow::*

pfset FileVersion 4

pfset Process.Topology.P        [lindex $argv 0]
pfset Process.Topology.Q        [lindex $argv 1]
pfset Process.Topology.R        [lindex $argv 2]

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
pfset ComputationalGrid.Lower.X                 0.0
pfset ComputationalGrid.Lower.Y                 0.0
pfset ComputationalGrid.Lower.Z                 0.0

pfset ComputationalGrid.DX	                    1.0
pfset ComputationalGrid.DY                      1.0
pfset ComputationalGrid.DZ	                    1.0

pfset ComputationalGrid.NX                      20
pfset ComputationalGrid.NY                      50
pfset ComputationalGrid.NZ                      20

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
pfset GeomInput.Names "domain_input"

#---------------------------------------------------------
# Domain Geometry Input
#---------------------------------------------------------
pfset GeomInput.domain_input.InputType            Box
pfset GeomInput.domain_input.GeomName             domain

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
pfset Geom.domain.Lower.X                        0.0
pfset Geom.domain.Lower.Y                        0.0
pfset Geom.domain.Lower.Z                        0.0

pfset Geom.domain.Upper.X                        20.0
pfset Geom.domain.Upper.Y                        20.0
pfset Geom.domain.Upper.Z                        20.0

pfset Geom.domain.Patches "left right front back bottom top"

#--------------------------------------------
# variable dz assignments
#------------------------------------------
pfset Solver.Nonlinear.VariableDz   True
pfset dzScale.GeomNames            domain
pfset dzScale.Type            nzList
pfset dzScale.nzListNumber       20
pfset Cell.0.dzScale.Value 1.0
pfset Cell.1.dzScale.Value 1.0
pfset Cell.2.dzScale.Value 1.0
pfset Cell.3.dzScale.Value 1.0
pfset Cell.4.dzScale.Value 1.0
pfset Cell.5.dzScale.Value 1.0
pfset Cell.6.dzScale.Value 1.0
pfset Cell.7.dzScale.Value 1.0
pfset Cell.8.dzScale.Value 1.0
pfset Cell.9.dzScale.Value 1.0
pfset Cell.10.dzScale.Value 1.0
pfset Cell.11.dzScale.Value 1.0
pfset Cell.12.dzScale.Value 1.0
pfset Cell.13.dzScale.Value 1.0
pfset Cell.14.dzScale.Value 1.0
pfset Cell.15.dzScale.Value 1.0
pfset Cell.16.dzScale.Value 1.0
pfset Cell.17.dzScale.Value 1.0
pfset Cell.18.dzScale.Value 1.0
pfset Cell.19.dzScale.Value 0.05

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

pfset Geom.Perm.Names domain
pfset Geom.domain.Perm.Type     Constant
pfset Geom.domain.Perm.Value    1.0

pfset Perm.TensorType               TensorByGeom

pfset Geom.Perm.TensorByGeom.Names  domain

pfset Geom.domain.Perm.TensorValX  1.0
pfset Geom.domain.Perm.TensorValY  1.0
pfset Geom.domain.Perm.TensorValZ  1.0



#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

pfset SpecificStorage.Type            Constant
pfset SpecificStorage.GeomNames       domain
pfset Geom.domain.SpecificStorage.Value 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

pfset Phase.Names "water"

pfset Phase.water.Density.Type	Constant
pfset Phase.water.Density.Value	1.0

pfset Phase.water.Viscosity.Type	Constant
pfset Phase.water.Viscosity.Value	1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
pfset Contaminants.Names			""

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------
pfset Geom.Retardation.GeomNames           ""

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

pfset Gravity				1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

pfset TimingInfo.BaseUnit     10.
pfset TimingInfo.StartCount    0
pfset TimingInfo.StartTime    0.0
pfset TimingInfo.StopTime      100.0
pfset TimingInfo.DumpInterval   10.0
pfset TimeStep.Type                     Constant
pfset TimeStep.Value                    10.0

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

pfset Geom.Porosity.GeomNames          domain

pfset Geom.domain.Porosity.Type    Constant
pfset Geom.domain.Porosity.Value   0.25

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
pfset Domain.GeomName domain

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

pfset Phase.RelPerm.Type               VanGenuchten
pfset Phase.RelPerm.GeomNames          domain
pfset Geom.domain.RelPerm.Alpha        2.0
pfset Geom.domain.RelPerm.N            2.0

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

pfset Phase.Saturation.Type            VanGenuchten
pfset Phase.Saturation.GeomNames       domain
pfset Geom.domain.Saturation.Alpha     2.0
pfset Geom.domain.Saturation.N         2.0
pfset Geom.domain.Saturation.SRes      0.1
pfset Geom.domain.Saturation.SSat      1.0

#---------------------------------------------------------
# No Flow Barrier
#---------------------------------------------------------

pfset Solver.Nonlinear.FlowBarrierX False


#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
pfset Wells.Names                           ""


#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
pfset Cycle.Names constant
pfset Cycle.constant.Names		"alltime"
pfset Cycle.constant.alltime.Length	 1
pfset Cycle.constant.Repeat		-1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------

pfset BCPressure.PatchNames "left right front back bottom top"

pfset Patch.left.BCPressure.Type			DirEquilRefPatch
pfset Patch.left.BCPressure.Cycle			"constant"
pfset Patch.left.BCPressure.RefGeom			domain
pfset Patch.left.BCPressure.RefPatch			bottom
pfset Patch.left.BCPressure.alltime.Value		11.0

pfset Patch.right.BCPressure.Type			DirEquilRefPatch
pfset Patch.right.BCPressure.Cycle			"constant"
pfset Patch.right.BCPressure.RefGeom			domain
pfset Patch.right.BCPressure.RefPatch			bottom
pfset Patch.right.BCPressure.alltime.Value		15.0

pfset Patch.front.BCPressure.Type			FluxConst
pfset Patch.front.BCPressure.Cycle			"constant"
pfset Patch.front.BCPressure.alltime.Value		0.0

pfset Patch.back.BCPressure.Type			FluxConst
pfset Patch.back.BCPressure.Cycle			"constant"
pfset Patch.back.BCPressure.alltime.Value		0.0

pfset Patch.bottom.BCPressure.Type			FluxConst
pfset Patch.bottom.BCPressure.Cycle			"constant"
pfset Patch.bottom.BCPressure.alltime.Value		0.0

# used to cycle different BCs on the top of the domain, even with no
# overland flow
pfset Patch.top.BCPressure.Type			        FluxConst
pfset Patch.top.BCPressure.Type			        OverlandFlow
pfset Patch.top.BCPressure.Type			        OverlandKinematic
#pfset Patch.top.BCPressure.Type			        SeepageFace
#pfset Patch.top.BCPressure.Type			        OverlandDiffusive

pfset Patch.top.BCPressure.Cycle			"constant"
pfset Patch.top.BCPressure.alltime.Value		0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

pfset TopoSlopesX.Type "Constant"
pfset TopoSlopesX.GeomNames ""

pfset TopoSlopesX.Geom.domain.Value 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

pfset TopoSlopesY.Type "Constant"
pfset TopoSlopesY.GeomNames ""

pfset TopoSlopesY.Geom.domain.Value 0.0

#---------------------------------------------------------
# Mannings coefficient
#---------------------------------------------------------

pfset Mannings.Type "Constant"
pfset Mannings.GeomNames ""
pfset Mannings.Geom.domain.Value 0.

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

pfset ICPressure.Type                                   HydroStaticPatch
pfset ICPressure.GeomNames                              "domain"
pfset Geom.domain.ICPressure.Value                      13.0
pfset Geom.domain.ICPressure.RefGeom                    domain
pfset Geom.domain.ICPressure.RefPatch                   bottom

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

pfset PhaseSources.water.Type                         Constant
pfset PhaseSources.water.GeomNames                    domain
pfset PhaseSources.water.Geom.domain.Value        0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

pfset KnownSolution                                    NoKnownSolution


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------
pfset Solver                                             Richards
pfset Solver.MaxIter                                     50000

pfset Solver.Nonlinear.MaxIter                           100
pfset Solver.Nonlinear.ResidualTol                       1e-7

pfset Solver.Nonlinear.EtaChoice                         EtaConstant
pfset Solver.Nonlinear.EtaValue                          1e-2

# used to test analytical and FD jacobian combinations
pfset Solver.Nonlinear.UseJacobian                       True
#pfset Solver.Nonlinear.UseJacobian                       False

pfset Solver.Nonlinear.DerivativeEpsilon                 1e-14

pfset Solver.Linear.KrylovDimension                      100

# used to test different linear preconditioners

pfset Solver.Linear.Preconditioner                       PFMG
##pfset Solver.Linear.Preconditioner                       PFMGOctree
##pfset Solver.Linear.Preconditioner                       MGSemi
##pfset Solver.Linear.Preconditioner                       SMG

pfset UseClustering False

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------
pfrun $runname
pfundist $runname

#
# Tests
#

source pftest.tcl
set passed 1
foreach i "00000 00001 00002 00003 00004 00005 00006 00007 00008 00009 00010" {
    if ![pftestFile $runname.out.press.$i.pfb "Max difference in Pressure for timestep $i" $sig_digits] {
    set passed 0
}
    if ![pftestFile $runname.out.satur.$i.pfb "Max difference in Saturation for timestep $i" $sig_digits] {
    set passed 0
}
}
if $passed {
    puts "$runname : PASSED"
} {
    puts "$runname : FAILED"
}
