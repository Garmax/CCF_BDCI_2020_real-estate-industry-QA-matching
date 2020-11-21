import pandas as pd
import numpy as np
import csv

experiment = 'bs16_lr1e-5_ep5'

template = pd.read_csv('sample_submission.tsv', sep='\t', header=None)
result = pd.read_csv(experiment + '.txt', sep='\t')

for i in range(53756):
    template.iloc[i][2]=result.iloc[i]['prediction']

template.to_csv(experiment + '.tsv', sep='\t', index=False, header=None)
