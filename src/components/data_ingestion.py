import os
import zipfile
from src.logger import logging
from src.utils import *
from src.components.entity import DataIngestionConfig
from pathlib import Path
from src.config.configuration import ConfigurationManager
class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config=config
    def extract_zip_file(self):
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir,exist_ok=True)
        logging.info("folder exist or created")
        logging.info(f"Extracting zip file from {self.config.data_zip_file} to {unzip_dir}")
        with zipfile.ZipFile(self.config.data_zip_file, 'r') as zip_ref:
            zip_ref.extractall(path=unzip_dir)
