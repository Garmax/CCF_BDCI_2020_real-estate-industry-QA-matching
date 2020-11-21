import pandas as pd
import numpy as np
import csv


def preprocess():
    train_query = pd.read_csv('C:/Users/a4/Desktop/train/train.query.tsv', sep='\t', header=None, encoding='utf-8', engine='python')
    train_reply = pd.read_csv('C:/Users/a4/Desktop/train/train.reply.tsv', sep='\t', header=None, encoding='utf-8', engine='python')
    test_query = pd.read_csv('C:/Users/a4/Desktop/test/test.query.tsv', sep='\t', header=None, encoding='gb18030', engine='python')
    test_reply = pd.read_csv('C:/Users/a4/Desktop/test/test.reply.tsv', sep='\t', header=None, encoding='gb18030', engine='python')
    # train = [[[] for i in range(5)] for i in range(train_reply.shape[0])]
    # for i in range(train_reply.shape[0]):
    #     train[i][0] = train_reply[3][i]
    #     train[i][1] = train_reply[0][i]
    #     train[i][2] = train_reply[1][i]
    #     train[i][3] = train_query[1][train_reply[0][i]]
    #     train[i][4] = train_reply[2][i]
    # print(train)
    # with open('C:/Users/a4/Desktop/train.tsv', 'w', newline='', encoding='gb18030') as tsv_file:
    #     writer = csv.writer(tsv_file, delimiter='\t')
    #     for row in train:
    #         writer.writerow(row)

    # test = [[[] for i in range(5)] for i in range(test_reply.shape[0])]
    # for i in range(test_reply.shape[0]):
    #     test[i][0] = i
    #     test[i][1] = test_reply[0][i]
    #     test[i][2] = test_reply[1][i]
    #     test[i][3] = test_query[1][test_reply[0][i]]
    #     test[i][4] = test_reply[2][i]
    # print(test)
    # with open('C:/Users/a4/Desktop/test.tsv', 'w', newline='', encoding='gb18030') as tsv_file:
    #     writer = csv.writer(tsv_file, delimiter='\t')
    #     for row in test:
    #         writer.writerow(row)

    dev_list = np.random.randint(train_reply.shape[0], size=1000)
    print(dev_list[0])
    dev = [[[] for i in range(5)] for i in range(1000)]
    for i in range(1000):
        dev[i][0] = train_reply[3][dev_list[i]]
        dev[i][1] = train_reply[0][dev_list[i]]
        dev[i][2] = train_reply[1][dev_list[i]]
        dev[i][3] = train_query[1][train_reply[0][dev_list[i]]]
        dev[i][4] = train_reply[2][dev_list[i]]
    # print(dev)
    with open('C:/Users/a4/Desktop/dev.tsv', 'w', newline='', encoding='gb18030') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t')
        for row in dev:
            writer.writerow(row)


if __name__ == '__main__':
    preprocess()