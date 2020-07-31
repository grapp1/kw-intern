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
          newline_subs[0] = newline_subs[0].replace('-', '_')
          if newline_subs[1][0].isalpha() or newline_subs[1][0] == "\"":
            newline = newline_subs[0] + ' = ' + "'" + ' '.join(newline_subs[1:]) + "'" + '\n'
            newline = newline.replace('-', '_').replace('\"', '').replace("'False'", "False").replace("'True'", "True")
          elif newline_subs[1][0] == '$' and len(newline_subs) == 2:
            newline = newline_subs[0] + ' = ' + newline_subs[1][1:] + '\n'
          else:
            newline = newline_subs[0] + ' = ' + ' '.join(newline_subs[1:]) + '\n'

        if newline[0:4] == 'set ' and 'runname' not in newline:
          newline = newline.replace('set ', '')
          newline_subs = newline.split()
          if newline_subs[1][0].isalpha():
            newline = newline_subs[0] + ' = ' + "'" + ' '.join(newline_subs[1:]) + "'" + '\n'
          else:
            newline = newline_subs[0] + ' = ' + ' '.join(newline_subs[1:]) + '\n'

        # commenting out all lines of code that haven't been edited yet
        if newline[0:1] != '#' and newline[0:1] != '\n' and newline == line:
          # testing for lines that continue to the next line
          if len(prevLine) >= 2 and prevLine[-2] == "\\":
            pass
          else:
            newline = '# ' + newline

        prevLine = newline

        fout.write(newline)

      outfile_string = str(pyfile[:-3])
      fout.write(f'{runname}.validate()\n')
      fout.write(f'{runname}.write("../output/{outfile_string}.pfidb")\n')
      fout.write(f'{runname}.write("../output/{outfile_string}.yaml")\n')
      fout.write(f'{runname}.run()\n')

  return

tclToPython('./test/tcl_converted/default_overland.tcl', './test/default_overland.py', 'dover')

