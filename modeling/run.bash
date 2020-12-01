#!/bin/bash
for i in {51..63};
do
	python modeling.py --model_name_or_path hfl/chinese-roberta-wwm-ext-large --task_name MRPC  --do_train  --do_eval --do_predict  --max_seq_length 128  --per_device_train_batch_size ${i}  --learning_rate 5e-5  --num_train_epochs 3 --data_dir 'data/MRPC' --output_dir bs${i}_lr5e-5_ep3_large --overwrite_output_dir;
done
