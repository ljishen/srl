#!/usr/bin/env python

import os
import sys
import pandas as pd

VERSION = '1.1'

if len(sys.argv) != 3:
    print("Usage: ./normalize.py <input csv file> <base machine name>")
    sys.exit()

input_file = sys.argv[1]
base_machine = sys.argv[2]
df = pd.read_csv(input_file)

# get a dataframe base results only with columns 'benchmark' and 'result'
predicate = (df['machine'] == base_machine) & (df['limits'] == 'without')
base_results = df[predicate][['benchmark', 'result']]

# rename the 'result' column
base_results.rename(columns={'result': 'base_result'}, inplace=True)

# merge all tests with the base_results column (i.e. join on 'benchmark' column)
df = pd.merge(base_results, df)

# and exclude the base system itself
df = df[df['machine'] != base_machine]

happened = False

# lastly, get normalized results for target systems w.r.t. the base system
def normalize(row):
    if row['lower_is_better'] is True:
        return row['base_result'] / row['result']
    else:
        global happened
        happened = True
        return row['result'] / row['base_result']

df['normalized'] = df.apply(normalize, axis=1)

print("happened: " + str(happened))

# and rewrite the results, now including the normalized column
prefix=os.path.splitext(input_file)[0]
df.to_csv(prefix+'_with_normalized_results_'+VERSION+'.csv', index=False)
