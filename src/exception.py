import sys
import logging, logger

def error_msg_detail(error, error_detail: sys):
    _, _, exe_tb = error_detail.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exe_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_detail(error_msg, error_detail)
        logging.info(self.error_msg)
        
    def __str__(self):
        return self.error_msg
        
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        # logging.info("This is a sample log test in exception.py")
        raise CustomException(e, sys)
