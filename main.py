import argparse
import module  # This will not link correctly if you use from imports
from module.web_scraper import WebScrapper
import csv
import codecs
import requests


FILENAME = "test.csv"
ENCODING = 'utf-16'

with codecs.open(FILENAME, "w", ENCODING) as fp:
    web_scrapper = WebScrapper()
    writer = csv.writer(fp)
    soup = web_scrapper.get_soup("https://blog.bozho.net/")
    articlesUrls = web_scrapper.get_articles_urls(soup, 'a', 'more-link', 3)

    for article in articlesUrls:
        currUrl = article['href']
        # print(requests.get(currUrl).text)
        articleSoup = web_scrapper.get_soup(currUrl)
        title = web_scrapper.get_title(articleSoup, 'h1')
        content = web_scrapper.get_content(articleSoup, 'div', 'post-content')
        date = web_scrapper.get_date(articleSoup, 'time', 'entry-date published updated')
        print(title.upper())
        print(article['href'])
        print(content)
        print(date)
        writer.writerow([title, date, content])
fp.close()

print("-----------")
with codecs.open(FILENAME, "r", ENCODING) as fp:
    csv_reader = csv.reader(fp)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)