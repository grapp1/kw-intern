from parflow import Run

lw = Run('Little Washita')

# -----------------------------------------------------------------------------
# Required for validation
# -----------------------------------------------------------------------------

lw.Process.Topology.P = -9

lw.ComputationalGrid.Lower.X = 1.0
lw.ComputationalGrid.Lower.Y = 1.0
lw.ComputationalGrid.Lower.Z = 1.0

lw.ComputationalGrid.NX = 1
lw.ComputationalGrid.NY = 1
lw.ComputationalGrid.NZ = 1

lw.ComputationalGrid.DX = 1.0
lw.ComputationalGrid.DY = 1.0
lw.ComputationalGrid.DZ = 1.0

lw.TimingInfo.StartTime = 0.0
lw.TimingInfo.StopTime = 10.0
lw.TimingInfo.DumpInterval = 2.0

lw.TimeStep.Type = 'Constant'
lw.TimeStep.Value = 1.0

lw.Domain.GeomName = 'domain'

lw.Gravity = 9.8

lw.KnownSolution = 'Constant'

# -----------------------------------------------------------------------------
# Setup database keys
# -----------------------------------------------------------------------------

lw.Solver = 'test'
lw.Solver = 'Impes'
# lw.Solver = 'Richards'

lw.Solver.help()
print('+'*10)
lw.help('Solver')

# -----------------------------------------------------------------------------
# Validation process
# -----------------------------------------------------------------------------

print('-'*80)
print('User ask for validation')
print('-'*80)
lw.validate()
print('-'*80)

# lw.write()
# lw.run()

lw.write('./output/value_obj.yaml')
lw.write('./output/value_obj.pfidb')
lw.write('./output/value_obj.json')
