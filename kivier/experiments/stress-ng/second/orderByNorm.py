#!/usr/bin/env python

import sys
import pandas as pd

if len(sys.argv) != 3:
    raise Exception("./normalize.py <base machine name> <data folder name inside results folder>")

base_machine = sys.argv[1]
folder_name = sys.argv[2]

df = pd.read_csv('results/'+folder_name+'/alltests_with_normalized_results.csv')
predicate = (df['machine'] == base_machine)
df = df[predicate]
df = df.sort_values(by='normalized', ascending=0)
df.to_csv('results/'+folder_name+'/alltests_with_normalized_ordered_'+base_machine+'_results.csv', index=False)
