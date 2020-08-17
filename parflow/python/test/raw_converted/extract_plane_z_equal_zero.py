
tcl_precision = 17

#
# Import the ParFlow TCL package
#
from parflow import Run
extract_plane_z_equal_zero = Run("extract_plane_z_equal_zero", __file__)

in_filename = [lindex $::argv 0]
out_filename = [lindex $::argv 1]

in_file = [pfload $in_filename]

code = [catch {eval pfgetgrid $in_file} grid]

# Extract grid size information
dimension = [lindex $grid 0]
origin = [lindex $grid 1]
interval = [lindex $grid 2]

nx = [lindex $dimension 0]
ny = [lindex $dimension 1]
nz = [lindex $dimension 2]

x = [lindex $origin 0]
y = [lindex $origin 1]
z = [lindex $origin 2]

dx = [lindex $interval 0]
dy = [lindex $interval 1]
dz = [lindex $interval 2]

z_zero_plane = [pfgetsubbox $in_file 0 0 0 $nx $ny 1]

# pfsave $z_zero_plane -pfb $out_filename

#  


extract_plane_z_equal_zero.run()
