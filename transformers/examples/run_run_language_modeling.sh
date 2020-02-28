export TRAIN_FILE=/search/odin/guobk/streaming/NLP-Corpus/wikitext-2/wiki.train.tokens
export TEST_FILE=/search/odin/guobk/streaming/NLP-Corpus/wikitext-2/wiki.test.tokens

python run_language_modeling.py \
    --output_dir=output \
    --model_type=gpt2 \
    --model_name_or_path=gpt2 \
    --do_train \
    --train_data_file=$TRAIN_FILE \
    --do_eval \
    --eval_data_file=$TEST_FILE