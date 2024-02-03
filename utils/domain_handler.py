from utils import logger


def get_media_name(url: str) -> str:
    """
    extracts media name from URL

    Args:
        url (str): URL of the news article

    Returns:
        str: name of the news media
    """
    try:
        # fetching string till media name e.g. https://www.news18
        media_name_with_prefix = url[:url.find(".co")]
        # fetching only media name i.e. string after last (.)
        media_name = media_name_with_prefix[media_name_with_prefix.rindex(".")+1:]
        return media_name
    except Exception as e:
        logger.log_message(
            message="Could not fetch media name: " + str(e.args), level=40)