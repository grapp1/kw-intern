from .database.generated import BaseRun

class Run(BaseRun):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def write(self, workingDirectory='.'):
    # write pfidb file
    pass

  def run(self):
    pass
