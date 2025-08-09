#Output of the Data Ingestion component should be the train and test file paths, which is created in the artifact_entity file (current)
import os
import sys
from networksecurity.compnonents import data_ingestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_file_path:str 
    test_file_path:str 

