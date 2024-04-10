from src.logger import logging
from src.exceptions import CustomeException
from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
import sys
class DataIngestion_Pipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config_manager = ConfigurationManager()
            config=config_manager.get_dataIngestionConfig()
            data_ingestion = DataIngestion(config)
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise CustomeException(e,sys)