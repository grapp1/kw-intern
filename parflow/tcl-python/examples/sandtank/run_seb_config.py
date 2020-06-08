# first version of script to convert the sandtank tcl script to Python
# need to include pfset function for variables
# does not include EcoSLIM

import parflow as pf

run = pf.Run('sandtank')

# -----------------------------------------------------------------------------
# Load dictionary as YAML
# -----------------------------------------------------------------------------

config = pf.YAMLFile('./run_seb_config.yaml')
run.set(config)

# -----------------------------------------------------------------------------
# Lake / River
# -----------------------------------------------------------------------------

if lake:
  pf.set(config.Templates.lake)
else:
  pf.set(config.Templates.river)

# -----------------------------------------------------------------------------
# Reset or keep going
# -----------------------------------------------------------------------------

if reset:
  pf.set(config.Templates.firstTime)
else:
  pf.set(config.Templates.nextTime)

# -----------------------------------------------------------------------------
# Check is the input is valid for possible run
# -----------------------------------------------------------------------------

run.validate(Level=DEBUG)

# -----------------------------------------------------------------------------
# pfdist ??
# -----------------------------------------------------------------------------

run.run()
run.dist('SandTank_Indicator.pfb')
