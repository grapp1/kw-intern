# SCRIPT TO RUN LITTLE WASHITA DOMAIN WITH TERRAIN-FOLLOWING GRID
# DETAILS:
# Arugments are 1) runname 2) year

# Import the ParFlow TCL package
lappend   auto_path $env(PARFLOW_DIR)/bin
package   require parflow
namespace import Parflow::*

pfset     FileVersion    4

#-----------------------------------------------------------------------------
# Set Processor topology
#-----------------------------------------------------------------------------
pfset Process.Topology.P 1
pfset Process.Topology.Q 1
pfset Process.Topology.R 1

#-----------------------------------------------------------------------------
# Make a directory for the simulation and copy inputs into it
#-----------------------------------------------------------------------------
cd "../run_dir"

# ParFlow Inputs
file copy -force "../parflow_input/LW.slopex.pfb" .
file copy -force "../parflow_input/LW.slopey.pfb" .
file copy -force "../parflow_input/IndicatorFile_Gleeson.50z.pfb"   .
file copy -force "../parflow_input/press.init.pfb"  .

#CLM Inputs
file copy -force "../clm_input/drv_clmin.dat" .
file copy -force "../clm_input/drv_vegp.dat"  .
file copy -force "../clm_input/drv_vegm.alluv.dat"  .

puts "Files Copied"

#-----------------------------------------------------------------------------
# Computational Grid
#-----------------------------------------------------------------------------
pfset ComputationalGrid.Lower.X           0.0
pfset ComputationalGrid.Lower.Y           0.0
pfset ComputationalGrid.Lower.Z           0.0

pfset ComputationalGrid.DX                1000.0
pfset ComputationalGrid.DY                1000.0
pfset ComputationalGrid.DZ                2.0

pfset ComputationalGrid.NX                41
pfset ComputationalGrid.NY                41
pfset ComputationalGrid.NZ                50


#-----------------------------------------------------------------------------
# Names of the GeomInputs
#-----------------------------------------------------------------------------
pfset GeomInput.Names                     "box_input indi_input"

#-----------------------------------------------------------------------------
# Domain Geometry Input
#-----------------------------------------------------------------------------
pfset GeomInput.box_input.InputType      Box
pfset GeomInput.box_input.GeomName      domain

#-----------------------------------------------------------------------------
# Domain Geometry
#-----------------------------------------------------------------------------
pfset Geom.domain.Lower.X                        0.0
pfset Geom.domain.Lower.Y                        0.0
pfset Geom.domain.Lower.Z                        0.0

pfset Geom.domain.Upper.X                        41000.0
pfset Geom.domain.Upper.Y                        41000.0
pfset Geom.domain.Upper.Z                          100.0
pfset Geom.domain.Patches             "x-lower x-upper y-lower y-upper z-lower z-upper"

#-----------------------------------------------------------------------------
# Indicator Geometry Input
#-----------------------------------------------------------------------------
pfset GeomInput.indi_input.InputType      IndicatorField
pfset GeomInput.indi_input.GeomNames      "s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 g1 g2 g3 g4 g5 g6 g7 g8"
pfset Geom.indi_input.FileName            "IndicatorFile_Gleeson.50z.pfb"

pfset GeomInput.s1.Value                1
pfset GeomInput.s2.Value                2
pfset GeomInput.s3.Value                3
pfset GeomInput.s4.Value                4
pfset GeomInput.s5.Value                5
pfset GeomInput.s6.Value                6
pfset GeomInput.s7.Value                7
pfset GeomInput.s8.Value                8
pfset GeomInput.s9.Value                9
pfset GeomInput.s10.Value               10
pfset GeomInput.s11.Value               11
pfset GeomInput.s12.Value               12
pfset GeomInput.s13.Value               13
pfset GeomInput.g1.Value                21
pfset GeomInput.g2.Value                22
pfset GeomInput.g3.Value                23
pfset GeomInput.g4.Value                24
pfset GeomInput.g5.Value                25
pfset GeomInput.g6.Value                26
pfset GeomInput.g7.Value                27
pfset GeomInput.g8.Value                28

