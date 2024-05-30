# utils/logging_config.py
import logging

def configure_logging():
    logging.basicConfig(
        filename='logs/automation.log',
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    return logging.getLogger('LANAutomation')

# Create logger object
logger = configure_logging()
