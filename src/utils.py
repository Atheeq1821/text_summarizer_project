
#constants

from pathlib import Path

CONFIG_FILE = Path("config/config.yaml")
PARAMS_FILE = Path("params.yaml")


#read yaml

from src.logger import logging
import yaml
from src.exceptions import CustomeException
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
import os
import sys

@ensure_annotations # To ensure the input datatype 
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logging.info(f"yaml file from {yaml_file} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomeException(e,sys)
