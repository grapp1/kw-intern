# first version of script to convert the sandtank tcl script to Python
# need to include pfset function for variables
# does not include EcoSLIM

import parflow as pf

run = pf.Run('sandtank')

# -----------------------------------------------------------------------------
# Load dictionary as YAML
# -----------------------------------------------------------------------------

options = pf.Options()
options.loadFromYAML('./config.yaml')

options.well_1_value = 10
options.well_2_value = 0
options.well_3_value = 5
options.well_4_value = 1

config = pf.ConfigYAML('./run_seb_config.yaml')
run.set(config, options)

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
