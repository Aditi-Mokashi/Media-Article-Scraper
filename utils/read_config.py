import json

from utils import logger


def get_config_data() -> list:
    """
    reads config.json file to get URLs of news articles

    Returns:
        list: list of URLs of news articles
    """
    try:
        with open("config.json", 'r') as f:
            data = json.load(f)
        return data['urls']
    except IOError as e:
        logger.log_message(message=f"Error while reading file: {e.args}", level=40)