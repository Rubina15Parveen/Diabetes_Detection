import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("results","train.csv")
    test_data_path: str=os.path.join("results","test.csv")
    raw_data_path: str=os.path.join("results","data.csv")

class DataIntegration:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method or component")
        try:
            df = pd.read_csv("Notebook and data/diabetes_dataset_with_notes.csv")
            logging.info("Read dataset as data frame")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("---------------Train test split began------------")
            train, test = train_test_split(df,test_size=0.2, random_state=12)

            train.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("-------------Ingestion of data completes here----------------------")
            return(
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise   CustomException(e,sys)
        

