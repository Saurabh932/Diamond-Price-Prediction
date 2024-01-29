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


obj=DataIngestion()

train_data_path,test_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initiate_data_transformation(train_data_path,test_data_path)


model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)

