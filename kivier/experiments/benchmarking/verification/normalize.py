#!/usr/bin/env python

import os
import sys
import pandas as pd

VERSION = '1.0'

if len(sys.argv) != 2:
    print("Usage: ./normalize.py <csv file>")
    sys.exit()

input_file = sys.argv[1]
df = pd.read_csv(input_file)

def calc(r1, r2):
    if r1 >= r2:
        return r1 / r2
    else:
        return -1 * r2 / r1

def normalize(row):
    if row['lower_is_better'] is True:
        return calc(row['base_result'], row['result'])
    else:
        return calc(row['result'], row['base_result'])

df['normalized'] = df.apply(normalize, axis=1)

prefix=os.path.splitext(input_file)[0]
df.to_csv(prefix+'_with_normalized_results_'+VERSION+'.csv', index=False)
