# Result Submissions
THU Fall 2020 大数据分析(B)大作业-房产行业聊天问答匹配-比赛提交部分

`generate_submission.py`即将模型输出格式转换成提交格式的代码；

`sample_submission.tsv`为官方提交样例；

`bs**_lr****_ep*.tsv`即为每次实验结果的提交文件，bs：批处理大小；lr：学习率；ep：Epoch

## Submission Results (hfl/chinese-roberta-wwm-ext)
每次实验结果提交的得分如下表所示。
|             Model             | Batch Size | Learning Rate | Epoch | eval_acc_and_f1 | Submission Score |
| :---------------------------: | :--------: | :-----------: | :---: | :-------------: | :--------------: |
|    chinese-roberta-wwm-ext    |    200     |     2e-5      |   5   |     0.9318      |      待提交      |
|    chinese-roberta-wwm-ext    |    200     |     5e-5      |   5   |     0.9782      |      待提交      |
|    chinese-roberta-wwm-ext    |    200     |     5e-5      |  10   |     0.9937      |      0.7490      |
|    chinese-roberta-wwm-ext    |     32     |     1e-5      |   3   |     0.9188      |      0.7417      |
|    chinese-roberta-wwm-ext    |     32     |     2e-5      |   3   |     0.9204      |      未运行      |
|    chinese-roberta-wwm-ext    |     32     |     5e-5      |   3   |     0.8906      |      未运行      |
| chinese-roberta-wwm-ext-large |     32     |     5e-5      |   5   |     0.9914      |      待提交      |
| chinese-roberta-wwm-ext-large |     32     |     5e-5      |  10   |     0.9937      |      待提交      |
|    chinese-roberta-wwm-ext    |     16     |     1e-5      |   3   |     0.9168      |      0.7519      |
|    chinese-roberta-wwm-ext    |     16     |     1e-5      |   5   |     0.9473      |      0.7465      |
|    chinese-roberta-wwm-ext    |     16     |     2e-5      |   3   |     0.9285      |      0.7519      |
|    chinese-roberta-wwm-ext    |     16     |     5e-5      |   2   |     0.9020      |      0.7480      |
|    chinese-roberta-wwm-ext    |     16     |     5e-5      |   3   |     0.9476      |      0.7521      |
|    chinese-roberta-wwm-ext    |     16     |     5e-5      |   5   |     0.9734      |      0.7499      |
|    chinese-roberta-wwm-ext    |     8      |     1e-5      |   3   |     0.9188      |      0.7464      |
|    chinese-roberta-wwm-ext    |     8      |     2e-5      |   3   |                 |      未运行      |
|    chinese-roberta-wwm-ext    |     8      |     5e-5      |   3   |     0.9204      |      0.7404      |
