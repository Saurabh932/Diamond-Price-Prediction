import os
import sys
import pickle
import numpy as np

from src.logger.logging import logging
from src.exception.exception import customexception
from src.utils import load_object

from dataclasses import dataclass
from pathlib import Path

from sklearn.metrics import mean_absolute_error, mean_squared_error
from urllib.parse import urlparse

import mlflow
import mlflow.sklearn

@dataclass
class ModelEvalutionConfig:
    pass

class ModelEvalution():
    def __init__(self):
        pass

    def initiate_model_evalution(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)