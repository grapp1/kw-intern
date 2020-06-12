# param_reader
# reader to convert csv file of parameters to ParFlow key/value pairs


import pandas as pd

# initializing the lists and output dictionary
param_keys = []
param_vals = []
params = {}


# setting up to read csv and convert to key/value format: e.g. Geom.domain.Perm.Value
with open('LW_params.csv') as csv_file:
    LW_params = pd.read_csv(csv_file)
    
    # completing list of keys and values from csv file
    for key, value in LW_params.iteritems(): 
        param_keys.append(key)
        param_vals.append(value)
    
    # converting lists to a dictionary
    for i in range(1,len(param_keys)):
        for j in range(len(param_vals[1])):
            params[f'Geom.{param_vals[0][j]}.{param_keys[i]}.Value'] = \
            param_vals[i][j]
            
print(params)                  

