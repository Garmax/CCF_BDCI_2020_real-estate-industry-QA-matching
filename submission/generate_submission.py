# %%
import pandas as pd
import numpy as np

experiment = 'bs200_lr5e-5_ep10'

template = pd.read_csv('../data/sample_submission.tsv', sep='\t',
                       header=None, dtype=np.int32)

result = pd.read_csv(
    '../modeling/{}/test_results_mrpc.txt'.format(experiment), sep='\t', dtype=np.int32)

template[2] = result['prediction']

template.to_csv(experiment + '.tsv', sep='\t', index=False, header=None)

# %%
