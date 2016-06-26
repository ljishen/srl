#!/usr/bin/env python
import sys
import pandas as pd

if len(sys.argv) != 3:
    raise Exception("./normalize.py <base machine name> <data folder name inside results folder>")

base_machine = sys.argv[1]
folder_name = sys.argv[2]
df = pd.read_csv('results/'+folder_name+'/alltests.csv')

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
df.to_csv('results/'+folder_name+'/alltests_with_normalized_results.csv', index=False)
