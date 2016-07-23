#!/usr/bin/env python

# This script is used to check if the json results produced by stress-ng has duplicated stress tests.

import sys
import pandas as pd

if len(sys.argv) != 2:
    print("Usage: ./check_duplicate.py <json file>")
    sys.exit()

df = pd.read_json(sys.argv[1])

stress_names = []
s = df['name'].str.rsplit(pat='-')
for index,value in s.iteritems():
    start = 2
    if value[1] == 'cpu' and value[2] == 'cache':
        start = 3
    stress_names.append('-'.join(value[start:]))

stress_name_s = pd.Series(stress_names)
print(stress_name_s[stress_name_s.duplicated(keep=False)])
