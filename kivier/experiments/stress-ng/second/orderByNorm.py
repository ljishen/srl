#!/usr/bin/env python

import sys
import pandas as pd

if len(sys.argv) != 2:
    raise Exception("Expecting one argument (base system name)")

df = pd.read_csv('results/alltests_with_normalized_results.csv')
base_machine = sys.argv[1]
predicate = (df['machine'] == base_machine)
df = df[predicate]
df = df.sort_values(by='normalized', ascending=0)
df.to_csv('results/alltests_with_normalized_ordered_'+base_machine+'_results.csv', index=False)
