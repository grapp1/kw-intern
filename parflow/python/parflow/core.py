import os

from .database.generated import BaseRun, PFDBObj
from .utils import extractKeysFromObject, writeDict
from .database import TerminalColors as term
from .database import TerminalSymbols as termSymbol

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
      fName = os.path.join(PFDBObj.workingDirectory, f'{fileName}.{fileFormat}')
    fullFilePath = os.path.abspath(fName)
    writeDict(self.getKeyDict(), fullFilePath)
    return fullFilePath, fullFilePath[:-(len(fileFormat)+1)]

  def checkParFlowExecution(self, runName):
    print(f'# {"="*78}')
    outFile = f'{runName}.out.txt'
    if os.path.exists(outFile):
      with open(outFile, "rt") as f:
        contents = f.read()
        if 'Problem solved' in contents:
          print(f'# ParFlow ran successfully {termSymbol.splash*3}')
        else:
          print(f'# ParFlow run failed. {termSymbol.x} {termSymbol.x} {termSymbol.x} Contents of error output file:')
          print("-"*80)
          print(contents)
          print("-"*80)
    else:
      print(f'# Cannot find {outFile} in {os.getcwd()}')
    print(f'# {"=" * 78}')

  def run(self, workingDirectory=None, skipValidation=False):
    if workingDirectory:
      PFDBObj.setWorkingDirectory(workingDirectory)

    fileName, runFile = self.write()

    print()
    print(f'# {"="*78}')
    print(f'# ParFlow directory')
    print(f'#  - {os.getenv("PARFLOW_DIR")}')
    print(f'# Working directory')
    print(f'#  - {os.path.dirname(fileName)}')
    print(f'# ParFlow database')
    print(f'#  - {os.path.basename(fileName)}')
    print(f'# {"="*78}')
    print()

    if not skipValidation:
      self.validate()
      print()

    P = self.Process.Topology.P
    Q = self.Process.Topology.Q
    R = self.Process.Topology.R
    NumProcs = P * Q * R

    os.chdir(PFDBObj.workingDirectory)
    os.system('sh $PARFLOW_DIR/bin/run ' + runFile + ' ' + str(NumProcs))

    self.checkParFlowExecution(runFile)
    print()

