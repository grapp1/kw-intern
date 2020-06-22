# EcoSLIM read testing
# requre that slimin.txt already exists

runname = 'test'
config = {}
config['StartNumber'] = 0
config['RunLength'] = 20
config['reset'] = 0

with open('slimin.txt', 'r') as file:
    data = file.readlines()
    
data[1] = f'"./{runname}"\n'

if config['reset'] == 1:
    data[6] = '0      !no particles per cell at start of simulation\n'
else:
    data[6] = '-1     !read particle restart file'
    
data[12] = f'''{config['StartNumber'] + 1}    ! Parflow t1: ParFlow file number to start from (initial condition is pft1-1)\n'''
data[13] = f'''{config['StartNumber'] + config['RunLength']}    ! Parflow t2: ParFlow file number to stop at\n'''

with open('slimin.txt', 'r+') as file:
    file.write(''.join(data))
