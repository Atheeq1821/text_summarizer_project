import sys
from src.logger import logging
def handle_exception(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_msg="Error occured in the filename [{0}] in the line number [{1}] and the error is [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    logging.info(error_msg)
    return error_msg

class CustomeException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_message = handle_exception(error_msg,error_details=error_detail)
    def __str__(self):
        return self.error_message
    