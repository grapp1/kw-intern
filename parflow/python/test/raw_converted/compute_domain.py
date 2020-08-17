#
# Import the ParFlow TCL package
#
from parflow import Run
compute_domain = Run("compute_domain", __file__)

compute_domain.FileVersion = 4

P = [lindex $argv 0]
Q = [lindex $argv 1]
R = [lindex $argv 2]

compute_domain.Process.Topology.P = P
compute_domain.Process.Topology.Q = Q
compute_domain.Process.Topology.R = R

NumProcs = [expr $P * $Q * $R]

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
compute_domain.ComputationalGrid.Lower.X = -10.0
compute_domain.ComputationalGrid.Lower.Y = 10.0
compute_domain.ComputationalGrid.Lower.Z = 1.0

compute_domain.ComputationalGrid.DX = 8.8888888888888893
compute_domain.ComputationalGrid.DY = 10.666666666666666
compute_domain.ComputationalGrid.DZ = 1.0

compute_domain.ComputationalGrid.NX = 10
compute_domain.ComputationalGrid.NY = 10
compute_domain.ComputationalGrid.NZ = 8

mask = [pfload correct_output/samrai.out.mask.pfb]

top = [pfcomputetop $mask]
# pfsave $top -sa "top.sa"

bottom = [pfcomputebottom $mask]
# pfsave $bottom -sa "bottom.sa"

domain = [pfcomputedomain $top $bottom]
# puts $domain

out = [pfprintdomain $domain]

grid_file = [open samrai_grid.tcl w]
# puts $grid_file $out

# file copy correct_output/samrai.out.mask.pfb samrai.out.mask.pfb

# pfdistondomain samrai.out.mask.pfb $domain

# pfundist samrai.out.mask.pfb

# source pftest.tcl
passed = 1

# if ![pftestFile samrai.out.mask.pfb "Max difference in mask" $sig_digits] {
#     set passed 0
# }
compute_domain.run()
