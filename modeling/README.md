# Model Set-up, Training & Testing
THU Fall 2020 大数据分析(B)大作业-房产行业聊天问答匹配-模型建立与训练部分

`modeling.py`即建模与训练/测试的代码；

`running.txt`为运行程序的脚本；

`data`目录为训练集、验证集与测试集；

`bs**_lr****_ep*`目录即为每次调参相应的结果（不含分批节点保存与pytorch_model）；
bs：批处理大小；lr：学习率；ep：Epoch

```python
python modeling.py \
  --model_name_or_path hfl/chinese-roberta-wwm-ext \
  --task_name MRPC \
  --do_train \
  --do_eval \
  --do_predict \
  --max_seq_length 128 \
  --per_device_train_batch_size 200 \
  --learning_rate 5e-5 \
  --num_train_epochs 5.0 \
  --data_dir 'data/MRPC'\
  --output_dir bs200_lr5e-5_ep5\
  --overwrite_output_dir
```