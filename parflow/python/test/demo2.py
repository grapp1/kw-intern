# demo2.py: testing run to set up geom inputs

from parflow import Run

lw = Run('Little Washita')

# -----------------------------------------------------------------------------
# Setup database keys
# -----------------------------------------------------------------------------
lw.Process.Topology.P = 1
lw.Process.Topology.Q = 2
lw.Process.Topology.P = 4
lw.Process.Topology.R = 6
lw.ComputationalGrid.Lower.X = 5.0

lw.Solver.Type = 'Richards'
lw.Solver.AbsTol = 1e-7

lw.GeomInput.Names = 'box_input indi_input'

lw.GeomInput.box_input.InputType = 'Box'
lw.GeomInput.box_input.GeomName = 'domain'

lw.GeomInput.indi_input.InputType = 'IndicatorField'
lw.GeomInput.indi_input.GeomNames = "s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 g1 g2 g3 g4 g5 g6 g7 g8"
lw.Geom.indi_input.FileName = "IndicatorFile_Gleeson.50z.pfb"

lw.GeomInput.s1.Value = 1
lw.GeomInput.s2.Value = 2
lw.GeomInput.s3.Value = 3
lw.GeomInput.s4.Value = 4
lw.GeomInput.s5.Value = 5
lw.GeomInput.s6.Value = 6
lw.GeomInput.s7.Value = 7
lw.GeomInput.s8.Value = 8
lw.GeomInput.s9.Value = 9
lw.GeomInput.s10.Value = 10
lw.GeomInput.s11.Value = 11
lw.GeomInput.s12.Value = 12
lw.GeomInput.s13.Value = 13
lw.GeomInput.g1.Value = 21
lw.GeomInput.g2.Value = 22
lw.GeomInput.g3.Value = 23
lw.GeomInput.g4.Value = 24
lw.GeomInput.g5.Value = 25
lw.GeomInput.g6.Value = 26
lw.GeomInput.g7.Value = 27
lw.GeomInput.g8.Value = 28


lw.Geom.domain.Perm.Type = 'Constant'

# -----------------------------------------------------------------------------
# Validation process
# -----------------------------------------------------------------------------

lw.validate()
lw.write('./output/demo2_lw.pfidb')
lw.run()
