import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

from utils import logger


def cnn(url) -> dict:
    """
    extract articles for cnn news website

    Args:
        url (str): URL of the article

    Returns:
        dict: dictionary containing URL of article, headline, short description and article content
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        article = [p.text.strip().replace("\n", " ").replace("  ", "") for p in list(soup.select(".article__content"))]
        article = " ".join(article)
        news = {
            'url': url,
            'headline': soup.find("h1").text.strip().replace("\n",""),
            'short_description': soup.find("span", attrs={'class':'inline-placeholder','data-editable':'metaCaption'}).text,
            'article': article
        }

        return news
    except HTTPError as e:
        logger.log_message(message=f"Error in while fetching CNN URL: {e.args}", level=40)
    except Exception as e:
        logger.log_message(message=f"Error in CNN: {e.args}", level=40)

def news18(url: str) -> dict:
    """
    extract articles for news18 news website

    Args:
        url (str): URL of the article

    Returns:
        dict: dictionary containing URL of article, headline, short description and article content
    """
    try:
        response = requests.get(url=url)
        soup = BeautifulSoup(response.content, "html.parser")
        article = [news.text.strip().replace("\n", " ") for news in list(soup.select("article > div > p"))]
        article = " ".join(article)

        news = {
            'url': url,
            'headline': soup.find("h1").text,
            'short_description': soup.find("h2").text,
            'article': article
        }
    except HTTPError as e:
        logger.log_message(message=f"Error in while fetching news18 URL: {e.args}", level=40)
    except Exception as e:
        logger.log_message(message=f"Error in news18: {e.args}", level=40)

    return news