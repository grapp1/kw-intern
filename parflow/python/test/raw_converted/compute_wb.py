
verbose = 1

tcl_precision = 17

DBL_MAX = 3.40282346638528859811704183485e+38
NEG_DBL_MAX = [expr -$DBL_MAX ]

#
# Import the ParFlow TCL package
#
from parflow import Run
compute_wb = Run("compute_wb", __file__)

compute_wb.FileVersion = 4

# if { $::argc != 3 } {
#     puts "Invalid args : <dir> <start_time> <stop_time>"
#     exit -1
# }

dir_new = [lindex $::argv 0]
start = [lindex $::argv 1]
stop = [lindex $::argv 2]

# set runname $dir_new

dir = [pwd]
# cd $dir_new
# set mask [pfload $runname.out.mask.silo]
# set specific_storage [pfload $runname.out.specific_storage.silo]
# set porosity         [pfload $runname.out.porosity.silo]
# cd $dir
top = [pfcomputetop $mask]

prev_total_water_balance = 0.0


# for {set file_num $start} {$file_num <= $stop} {incr file_num} {
#     set total_water_balance 0.0
#     set total_water_in_domain 0.0

#     set dir [pwd]
#     cd $dir_new
#     set file "press"
#     set filename [format "%s.out.%s.%05d.silo" $dir_new $file $file_num]
#     set pressure [pfload $filename $NEG_DBL_MAX]
#     cd $dir

#     set surface_storage [pfsurfacestorage $top $pressure]
#     set total_surface_storage [pfsum $surface_storage]
#     if $verbose {
# 	puts [format "Surface storage\t\t\t\t\t : %.16e" $total_surface_storage]
#     }
#     set total_water_in_domain [expr $total_water_in_domain + $total_surface_storage]


#     set dir [pwd]
#     cd $dir_new
#     set file "satur"
#     set filename [format "%s.out.%s.%05d.silo" $dir_new $file $file_num]
#     set pressure [pfload $filename $NEG_DBL_MAX]
#     cd $dir

#     set dir [pwd]
#     cd $dir_new
#     set filename [format "%s.out.%s.%05d.silo" $dir_new $file $file_num]
#     set saturation [pfload $filename]
#     cd $dir

#     set water_table_depth [pfwatertabledepth $top $saturation]

#     set subsurface_storage [pfsubsurfacestorage $mask $porosity $pressure $saturation $specific_storage]
#     set total_subsurface_storage [pfsum $subsurface_storage]
#     if $verbose {
# 	puts [format "Subsurface storage\t\t\t\t : %.16e" $total_subsurface_storage]
#     }
#     set total_water_in_domain [expr $total_water_in_domain + $total_subsurface_storage]

#     if $verbose {
# 	puts [format "Total water in domain\t\t\t\t : %.16e" $total_water_in_domain]
# 	puts ""
#     }
#     pfdelete $pressure
# }
compute_wb.run()
