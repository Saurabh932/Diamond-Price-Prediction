import os
import sys
import numpy as np
import pandas as pd

from src.logger.logging import logging
from src.exception.exception import customexception

from dataclasses import dataclass
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

@dataclass
class DataTransformationConfig:
    pass

class DataTransformation():
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)