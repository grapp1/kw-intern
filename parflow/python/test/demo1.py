from parflow import Run

lw = Run('Little Washita')

# -----------------------------------------------------------------------------
# Setup database keys
# -----------------------------------------------------------------------------

# lw.enableLineError()
# lw.enableExitError()

lw.Process.Topology.Q = 1
lw.Process.Topology.P = -1.5

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
