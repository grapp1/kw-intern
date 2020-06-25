# schema_v4.py: traditional dictionary structure, importing yaml

import yaml

class run:

    """Initializing ParFlow run"""

    def __init__(self, runname='runname', input_set_file = "input_set2.yaml"):
        self.runname = runname
        with open(input_set_file) as file:
            self.pf = yaml.load(file, Loader=yaml.FullLoader)


# to add autocompletion
class PFDict:
  def __init__(self, d=None):
    if d is None:
      d = {}
    for k, v in d.items():
      if isinstance(v, (list, tuple)):
        v = [PFDict(x) if isinstance(x, dict) else x for x in v]
      elif isinstance(v, dict):
        v = PFDict(v)
      setattr(self, k, v)





