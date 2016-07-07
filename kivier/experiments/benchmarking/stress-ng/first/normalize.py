#!/usr/bin/env python
import sys
import pandas as pd
import csv

if len(sys.argv) != 3:
    raise Exception("Expecting two argument: input file and the name of base machine")

input_filename = sys.argv[1]
fixed_filename = input_filename + ".fix"

with open('data/without_kv1.json', 'r') as f_kv_profile:
    kv_profile = f_kv_profile.read()

    with open(fixed_filename, 'w') as ff:
        fixed_writer = csv.writer(ff, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        with open(input_filename, 'r') as f:
            for row in csv.reader(f, delimiter=',', skipinitialspace=True):
                if "-memory-" in row[2]:
                    new_benchmark = row[2].replace("-memory-", "-cpu-")
                    if kv_profile.find(new_benchmark) > 0:
                        row[2] = new_benchmark
                fixed_writer.writerow(row)



df = pd.read_csv(fixed_filename)
base_machine = sys.argv[2]

# get a dataframe base results only with columns 'benchmark' and 'result'
predicate = (df['machine'] == base_machine) & (df['limits'] == 'without')
base_results = df[predicate][['benchmark', 'result']]

# rename the 'result' column
base_results.rename(columns={'result': 'base_result'}, inplace=True)

# merge all tests with the base_results column (i.e. join on 'benchmark' column)
df = pd.merge(base_results, df, how='inner', on='benchmark')

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
df.to_csv('alltests_with_normalized_results.csv', index=False)
