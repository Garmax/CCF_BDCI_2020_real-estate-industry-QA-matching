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
# train = [[[] for i in range(5)] for i in range(train_reply.shape[0])]
# for i in range(train_reply.shape[0]):
#     train[i][0] = train_reply[3][i]
#     train[i][1] = train_reply[0][i]
#     train[i][2] = train_reply[1][i]
#     train[i][3] = train_query[1][train_reply[0][i]]
#     train[i][4] = train_reply[2][i]

# %%
# with open('../data/train.tsv', 'w', newline='', encoding='gb18030') as tsv_file:
#     writer = csv.writer(tsv_file, delimiter='\t')
#     # writer.writerow('header')
#     for row in train:
#         writer.writerow(row)

#%%


#%%
# test = [[[] for i in range(5)] for i in range(test_reply.shape[0])]
# for i in range(test_reply.shape[0]):
#     test[i][0] = i
#     test[i][1] = test_reply[0][i]
#     test[i][2] = test_reply[1][i]
#     test[i][3] = test_query[1][test_reply[0][i]]
#     test[i][4] = test_reply[2][i]
# print(test)
# with open('../data/test.tsv', 'w', newline='', encoding='gb18030') as tsv_file:
#     writer = csv.writer(tsv_file, delimiter='\t')
#     # writer.writerow('header')
#     for row in test:
#         writer.writerow(row)




#%%
# dev_list = np.random.randint(train_reply.shape[0], size=1000)
# print(dev_list[0])
# dev = [[[] for i in range(5)] for i in range(1000)]
# for i in range(1000):
#     dev[i][0] = train_reply[3][dev_list[i]]
#     dev[i][1] = train_reply[0][dev_list[i]]
#     dev[i][2] = train_reply[1][dev_list[i]]
#     dev[i][3] = train_query[1][train_reply[0][dev_list[i]]]
#     dev[i][4] = train_reply[2][dev_list[i]]
# print(dev)
# with open('C:/Users/a4/Desktop/dev.tsv', 'w', newline='') as tsv_file:
#     writer = csv.writer(tsv_file, delimiter='\t')
#     # writer.writerow('header')
#     for row in dev:
#         writer.writerow(row)

#%%
if __name__ == '__main__':
    preprocess()

# %%
