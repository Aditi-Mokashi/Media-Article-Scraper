import requests
from bs4 import BeautifulSoup

def cnn(url):
    response = requests.get(url)
    if response.status_code == 200:
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

def news18(url: str):
    news = {}
    
    response = requests.get(url=url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        article = [news.text.strip().replace("\n", " ") for news in list(soup.select("article > div > p"))]
        article = " ".join(article)

        news = {
            'url': url,
            'headline': soup.find("h1").text,
            'short_description': soup.find("h2").text,
            'article': article
        }

        return news