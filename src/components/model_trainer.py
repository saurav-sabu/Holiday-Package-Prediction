import os
import sys
import numpy as np
import pandas as pd

from src.logger import logging
from src.exception import CustomException

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier

from src.utils import save_object, evaluate_model
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,train_arr,test_arr):

        try:
            logging.info("Model Training Started")

            X_train,y_train,X_test,y_test = (train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1])

            models = {
                "RF":RandomForestClassifier(),
                "DC":DecisionTreeClassifier(),
                "LR":LogisticRegression(),
                "KNN":KNeighborsClassifier(),
                "ADA":AdaBoostClassifier(),
                "SVC":SVC()
            }

            model_report = evaluate_model(X_train,y_train,X_test,y_test,models)

            logging.info(f"Model Report: {model_report}")

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            logging.info(f"Best Model : {best_model_name} and Best Accuracy Score : {best_model_score}")

            save_object(
                filepath= ModelTrainerConfig.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            raise CustomException(e,sys)