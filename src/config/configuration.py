from src.utils import *
from src.components.entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(self,config_file_path=CONFIG_FILE,params_file_path=PARAMS_FILE):
        self.config_file=read_yaml(config_file_path)
        self.params_file=read_yaml(params_file_path)
    def get_dataIngestionConfig(self):
        config=self.config_file.data_ingestion
        data_ingestion_config= DataIngestionConfig(
            root_dir=config.root_dir,
            data_zip_file=config.data_zip_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
