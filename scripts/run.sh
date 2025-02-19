#!/bin/bash
python data_ingestion/ingestion.py &
python model_training/train.py &
python hyperparameter_tuning/tune.py &
python model_serving/serve.py
