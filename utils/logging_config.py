import logging

def setup_logging(log_file='logs/automation.log'):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

# Example usage
if __name__ == "__main__":
    setup_logging()
    logging.info("Logging setup complete")
