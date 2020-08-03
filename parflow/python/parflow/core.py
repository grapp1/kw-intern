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

  def write(self, fileFormat='pfidb', fileName=None):
    fName = os.path.join(PFDBObj.workingDirectory, f'{self._name}.{fileFormat}')
    if fileName:
      fName = os.path.join(PFDBObj.workingDirectory, f'{fileName}.{fileFormat}')
    writeDict(self.getKeyDict(), fName)

  def printOut(self, runName):
    print('\n', "*"*80, '\n')
    outFile = f'{runName}.out.txt'
    if os.path.exists(outFile):
      with open(outFile, "rt") as f:
        contents = f.read()
        if 'Problem solved' in contents:
          print('ParFlow ran successfully')
        else:
          print('ParFlow run failed. Contents of error output file: \n')
          f.close()
          print(contents)
    else:
      print(f'Cannot find {outFile} in {os.getcwd()}')

  def run(self, runName=None):
    fileName = f'./output/{runName}'
    self.write(fileFormat='pfidb', fileName=fileName)
    P = self.Process.Topology.P
    Q = self.Process.Topology.Q
    R = self.Process.Topology.R
    NumProcs = P * Q * R
    os.system('sh $PARFLOW_DIR/bin/run ' + fileName + ' ' + str(NumProcs))
    self.printOut(fileName)