#-----------------------------------------------------------------------------
# Permeability (values in m/hr)
#-----------------------------------------------------------------------------
pfset Geom.Perm.Names                     "domain s1 s2 s3 s4 s5 s6 s7 s8 s9 g2 g3 g6 g8"

pfset Geom.domain.Perm.Type           Constant
pfset Geom.domain.Perm.Value          0.2

pfset Geom.s1.Perm.Type               Constant
pfset Geom.s1.Perm.Value              0.269022595

pfset Geom.s2.Perm.Type               Constant
pfset Geom.s2.Perm.Value              0.043630356

pfset Geom.s3.Perm.Type               Constant
pfset Geom.s3.Perm.Value              0.015841225

pfset Geom.s4.Perm.Type               Constant
pfset Geom.s4.Perm.Value              0.007582087

pfset Geom.s5.Perm.Type               Constant
pfset Geom.s5.Perm.Value              0.01818816

pfset Geom.s6.Perm.Type               Constant
pfset Geom.s6.Perm.Value              0.005009435

pfset Geom.s7.Perm.Type               Constant
pfset Geom.s7.Perm.Value              0.005492736

pfset Geom.s8.Perm.Type               Constant
pfset Geom.s8.Perm.Value              0.004675077

pfset Geom.s9.Perm.Type               Constant
pfset Geom.s9.Perm.Value              0.003386794

pfset Geom.g2.Perm.Type               Constant
pfset Geom.g2.Perm.Value              0.025

pfset Geom.g3.Perm.Type               Constant
pfset Geom.g3.Perm.Value              0.059

pfset Geom.g6.Perm.Type               Constant
pfset Geom.g6.Perm.Value              0.2

pfset Geom.g8.Perm.Type              Constant
pfset Geom.g8.Perm.Value             0.68

pfset Perm.TensorType                     TensorByGeom
pfset Geom.Perm.TensorByGeom.Names        "domain"
pfset Geom.domain.Perm.TensorValX         1.0d0
pfset Geom.domain.Perm.TensorValY         1.0d0
pfset Geom.domain.Perm.TensorValZ         1.0d0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------
pfset SpecificStorage.Type                Constant
pfset SpecificStorage.GeomNames           "domain"
pfset Geom.domain.SpecificStorage.Value   1.0e-5

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------
pfset Phase.Names                         "water"
pfset Phase.water.Density.Type            Constant
pfset Phase.water.Density.Value           1.0
pfset Phase.water.Viscosity.Type          Constant
pfset Phase.water.Viscosity.Value         1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
pfset Contaminants.Names                  ""

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------
pfset Gravity                             1.0

#-----------------------------------------------------------------------------
# Timing (time units is set by units of permeability)
#-----------------------------------------------------------------------------
pfset TimingInfo.BaseUnit                 1.0
pfset TimingInfo.StartCount               0.0
pfset TimingInfo.StartTime                0.0
pfset TimingInfo.StopTime                 24.0
pfset TimingInfo.DumpInterval             1.0
pfset TimeStep.Type                       Constant
pfset TimeStep.Value                      1.0

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------
pfset Geom.Porosity.GeomNames             "domain s1 s2 s3 s4 s5 s6 s7 s8 s9"

pfset Geom.domain.Porosity.Type          Constant
pfset Geom.domain.Porosity.Value         0.4

pfset Geom.s1.Porosity.Type    Constant
pfset Geom.s1.Porosity.Value   0.375

pfset Geom.s2.Porosity.Type    Constant
pfset Geom.s2.Porosity.Value   0.39

pfset Geom.s3.Porosity.Type    Constant
pfset Geom.s3.Porosity.Value   0.387

pfset Geom.s4.Porosity.Type    Constant
pfset Geom.s4.Porosity.Value   0.439

pfset Geom.s5.Porosity.Type    Constant
pfset Geom.s5.Porosity.Value   0.489

pfset Geom.s6.Porosity.Type    Constant
pfset Geom.s6.Porosity.Value   0.399

