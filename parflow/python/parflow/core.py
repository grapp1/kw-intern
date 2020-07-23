import os

from .database.generated import BaseRun, PFDBObj
from .utils import extractKeysFromObject, writeDict

class Run(BaseRun):
  def __init__(self, name, basescript=None):
    super().__init__(None)
    self._name = name
    if basescript:
      PFDBObj.setWorkingDirectory(os.path.dirname(basescript))

  def getKeyDict(self):
    keyDict = {}
    extractKeysFromObject(keyDict, self)
    return keyDict

  def write(self, fileName=None, fileFormat='pfidb'):
    fName = os.path.join(PFDBObj.workingDirectory, f'{self._name}.{fileFormat}')
    if fileName:
      fName = os.path.join(PFDBObj.workingDirectory, fileName)
    writeDict(self.getKeyDict(), fName)

  def run(self, fileName=None):
    fName = os.path.join(PFDBObj.workingDirectory, f'{self._name}')
    if fileName:
      fName = os.path.join(PFDBObj.workingDirectory, fileName)
    os.system(f'./run_parflow.sh {fName}')
