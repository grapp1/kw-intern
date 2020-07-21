# Script to convert tcl scripts to python format

def tclToPython(tclfile, pyfile, runname):
  runstr = str(runname) + '.'
  with open(tclfile, 'r') as fin:
    with open(pyfile, 'w') as fout:
      lines = fin.readlines()
      prevLine = ''
      for line in lines:
        newline = line
        if 'lappend auto_path $env(PARFLOW_DIR)/bin' in newline:
          newline = 'from parflow import Run\n'

        if 'package require parflow' in newline:
          newline = ''

        if 'namespace import Parflow::*' in newline:
          newline = f'{runname} = Run("{runname}", __file__)\n'

        if newline[0:6] == 'pfset ':
          newline = newline.replace('pfset ', runstr)
          newline_subs = newline.split()
          if newline_subs[1][0].isalpha():
            newline = newline_subs[0] + ' = ' + "'" + ' '.join(newline_subs[1:]) + "'" + '\n'
          else:
            newline = newline_subs[0] + ' = ' + ' '.join(newline_subs[1:]) + '\n'

        # removing all lines of code that aren't commented out
        if newline[0:1] != '#' and newline[0:1] != '\n' and newline == line:
          # testing for lines that continue to the next line
          if len(prevLine) >= 2 and prevLine[-2] == "\\":
            pass
          else:
            newline = ''

        prevLine = newline

        fout.write(newline)

      outfile_string = str(pyfile[:-3])
      fout.write(f'{runname}.validate()\n')
      fout.write(f'{runname}.write("../output/{outfile_string}.pfidb")\n')
      fout.write(f'{runname}.write("../output/{outfile_string}.yaml")\n')
      fout.write(f'{runname}.run()\n')

  return

tclToPython('./comparison/default_richards.tcl', 'default_richards2.py', 'drich')

