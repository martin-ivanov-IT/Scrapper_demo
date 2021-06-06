import requests
from html import unescape
from bs4 import BeautifulSoup


class WebScrapper:

    @classmethod
    def fetch_html(cls, url):
        html = requests.get(url).text
        return html

    @classmethod
    def get_soup(cls, url=None, html=None, request_args=None):
        html = cls.fetch_html(url)

        return BeautifulSoup(html, "lxml")

    @classmethod
    def get_articles_urls(cls, soup, atr, classAtr, articlesNeeded):
        return soup.find_all(atr, class_= classAtr)[:articlesNeeded]

    @classmethod
    def get_content(cls, soup, atr, classAtr):
        text = soup.find(atr, class_=classAtr).get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

    @classmethod
    def get_title(cls, soup, atr):
        title = soup.find(atr).text
        return title

    def get_date(self, soup, atr, classAtr):
        date = soup.find(atr, class_=classAtr).text
        return date
