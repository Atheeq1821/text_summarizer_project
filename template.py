import os
from pathlib import Path
import logging

from datetime import datetime

# CREATING LOG FILES

log_file= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), 'logs',log_file)
os.makedirs(logs_path,exist_ok=True)

log_file_path = os.path.join(logs_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s" ,
    level=logging.INFO
    )

#Creating list of files

project_name = "TextSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/utils.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    
        ]

# CREATING FILES AND FOLDERS

for file in list_of_files:
    filepath=Path(file)
    folder,filename = os.path.split(filepath)
    if folder!="":
        os.makedirs(folder,exist_ok=True)
    if (not os.path.exists(filename)):
        with open(filepath, "w") as f:
            pass
        logging.info(f"File {filename} created")   
    else:
        logging.info(f"File {filename} already exists")     


if __name__=='__main__':
    logging.info("Logging started")