import os

from .database.generated import BaseRun
from .utils import extractKeysFromObject, writeDict

class Run(BaseRun):
  def __init__(self, name):
    super().__init__(None)
    self._name = name

  def getKeyDict(self):
    keyDict = {}
    extractKeysFromObject(keyDict, self)
    return keyDict

  def write(self, fileName=None, fileFormat='pfidb', workingDirectory='.'):
    fName = os.path.join(workingDirectory, f'{self._name}.{fileFormat}')
    fName = fileName if fileName else fName
    writeDict(self.getKeyDict(), fName)

  def run(self):
    pass
