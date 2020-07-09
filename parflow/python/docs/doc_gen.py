# Running tests to generate documentation from yaml/json files

import pypandoc as ppd
import json


with open('demo1_lw_test.json') as json_file:
    data = json.load(json_file)


output = ppd.convert_text(json.dumps(data), format='json',to='md', outputfile='test.md')
