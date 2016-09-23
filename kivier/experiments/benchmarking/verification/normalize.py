#!/usr/bin/env python

import os
import sys
import pandas as pd

VERSION = '1.1'

if len(sys.argv) != 2:
    print("Usage: ./normalize.py <csv file>")
    sys.exit()

input_file = sys.argv[1]
df = pd.read_csv(input_file)

def normalize(row):
    if row['lower_is_better'] is True:
        return row['base_result'] / row['result']
    else:
        return row['result'] / row['base_result']

df['normalized'] = df.apply(normalize, axis=1)

prefix=os.path.splitext(input_file)[0]
df.to_csv(prefix+'_with_normalized_results_'+VERSION+'.csv', index=False)