pfset Geom.s7.Porosity.Type    Constant
pfset Geom.s7.Porosity.Value   0.384

pfset Geom.s8.Porosity.Type            Constant
pfset Geom.s8.Porosity.Value           0.482

pfset Geom.s9.Porosity.Type            Constant
pfset Geom.s9.Porosity.Value           0.442

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
pfset Domain.GeomName                     "domain"

#----------------------------------------------------------------------------
# Mobility
#----------------------------------------------------------------------------
pfset Phase.water.Mobility.Type        Constant
pfset Phase.water.Mobility.Value       1.0

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
pfset Wells.Names                         ""

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
pfset Cycle.Names                         "constant"
pfset Cycle.constant.Names                "alltime"
pfset Cycle.constant.alltime.Length        1
pfset Cycle.constant.Repeat               -1

#-----------------------------------------------------------------------------
# Boundary Conditions
#-----------------------------------------------------------------------------
pfset BCPressure.PatchNames                   [pfget Geom.domain.Patches]

pfset Patch.x-lower.BCPressure.Type		      FluxConst
pfset Patch.x-lower.BCPressure.Cycle		      "constant"
pfset Patch.x-lower.BCPressure.alltime.Value	      0.0

pfset Patch.y-lower.BCPressure.Type		      FluxConst
pfset Patch.y-lower.BCPressure.Cycle		      "constant"
pfset Patch.y-lower.BCPressure.alltime.Value	      0.0

pfset Patch.z-lower.BCPressure.Type		      FluxConst
pfset Patch.z-lower.BCPressure.Cycle		      "constant"
pfset Patch.z-lower.BCPressure.alltime.Value	      0.0

pfset Patch.x-upper.BCPressure.Type		      FluxConst
pfset Patch.x-upper.BCPressure.Cycle		      "constant"
pfset Patch.x-upper.BCPressure.alltime.Value	      0.0

pfset Patch.y-upper.BCPressure.Type		      FluxConst
pfset Patch.y-upper.BCPressure.Cycle		      "constant"
pfset Patch.y-upper.BCPressure.alltime.Value	      0.0

pfset Patch.z-upper.BCPressure.Type		      OverlandFlow
pfset Patch.z-upper.BCPressure.Cycle		      "constant"
pfset Patch.z-upper.BCPressure.alltime.Value	      0.0

#-----------------------------------------------------------------------------
# Topo slopes in x-direction
#-----------------------------------------------------------------------------
pfset TopoSlopesX.Type                                "PFBFile"
pfset TopoSlopesX.GeomNames                           "domain"
pfset TopoSlopesX.FileName                            "LW.slopex.pfb"

#-----------------------------------------------------------------------------
# Topo slopes in y-direction
#-----------------------------------------------------------------------------
pfset TopoSlopesY.Type                                "PFBFile"
pfset TopoSlopesY.GeomNames                           "domain"
pfset TopoSlopesY.FileName                            "LW.slopey.pfb"

#-----------------------------------------------------------------------------
# Mannings coefficient
#-----------------------------------------------------------------------------
pfset Mannings.Type                                   "Constant"
pfset Mannings.GeomNames                              "domain"
pfset Mannings.Geom.domain.Value                      5.52e-6

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------
pfset Phase.RelPerm.Type                  VanGenuchten
pfset Phase.RelPerm.GeomNames             "domain s1 s2 s3 s4 s5 s6 s7 s8 s9 "

pfset Geom.domain.RelPerm.Alpha           3.5
pfset Geom.domain.RelPerm.N               2.0

pfset Geom.s1.RelPerm.Alpha        3.548
pfset Geom.s1.RelPerm.N            4.162

pfset Geom.s2.RelPerm.Alpha        3.467
pfset Geom.s2.RelPerm.N            2.738

pfset Geom.s3.RelPerm.Alpha        2.692
pfset Geom.s3.RelPerm.N            2.445

pfset Geom.s4.RelPerm.Alpha        0.501
pfset Geom.s4.RelPerm.N            2.659

