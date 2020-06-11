# param_reader
# reader to convert csv file of parameters to ParFlow key/value pairs


import pandas as pd

param_keys = []
param_vals = []

pd.read_csv

with open('LW_params.csv') as csv_file:
    LW_params = pd.read_csv(csv_file)
    print(LW_params)
    
    for key, value in LW_params.iteritems(): 
        print(key,".",value)
        print() 
                    
                    

