# Import the modules
import pandas as pd
import numpy as np
import os
import sys
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# Configuration class for data transformation
@dataclass
class DataTransformationConfig:
    # Path to save the preprocessor object
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")


class DataTransformation:

    def __init__(self):
        # Initialize the data transformation configuration
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        
        """
        This function creates and returns a ColumnTransformer object which applies
        OneHotEncoding to categorical features and StandardScaling to numerical features.
        """

        try:
            logging.info("Data Transformation Started")

            # Define the list of categorical and numerical features
            categorical_feature = ['TypeofContact', 'Occupation', 'ProductPitched', 'MaritalStatus','Designation']
            
            numerical_feature = ['Age', 'CityTier', 'DurationOfPitch', 'NumberOfFollowups','PreferredPropertyStar', 'NumberOfTrips', 'Passport',
                                'PitchSatisfactionScore', 'OwnCar', 'MonthlyIncome', 'TotalVisiting']
            
            # Initialize the StandardScaler for numeric features
            sc = StandardScaler()
            # Initialize the OneHotEncoder for categorical features
            ohe = OneHotEncoder()

            # Create a ColumnTransformer to apply different preprocessing steps to different types of features
            ct = ColumnTransformer(
                [
                    ("OneHotEncoder",ohe,categorical_feature), # Apply OneHotEncoder to categorical features
                    ("StandardScaler",sc,numerical_feature) # Apply StandardScaler to numeric features
                ]
            )

            logging.info("Data Transformation Stage Completed..")

            return ct # Return the ColumnTransformer object

        except Exception as e:
            logging.info("Exception occured in Data Transformation Stage.")
            raise CustomException(e,sys) # Raise a custom exception if any error occurs
        

    def initiate_data_transformation(self,train_data_path,test_data_path):

        """
        This function reads the train and test datasets, applies the preprocessing transformations,
        and saves the transformed datasets and the preprocessor object.
        """

        try:
            logging.info("Read Train and Test Data")
            # Read train and test datasets
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info("Getting Preprocessing Object")

            preprocessing_obj = self.get_data_transformation_object() # Get the ColumnTransformer object

            logging.info("Splitting into Train and Test Data")

            # Split the train data into input features and target feature
            input_feature_train_df = train_df.drop("ProdTaken",axis=1)
            target_feature_train_df = train_df["ProdTaken"]

            # Split the test data into input features and target feature
            input_feature_test_df = test_df.drop("ProdTaken",axis=1)
            target_feature_test_df = test_df["ProdTaken"]

            logging.info("Applied Data Transformation in the train and test data!!")

             # Apply the transformations to the train and test input features
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            logging.info("Combine the transformed input features and target feature for train and test data!!")
            # Combine the transformed input features and target feature for train and test data
            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            logging.info("Save the preprocessor object to the specified file path!!")
            # Save the preprocessor object to the specified file path
            save_object(
                filepath=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            # Return the transformed train and test arrays and the path to the preprocessor object
            return ( 
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys) # Raise a custom exception if any error occurs

