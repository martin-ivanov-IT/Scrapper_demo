from bs4 import BeautifulSoup
import requests
import csv
import codecs
from web_scraper import WebScrapper

# csv_file = open('cms_scrape2.csv', 'w', encoding='utf-8')
# csv_writer = csv.writer(csv_file)

FILENAME = "test.csv"
ENCODING = 'utf-16'

with codecs.open(FILENAME, "w", ENCODING) as fp:
    web_scrapper = WebScrapper()
    writer = csv.writer(fp)
    soup = web_scrapper.get_soup("https://www.travelsmart.bg//")
    articlesUrls = web_scrapper.get_articles_urls(soup, 'a', 'fusion-read-more', 20)

    for article in articlesUrls:
        currUrl = article['href']
        articleSoup = web_scrapper.get_soup(currUrl)
        title = web_scrapper.get_title(articleSoup, 'h1')
        content = web_scrapper.get_content(articleSoup, 'div', 'fusion-text fusion-text-1')
        date = web_scrapper.get_date(articleSoup, 'span', 'updated rich-snippet-hidden')
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