pfset Geom.s5.RelPerm.Alpha        0.661
pfset Geom.s5.RelPerm.N            2.659

pfset Geom.s6.RelPerm.Alpha        1.122
pfset Geom.s6.RelPerm.N            2.479

pfset Geom.s7.RelPerm.Alpha        2.089
pfset Geom.s7.RelPerm.N            2.318

pfset Geom.s8.RelPerm.Alpha        0.832
pfset Geom.s8.RelPerm.N            2.514

pfset Geom.s9.RelPerm.Alpha        1.585
pfset Geom.s9.RelPerm.N            2.413

#-----------------------------------------------------------------------------
# Saturation
#-----------------------------------------------------------------------------
pfset Phase.Saturation.Type               VanGenuchten
pfset Phase.Saturation.GeomNames          "domain s1 s2 s3 s4 s5 s6 s7 s8 s9 "

pfset Geom.domain.Saturation.Alpha        3.5
pfset Geom.domain.Saturation.N            2.
pfset Geom.domain.Saturation.SRes         0.2
pfset Geom.domain.Saturation.SSat         1.0

pfset Geom.s1.Saturation.Alpha        3.548
pfset Geom.s1.Saturation.N            4.162
pfset Geom.s1.Saturation.SRes         0.000001
pfset Geom.s1.Saturation.SSat         1.0

pfset Geom.s2.Saturation.Alpha        3.467
pfset Geom.s2.Saturation.N            2.738
pfset Geom.s2.Saturation.SRes         0.000001
pfset Geom.s2.Saturation.SSat         1.0

pfset Geom.s3.Saturation.Alpha        2.692
pfset Geom.s3.Saturation.N            2.445
pfset Geom.s3.Saturation.SRes         0.000001
pfset Geom.s3.Saturation.SSat         1.0

pfset Geom.s4.Saturation.Alpha        0.501
pfset Geom.s4.Saturation.N            2.659
pfset Geom.s4.Saturation.SRes         0.000001
pfset Geom.s4.Saturation.SSat         1.0

pfset Geom.s5.Saturation.Alpha        0.661
pfset Geom.s5.Saturation.N            2.659
pfset Geom.s5.Saturation.SRes         0.000001
pfset Geom.s5.Saturation.SSat         1.0

pfset Geom.s6.Saturation.Alpha        1.122
pfset Geom.s6.Saturation.N            2.479
pfset Geom.s6.Saturation.SRes         0.000001
pfset Geom.s6.Saturation.SSat         1.0

pfset Geom.s7.Saturation.Alpha        2.089
pfset Geom.s7.Saturation.N            2.318
pfset Geom.s7.Saturation.SRes         0.000001
pfset Geom.s7.Saturation.SSat         1.0

pfset Geom.s8.Saturation.Alpha        0.832
pfset Geom.s8.Saturation.N            2.514
pfset Geom.s8.Saturation.SRes         0.000001
pfset Geom.s8.Saturation.SSat         1.0

pfset Geom.s9.Saturation.Alpha        1.585
pfset Geom.s9.Saturation.N            2.413
pfset Geom.s9.Saturation.SRes         0.000001
pfset Geom.s9.Saturation.SSat         1.0

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------
pfset PhaseSources.water.Type                         "Constant"
pfset PhaseSources.water.GeomNames                    "domain"
pfset PhaseSources.water.Geom.domain.Value            0.0

#----------------------------------------------------------------
# CLM Settings:
# ------------------------------------------------------------
pfset Solver.LSM                                      CLM
pfset Solver.CLM.CLMFileDir                           "clm_output/"
pfset Solver.CLM.Print1dOut                           False
pfset Solver.BinaryOutDir                             False
pfset Solver.CLM.DailyRST                      		  True
pfset Solver.CLM.SingleFile                       	  True
pfset Solver.CLM.CLMDumpInterval                      1

pfset Solver.CLM.MetForcing                           3D
pfset Solver.CLM.MetFileName                          "NLDAS"
pfset Solver.CLM.MetFilePath                          "../NLDAS/"
pfset Solver.CLM.MetFileNT                            24
pfset Solver.CLM.IstepStart                           1

