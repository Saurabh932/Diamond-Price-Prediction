import os
import sys
import numpy as np
import pandas as pd

from src.logger.logging import logging
from src.exception.exception import customexception
from src.utils import save_object, evaluate_model

from dataclasses import dataclass
from pathlib import Path

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet


@dataclass
class ModelTrainerConfig:
    pass

class ModelTrainer():
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)