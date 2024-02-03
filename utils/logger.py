import logging


def log_message(message: str, level: int):
    """
    logs success/failure messages

    Args:
        message (str): message to log
        level (int): severity level (debug=10, info=20, warning=30, error=40, critical=50)
    """
    logging.basicConfig(filename="logger.log",
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        level=logging.INFO)
    
    if level == 10:
        logging.debug(msg=message)
    elif level == 20:
        logging.info(msg=message)
    elif level == 30:
        logging.warning(msg=message)
    elif level == 40:
        logging.error(msg=message)
    elif level == 50:
        logging.critical(msg=message)