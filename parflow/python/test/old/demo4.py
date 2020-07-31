# demo4.py: testing run to set up timing inputs adn solver settings

from parflow import Run

lw = Run('Little Washita')

# -----------------------------------------------------------------------------
# Setup database keys
# -----------------------------------------------------------------------------
lw.Process.Topology.P = 1
lw.Process.Topology.Q = 2
lw.Process.Topology.P = 1

# lw.TimingInfo.BaseUnit = 1.0
# lw.TimingInfo.StartCount = 0.0
# lw.TimingInfo.StartTime = 0.0
# lw.TimingInfo.StopTime = 24.0   # need to make sure this is greater than the start time, etc.
# lw.TimingInfo.DumpInterval = 1.0
# lw.TimeStep.Type = Constant
# lw.TimeStep.Value = 1.0

# lw.Solver = 'Richards'
lw.Solver.TerrainFollowingGrid = True
lw.Solver.Nonlinear.VariableDz = False

lw.Solver.MaxIter = 25000
lw.Solver.Drop = 1E-20
lw.Solver.AbsTol = 1E-8
lw.Solver.MaxConvergenceFailures = 8
lw.Solver.Nonlinear.MaxIter = 80
lw.Solver.Nonlinear.ResidualTol = 1e-6

lw.Solver.Nonlinear.EtaChoice = EtaConstant
lw.Solver.Nonlinear.EtaValue = 0.001
lw.Solver.Nonlinear.UseJacobian = True
lw.Solver.Nonlinear.DerivativeEpsilon = 1e-16
lw.Solver.Nonlinear.StepTol = 1e-30
lw.Solver.Nonlinear.Globalization = LineSearch
lw.Solver.Linear.KrylovDimension = 70
lw.Solver.Linear.MaxRestarts = 2

lw.Solver.Linear.Preconditioner = PFMG
lw.Solver.Linear.Preconditioner.PCMatrixType = FullJacobian

# -----------------------------------------------------------------------------
# Validation process
# -----------------------------------------------------------------------------

lw.validate()
lw.write()
lw.run()
