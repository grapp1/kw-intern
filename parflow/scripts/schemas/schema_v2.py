# schema_v2.py: traditional dictionary structure

import yaml

class parflow:

    """Hello, welcome to ParFlow"""

    def __init__(self, runname='runname', config_file = "run_config.yaml"):
        self.runname = runname
        with open(config_file) as file:
            self.pf = yaml.load(file, Loader=yaml.FullLoader)


class PFDict(dict):
  def __init__(self, d):
    super().__init__(d)
    self.convert_children()

  def convert_children(self):
    def convert_recursive(child):
      for key, value in child.items():
        if isinstance(value, dict):
          child[key] = PFDict(value)
          convert_recursive(child[key])

    convert_recursive(self)

  def __getattr__(self, item):
    if item in self.d:
      return self.d[item]

  def __dir__(self):
    return self.d.keys()




