# script for clearing outputs in test/examples/{test_run} directories

import os
import glob

print()
print(" Which directory(ies) from '/examples/' would you like to clear?")
output_directory = [input(" (type all for all directories, separate multiple directories by spaces): ")][0].split(' ')

os.chdir('./examples/')

if output_directory[0] == 'all':
  output_directory = os.listdir()

for directory in output_directory:
  if os.path.isdir(directory):
    fileNames = glob.glob(f'./{directory}/*.out.*')
    fileNames = fileNames + glob.glob(f'./{directory}/*.pfidb')
    if len(fileNames):
      try:
        for file in fileNames:
          os.remove(file)
        print(f'  + Cleared directory "{directory}"')
      except OSError:
        print(f'  X Error in clearing directory "{directory}"')
    else:
      print(f'  - No output files in {directory}')

print()