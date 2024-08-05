import os
import sys
import pandas as pd

from src.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.logger import logging
from src.exception import CustomException

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    obj1 = DataTransformation()
    train_arr,test_arr,obj_path = obj1.initiate_data_transformation(train_data_path,test_data_path)
