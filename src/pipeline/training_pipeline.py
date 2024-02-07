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


'''First to run'''

# data_ingestion_obj=DataIngestion()
# train_data_path,test_data_path=data_ingestion_obj.initiate_data_ingestion()

# data_transformation_obj=DataTransformation()
# train_arr,test_arr=data_transformation_obj.initiate_data_transformation(train_data_path,test_data_path)


# model_trainer_obj=ModelTrainer()
# model_trainer_obj.initate_model_training(train_arr,test_arr)

# model_eval_obj = ModelEvaluation()
# model_eval_obj.initiate_model_evalution(train_arr, test_arr)


'''After then run this'''

class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            data_ingestion=DataIngestion()
            train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
            return train_data_path, test_data_path
        
        except Exception as e:
            raise customexception(e, sys)
        
    def start_data_transformation(self, train_data_path, test_data_path):
        try:
            data_transformation=DataTransformation()
            train_arr,test_arr=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
            return train_arr, test_arr
        
        except Exception as e:
            raise customexception(e, sys)

    def start_model_training(self, train_arr, test_arr):
        try:
            model_trainer_obj=ModelTrainer()
            model_trainer_obj.initate_model_training(train_arr,test_arr)

        except Exception as e:
            raise customexception(e, sys)

    def start_model_evaluation(self, train_arr, test_arr):
        try:
            model_eval_obj = ModelEvaluation()
            model_eval_obj.initiate_model_evalution(train_arr, test_arr)

        except Exception as e:
            raise customexception(e, sys)