pfset Solver.CLM.EvapBeta                             Linear
pfset Solver.CLM.VegWaterStress                       Saturation
pfset Solver.CLM.ResSat                               0.1
pfset Solver.CLM.WiltingPoint                         0.12
pfset Solver.CLM.FieldCapacity                        0.98
pfset Solver.CLM.IrrigationType                       none

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------
pfset ICPressure.Type                                 PFBFile
pfset ICPressure.GeomNames                            domain
pfset Geom.domain.ICPressure.RefPatch                   z-upper
pfset Geom.domain.ICPressure.FileName                   press.init.pfb

#----------------------------------------------------------------
# Outputs
# ------------------------------------------------------------
pfset Solver.WriteSiloSubsurfData 					  True
pfset Solver.WriteSiloPressure 						  True
pfset Solver.WriteSiloSaturation 					  True
pfset Solver.WriteSiloSlopes      					  True
pfset Solver.WriteSiloCLM                             True
pfset Solver.WriteCLMBinary                           False
pfset Solver.WriteSiloMannings                        True
pfset Solver.PrintCLM                                 True



#pfset Solver.PrintPressure                            True
#pfset Solver.PrintSaturation                          True
#pfset Solver.PrintMask                                True
#pfset Solver.PrintCLM                                 True
#pfset Solver.WriteSiloSpecificStorage                 False
#pfset Solver.WriteSiloMannings                        False
#pfset Solver.WriteSiloSubsurfData                     False
#pfset Solver.WriteSiloEvapTrans                       False
#pfset Solver.WriteSiloEvapTransSum                    False
#pfset Solver.WriteSiloOverlandSum                     False



#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------
pfset KnownSolution                                   NoKnownSolution

#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------
# ParFlow Solution
pfset Solver                                          Richards
pfset Solver.TerrainFollowingGrid                     True
pfset Solver.Nonlinear.VariableDz                     False

pfset Solver.MaxIter                                  25000
pfset Solver.Drop                                     1E-20
pfset Solver.AbsTol                                   1E-8
pfset Solver.MaxConvergenceFailures                   8
pfset Solver.Nonlinear.MaxIter                        80
pfset Solver.Nonlinear.ResidualTol                    1e-6

## new solver settings for Terrain Following Grid
pfset Solver.Nonlinear.EtaChoice                         EtaConstant
pfset Solver.Nonlinear.EtaValue                          0.001
pfset Solver.Nonlinear.UseJacobian                       True
pfset Solver.Nonlinear.DerivativeEpsilon                 1e-16
pfset Solver.Nonlinear.StepTol				 			1e-30
pfset Solver.Nonlinear.Globalization                     LineSearch
pfset Solver.Linear.KrylovDimension                      70
pfset Solver.Linear.MaxRestarts                           2

pfset Solver.Linear.Preconditioner                       PFMG
pfset Solver.Linear.Preconditioner.PCMatrixType     FullJacobian


#-----------------------------------------------------------------------------
# Distribute inputs
#-----------------------------------------------------------------------------
pfset ComputationalGrid.NX                41
pfset ComputationalGrid.NY                41
pfset ComputationalGrid.NZ                1
pfdist LW.slopex.pfb
pfdist LW.slopey.pfb

pfset ComputationalGrid.NX                41
pfset ComputationalGrid.NY                41
pfset ComputationalGrid.NZ                50
pfdist IndicatorFile_Gleeson.50z.pfb
pfdist press.init.pfb

#-----------------------------------------------------------------------------
# Run Simulation
#-----------------------------------------------------------------------------
set runname "LW"
puts $runname
pfrun    $runname

#-----------------------------------------------------------------------------
# Undistribute outputs
#-----------------------------------------------------------------------------
pfundist $runname
#pfundist press.init.pfb
pfundist LW.slopex.pfb
pfundist LW.slopey.pfb
pfundist IndicatorFile_Gleeson.50z.pfb

puts "ParFlow run Complete"
