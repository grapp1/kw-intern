from .database.generated import Process, ComputationalGrid, GeomInput

class Run:
  def __init__(self, name):
    self.name = name

    # Attach all root keys required by the database
    self.Process = Process()
    self.ComputationalGrid = ComputationalGrid()
    self.GeomInput = GeomInput()

  def validate(self, indent=0):
    strIndent = '  '*indent
    errorCount = 0
    print('-'*80)
    print('Validating Parflow input')
    print('-'*80)
    for key in ['Process', 'ComputationalGrid', 'GeomInput']:
      print(f'{strIndent}{key}')
      errorCount += self.__dict__[key].validate(indent + 1)

    print('-'*80)
    if errorCount:
      print(f'{strIndent}{errorCount} issue(s) were found')
      print('-'*80)
    else:
      print(f'No error detected - SUCCESS')
      print('-'*80)

    return errorCount


  def write(self, workingDirectory='.'):
    # write pfidb file
    pass

  def run(self):
    pass
