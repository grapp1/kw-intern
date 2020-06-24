# schema_v2.py: traditional dictionary structure

import yaml

class parflow:

    """Hello, welcome to ParFlow"""

    def __init__(self, runname='runname', config_file = "run_config.yaml"):
        self.runname = runname
        with open(config_file) as file:
            self.pf = yaml.load(file, Loader=yaml.FullLoader)
