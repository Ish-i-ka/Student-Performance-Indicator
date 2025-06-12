# PROJECT1/main.py

from src.logger import logging
from src.exception import CustomException
import sys

logging.info("Starting the main application.")

def risky_function():
    try:
        result = 10 / 0
        return result
    except Exception as e:
        # Raise your custom exception
        raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        risky_function()
    except CustomException as ce:
        logging.error(ce.error_message)
        print(f"A custom exception was caught: {ce}")

logging.info("Main application has finished.")