#!/usr/bin/env python

import os
import sys
import pandas as pd


if len(sys.argv) != 4:
    print("This script finds all stressors in both files and only retain the items in base machine.")
    print("Usage: ./retain_base.py <base machine name> <reference machine name> <destination folder>")
    sys.exit()

base_machine = sys.argv[1]
ref_machine = sys.argv[2]
dest = sys.argv[3]

df_base = pd.read_json(base_machine)
df_ref = pd.read_json(ref_machine)

column_prefix = 'ref_'

df_ref.rename(columns = lambda x : column_prefix + x, inplace=True)

df = pd.merge(df_base, df_ref, how='inner', left_on='name', right_on=column_prefix+'name')
df = df.filter(regex='^(?!'+column_prefix+')\w+')

if not os.path.exists(dest):
    os.makedirs(dest)
df.to_json(dest+'/retained.json', orient='records')
