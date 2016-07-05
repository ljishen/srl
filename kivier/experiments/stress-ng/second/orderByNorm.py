#!/usr/bin/env python
import sys
import pandas as pd

VERSION = '1.1'

if len(sys.argv) != 3:
    raise Exception("./orderByNorm.py <target machine name> <data folder name inside results folder>")

target_machine = sys.argv[1]
folder_name = sys.argv[2]

df = pd.read_csv('results/'+folder_name+'/alltests_with_normalized_results_'+VERSION+'.csv')
df = df[df['machine'] == target_machine]
df = df.sort_values(by='normalized', ascending=0)
df.to_csv('results/'+folder_name+'/alltests_with_normalized_ordered_'+target_machine+'_results_'+VERSION+'.csv', index=False)
