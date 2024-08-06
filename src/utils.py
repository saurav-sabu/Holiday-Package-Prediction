# Import the modules
import os
import sys
import pandas as pd
import numpy as np
import pickle

from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

def save_object(filepath,obj):
    """
    This function saves a given object to a specified file path using pickle.
    """
    try:
        # Get the directory path from the file path
        dir_path = os.path.dirname(filepath)

        # Create the directory if it does not exist
        os.makedirs(dir_path,exist_ok=True)

        # Save the object to the specified file path using pickle
        with open(filepath,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys) # Raise a custom exception if any error occurs
    

def evaluate_model(X_train,y_train,X_test,y_test,models):

    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]

            model.fit(X_train,y_train)

            y_test_pred = model.predict(X_test)

            test_model_score = accuracy_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score

            return report
        
    except Exception as e:
        raise CustomException(e,sys)




