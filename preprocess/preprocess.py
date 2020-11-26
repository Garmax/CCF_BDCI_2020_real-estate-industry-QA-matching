# %%
import pandas as pd
import numpy as np

# %%
train_query = pd.read_csv('../data/train/train.query.tsv',
                          sep='\t', header=None, encoding='utf-8')
train_reply = pd.read_csv('../data/train/train.reply.tsv',
                          sep='\t', header=None, encoding='utf-8')
test_query = pd.read_csv('../data/test/test.query.tsv',
                         sep='\t', header=None, encoding='gb18030')
test_reply = pd.read_csv('../data/test/test.reply.tsv',
                         sep='\t', header=None, encoding='gb18030')

# %%
# def preprocess():
train = pd.concat([train_reply.iloc[:, 3], train_reply.iloc[:, 0], train_reply.iloc[:, 1],
                    train_query.iloc[train_reply[0], 1].reset_index(drop=True), train_reply.iloc[:, 2]], axis=1, ignore_index=True)
train.columns= ['col1','col2','col3','col4','col5']
train.to_csv('../modeling/data/MRPC/train.tsv', sep='\t', index=None)

test = pd.concat([test_reply.iloc[:, 0], test_reply.iloc[:, 1], 
                    test_query.iloc[test_reply[0], 1].reset_index(drop=True), test_reply.iloc[:, 2]], axis=1, ignore_index=True)
test.columns= ['col2','col3','col4','col5']
test['col1'] = test.index
test = test.reindex(columns=['col1','col2','col3','col4','col5'])   
test.to_csv('../modeling/data/MRPC/test.tsv', sep='\t', index=None)

#%%
#random_state =0随机，random_state=1设置种子
dev = train.sample(n=1000, random_state=1)
dev.columns= ['col1','col2','col3','col4','col5']
dev.to_csv('../modeling/data/MRPC/dev.tsv', sep='\t', index=None)

# %%
from sklearn.model_selection import train_test_split
train_split, test_split = train_test_split(train, test_size=0.2)
train_split.to_csv('../modeling/data/SPLIT/train.tsv', sep='\t', index=None)
test_split.to_csv('../modeling/data/SPLIT/test.tsv', sep='\t', index=None)
dev = train_split.sample(n=1000, random_state=1)
dev.columns= ['col1','col2','col3','col4','col5']
dev.to_csv('../modeling/data/SPLIT/dev.tsv', sep='\t', index=None)