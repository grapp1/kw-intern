import runpy, os


test_files = ['default_richards.py',
              'water_balance_x.py',
              'default_overland.py',
              'crater2D.py',
              'harvey_flow.py',
              'forsyth2.py',
              'default_single.py']

os.chdir('./examples')

for file in test_files:
  runpy.run_path(path_name=f'./{file[:-3]}/{file}')
  os.chdir('../')

