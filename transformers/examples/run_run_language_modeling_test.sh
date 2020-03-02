export TRAIN_FILE=data/sogou/train_test.txt
export TEST_FILE=data/sogou/valid_test.txt

python run_language_modeling_test.py \
    --output_dir=output \
    --model_type=gpt2 \
    --model_name_or_path=gpt2 \
    --config_name=output_test \
    --tokenizer_name=output_test \
    --do_train \
    --train_data_file=$TRAIN_FILE \
    --do_eval \
    --eval_data_file=$TEST_FILE