import runpy


test_files = ['default_richards.py',
              'water_balance_x.py',
              'default_single.py']

for file in test_files:
  runpy.run_path(path_name=f'./test/{file}')

