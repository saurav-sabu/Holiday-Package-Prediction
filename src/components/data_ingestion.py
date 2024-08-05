# Importing the modules
import os
import sys
import pandas as pd

from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException

# Data class for defining the configuration of data ingestion paths
@dataclass
class DataIngestionConfig:

    train_data_path : str = os.path.join("artifacts","train.csv")
    test_data_path : str = os.path.join("artifacts","test.csv")
    raw_data_path : str = os.path.join("artifacts","raw.csv")


# Class for handling the data ingestion process
class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # Initialize the data ingestion configuration

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Method Started") # Log the start of the data ingestion process

        try:
            df = pd.read_csv(os.path.join("notebooks/data","cleaned_travel_data.csv"))
            logging.info("Data Loaded")  # Log that data has been successfully loaded

            # Create the directory for raw data if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            # Save the raw data to a CSV file
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Raw Data Created") # Log that raw data has been successfully created

            # Split the dataset into training and testing sets
            train_set, test_set = train_test_split(df,test_size=0.3,random_state=42)

            # Save the training data to a CSV file
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)      

            # Save the testing data to a CSV file      
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Data Ingestion Stage completed..") # Log that data ingestion has been successfully completed

            # Return the paths to the training and testing data files
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("Exception occurred at Data Ingestion Method") # Log any exceptions that occur during data ingestion
            raise CustomException(e,sys) # Raise a custom exception with the error details




