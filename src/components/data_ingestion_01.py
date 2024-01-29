import os
import sys
import numpy as np
import pandas as pd

from src.logger.logging import logging
from src.exception.exception import customexception

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts", "raw.csv")
    train_data_path:str = os.path.join("artifacts", "train.csv")
    test_data_path:str = os.path.join("artifacts", "test.csv")

class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            data = pd.read_csv("dataset/train.csv")
            logging.info("Reading dataframe")
            
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(" I have saved the raw dataset in artifact folder")

            logging.info("Performing train_test_split")
            train_data, test_data = train_test_split(data, test_size=0.30)
            logging.info("Successfully performed train test split")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data Ingestion has Completed.")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info()
            raise customexception(e, sys)
        

if __name__ == "__main__":
    
    obj=DataIngestion()
    obj.initiate_data_ingestion()