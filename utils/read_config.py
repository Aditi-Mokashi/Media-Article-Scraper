import json

def get_config_data() -> list:
    """
    reads config.json file to get URLs of news articles

    Returns:
        list: list of URLs of news articles
    """
    with open("config.json", 'r') as f:
        data = json.load(f)
    return data['urls']