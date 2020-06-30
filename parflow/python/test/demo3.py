# demo3.py: testing run to set up geom inputs - box input with patches and boundary conditions

from parflow import Run

lw = Run('Little Washita')

# -----------------------------------------------------------------------------
# Setup database keys
# -----------------------------------------------------------------------------
lw.Process.Topology.P = 1
lw.Process.Topology.Q = 2
lw.Process.Topology.P = 1

lw.GeomInput.Names = 'box_input indi_input'

lw.GeomInput.box_input.InputType = Box
lw.GeomInput.box_input.GeomName = domain

lw.Geom.domain.Lower.X = 0.0
lw.Geom.domain.Lower.Y = 0.0
lw.Geom.domain.Lower.Z = 0.0

lw.Geom.domain.Upper.X = 41000.0
lw.Geom.domain.Upper.Y = 41000.0
lw.Geom.domain.Upper.Z = 100.0
lw.Geom.domain.Patches = "x-lower x-upper y-lower y-upper z-lower z-upper"

lw.Cycle.Names = "constant"
lw.Cycle.constant.Names = "alltime"
lw.Cycle.constant.alltime.Length = 1
lw.Cycle.constant.Repeat = -1

lw.BCPressure.PatchNames = lw.Geom.domain.Patches

lw.Patch.x-lower.BCPressure.Type = FluxConst
lw.Patch.x-lower.BCPressure.Cycle = "constant"
lw.Patch.x-lower.BCPressure.alltime.Value = 0.0

lw.Patch.y-lower.BCPressure.Type = FluxConst
lw.Patch.y-lower.BCPressure.Cycle = "constant"
lw.Patch.y-lower.BCPressure.alltime.Value = 0.0

lw.Patch.z-lower.BCPressure.Type = FluxConst
lw.Patch.z-lower.BCPressure.Cycle = "constant"
lw.Patch.z-lower.BCPressure.alltime.Value = 0.0

lw.Patch.x-upper.BCPressure.Type = FluxConst
lw.Patch.x-upper.BCPressure.Cycle = "constant"
lw.Patch.x-upper.BCPressure.alltime.Value = 0.0

lw.Patch.y-upper.BCPressure.Type = FluxConst
lw.Patch.y-upper.BCPressure.Cycle = "constant"
lw.Patch.y-upper.BCPressure.alltime.Value = 0.0

lw.Patch.z-upper.BCPressure.Type = OverlandFlow
lw.Patch.z-upper.BCPressure.Cycle = "constant"
lw.Patch.z-upper.BCPressure.alltime.Value = 0.0

# -----------------------------------------------------------------------------
# Validation process
# -----------------------------------------------------------------------------

lw.validate()
lw.write()
lw.run()
