import sys 
from .logger import logging

def error_msg_detail(error,error_detail:sys):
    """
    This function is used to format the error message with details.
    """
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_msg_detail(error_message, error_detail)
        
    def __str__(self):
        return self.error_message
   
#only to check wether this file is working or not    
'''if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by Zero Error")
        raise CustomException(e,sys)'''