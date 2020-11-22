# Result Submissions
THU Fall 2020 大数据分析(B)大作业-房产行业聊天问答匹配-比赛提交部分

`generate_submission.py`即将模型输出格式转换成提交格式的代码；

`sample_submission.tsv`为官方提交样例；

`data`目录为训练集、验证集与测试集；

`bs**_lr****_ep*.tsv`即为每次实验结果的提交文件，bs：批处理大小；lr：学习率；ep：Epoch

## Submission Results (hfl/chinese-roberta-wwm-ext)
每次实验结果提交的得分如下表所示。
Batch Size|Learning Rate|Epoch|Submission Score
:-------:|:------:|:--------:|:-------:
32|1e-5|3|0.7417
32|2e-5|3|
32|5e-5|3|
16|1e-5|3|0.7519
16|1e-5|5|0.7465
16|2e-5|3|0.7519
16|5e-5|3|0.7521
8|1e-5|3|0.7464
8|2e-5|3|
8|5e-5|3|0.7404
