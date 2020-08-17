# ParFlow-integration/test/python

This directory contains tools for testing Python scripts and examples of the ParFlow
test files converted to Python. The folders divide the tests according to the modules
they require, based on the parflow/test/CMakeLists.txt. The "other" folder holds
tests that additional to the standard ParFlow test suite.

## Folders:

### base

- default_richards_wells.tcl TODO
- forsyth2.tcl
- harvey_flow.tcl
- harvey_flow_pgs.tcl TODO
- crater2D.tcl
- crater2D_vangtable_spline.tcl TODO
- crater2D_vangtable_linear.tcl TODO
- small_domain.tcl TODO
- richards_hydrostatic_equalibrium.tcl TODO
- default_richards_nocluster.tcl TODO
- octree-simple.tcl TODO
- octree-large-domain.tcl TODO
- terrain_following_grid_overland.tcl  TODO
- var_dz_1D.tcl TODO
- pfmg.tcl TODO
- pfmg_galerkin.tcl TODO
- smg.tcl TODO
- pfmg_octree.tcl TODO
- van-genuchten-file.tcl TODO
- overland_slopingslab_KWE.tcl TODO
- overland_tiltedV_KWE.tcl TODO
- overland_slopingslab_DWE.tcl TODO
- overland_tiltedV_DWE.tcl TODO
- overland_FlatICP.tcl TODO
- richards_FBx.tcl TODO
- richards_FBy.tcl TODO
- richards_box_proctest.tcl TODO
- richards_box_proctest.vardz.tcl TODO

### base_2d

- default_overland.tcl
- default_overland.pfmg.jac.tcl TODO
- default_overland.pfmg_octree.jac.tcl TODO
- default_overland.pfmg_octree.fulljac.tcl TODO
- LW_var_dz.tcl NEEDSDIST
- LW_var_dz_spinup.tcl TODO
- overland_slopingslab_KWE.tcl TODO
- richards_box_proctest.vardz.tcl TODO

### base_3d

- default_single.tcl
- default_richards.tcl

### clm

TBD

### clm-samrai

- clm_samrai.tcl TODO

### netcdf

- default_richards_with_netcdf.tcl TODO

### samrai

- samrai_compute_domain.tcl TODO
- samrai.tcl TODO

### silo

- indicator_field NEEDSDIST
- water_balance_y
- water_balance_x
- water_balance_x.hardflow.nojac
- water_balance_x.hardflow.jac
- default_richards_with_silo

### other
