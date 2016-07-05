#!/usr/bin/env python

import pandas as pd

VERSION = '1.0'

df = pd.read_csv('alltests.csv')

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

df.to_csv('alltests_with_normalized_results_'+VERSION+'.csv', index=False)
