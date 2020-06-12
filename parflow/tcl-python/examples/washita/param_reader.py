# param_reader
# reader to convert csv file of parameters to ParFlow key/value pairs

import pandas as pd
import numpy as np

# initializing the output dictionary
params = {}

# setting up to read csv and convert to key/value format: e.g. Geom.domain.Perm.Value
with open('LW_params.csv') as csv_file:
    LW_params = pd.read_csv(csv_file)
    
    # completing list of keys and values from csv file
    p_keys, p_vals = zip(*LW_params.items())
    
    # converting lists to a dictionary
    nan_values = 0
    for i in range(1,len(p_keys)):
        for j in range(len(p_vals[1])):
            value = f'Geom.{p_vals[0][j]}.{p_keys[i]}.Value'
            params[value] = p_vals[i][j]
            if np.isnan(p_vals[i][j]) == True:
                print(f'No value for Geom.{p_vals[0][j]}.{p_keys[i]}.Value, assigning domain value')
                del params[value]
                nan_values += 1
                
print(nan_values, 'NA values assigned to domain')
print(params)                  

