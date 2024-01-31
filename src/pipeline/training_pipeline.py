import os
import sys
import numpy as np
import pandas as pd

from src.logger.logging import logging
from src.exception.exception import customexception
from src.components.data_ingestion_01 import DataIngestion
from src.components.data_transformation_02 import DataTransformation
from src.components.model_trainer_03 import ModelTrainer
from src.components.model_evaluation_04 import ModelEvaluation


data_ingestion_obj=DataIngestion()
train_data_path,test_data_path=data_ingestion_obj.initiate_data_ingestion()

data_transformation_obj=DataTransformation()
train_arr,test_arr=data_transformation_obj.initiate_data_transformation(train_data_path,test_data_path)


model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)

model_eval_obj = ModelEvaluation()
model_eval_obj.initiate_model_evalution(train_arr, test_arr)