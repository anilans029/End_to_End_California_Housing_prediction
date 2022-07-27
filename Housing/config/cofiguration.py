from Housing.entity.config_entity import *
from Housing.utils.util import read_yaml_file
import os
from Housing.constant import *
from Housing.exception import HousingException
from Housing.logger import logging
import sys


class Configuration:


    def __init__(self,
        config_file_path:str =CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP
        ) -> None:
        try:
            self.config_info  = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_ingestioin_config(self) -> DataIngestionConfig:
        try:
            config_info= self.config_info
            data_ingestion_config = config_info[DATA_INGESTION_CONFIG_KEY]
            training_pipeline_dir = self.training_pipeline_config.artifact_dir

            dataset_download_url = data_ingestion_config[DATA_INGESTION_DATASET_DOWNLOAD_URL_KEY]


            tgz_download_dir_path= os.path.join(training_pipeline_dir,DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY)

            raw_data_dir = os.path.join(training_pipeline_dir,DATA_INGESTION_RAW_DATA_DIR_KEY)

            data_ingestion_config_dir = data_ingestion_config[DATA_INGESTION_INGESTED_DIR_KEY]
            ingested_train_dir=  data_ingestion_config[DATA_INGESTION_INGESTED_TRAIN_DIR_KEY]
            ingested_train_path = os.path.join(training_pipeline_dir,data_ingestion_config_dir,ingested_train_dir)
        
            ingested_test_dir=  data_ingestion_config[DATA_INGESTION_INGESTED_TEST_DIR_KEY]
            ingested_test_path = os.path.join(training_pipeline_dir,data_ingestion_config_dir,ingested_test_dir)

            data_ingestion_config = DataIngestionConfig(dataset_download_url=dataset_download_url,
                                tgz_download_dir=tgz_download_dir_path,
                                raw_data_dir=raw_data_dir,
                                ingested_train_dir=ingested_train_path,
                                ingested_test_dir=ingested_test_path
                                )

            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        
        except Exception as e:
            logging.exception(HousingException(e,sys))
            raise HousingException(e,sys) from e



    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self)-> DataTranformationConfig:
        pass

    def get_model_trainer_config(self)-> ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self)-> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self)->ModelPushConfig:
        pass

    def get_training_pipeline_config(self) ->TrainingPipelingConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelingConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e
