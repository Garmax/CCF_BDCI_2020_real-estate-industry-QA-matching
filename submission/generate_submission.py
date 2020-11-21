import pandas as pd
import numpy as np
import csv

experiment = 'bs16_lr1e-5_ep3'

template = pd.read_csv('sample_submission.tsv', sep='\t', header=None)
result = pd.read_csv(experiment + '.txt', sep='\t')

for i in range(53756):
    template.iloc[i][2]=result.iloc[i]['prediction']

template.to_csv(experiment + '.tsv', sep='\t', index=False, header=None)

# with open('C:/Users/a4/Desktop/dev.tsv', 'w', newline='', encoding='gb18030') as tsv_file:
#     writer = csv.writer(tsv_file, delimiter='\t')
#     #writer.writerow('header')
#     for row in dev:
#         writer.writerow(row)
