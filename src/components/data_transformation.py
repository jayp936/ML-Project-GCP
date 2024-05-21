from sklearn.preprocessing import StandardScaler, OneHotEncoder
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        try:
            numerical_features = ['writing_score','reading_score']
            categorical_features = ['gender','race_ethnicity','parental_level_of_education','lunch','test_preparation_course']
            numerical_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )
            
            categorical_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder',OneHotEncoder()),
                    ('scaler',StandardScaler())
                ]
            )
            logging.info('Numerical Columns Standard Scaling completed')
            logging.info('Categorical Columns Encoding completed')
            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', numerical_pipeline,numerical_features)
                    ('categorical_pipeline',categorical_pipeline,categorical_features)
                ]
            )
            return preprocessor
        
        
        except Exception as e:
            raise CustomException(e,sys)
    

    def initiate_data_transformation(self,train_path,test_path):
                try:
                    train_df = pd.read_csv(train_path)
                    test_df = pd.read_csv(test_path)
                    logging.info('read train and test data completed')
                    logging.info('obtaining preprocessing object')
                    preprocessing_object = self.get_data_transformer_object()

                    target_column_name = 'math_score'
                    numerical_features = ['writing_score','reading_score']
                    input_features_train_df = train_df.drop(columns=[target_column_name],axis=1)

                    save_object(
                         file_path = self.data_transformation_config.preprocessor_obj_file_path,
                         obj = preprocessing_object
                    )
                    
                except:
                    pass