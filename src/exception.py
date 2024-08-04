import sys
from src.logger import logging

# Function to extract detailed error messages
def error_message_detail(error,error_detail:sys):

    # Extract the traceback object
    _,_,exc_tb = error_detail.exc_info()

    # Get the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a detailed error message including the filename, line number, and error message
    error_message = f"Error Occurred in python script {file_name}, line number {exc_tb.tb_lineno} and error message is {str(error)}"

    return error_message

# Custom exception class
class CustomException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) # Initialize the base Exception class

        # Generate a detailed error message using the provided error and error detail
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    # Return the detailed error message when the exception is printed
    def __str__(self):
        return self.error_message