from networksecurity.compnonents.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconf = TrainingPipelineConfig()
        data_ing_conf = DataIngestionConfig(trainingpipelineconf)
        data_ing = DataIngestion(data_ing_conf)
        logging.info("Initiate Data Ingestion")
        artif = data_ing.initiate_data_ingestion()
        print(artif) 
    
    except Exception as e:
        raise NetworkSecurityException(e, sys)