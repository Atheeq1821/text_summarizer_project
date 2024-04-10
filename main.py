from src.pipeline.data_ingestion_pipeline import DataIngestion_Pipeline
from src.logger import logging
from src.exceptions import CustomeException
import sys

STAGE_NAME= "DATA INGESTION"

try:
    logging.info(" <<<<<< Data Ingestion Started >>>>>>>>>>>>>>>>")
    data_ingestion = DataIngestion_Pipeline()
    data_ingestion.main() 
    logging.info(" <<<<<< Data Ingestion Completed >>>>>>>>>>>>>>>>")
except Exception as e:
    raise CustomeException(e,sys)
