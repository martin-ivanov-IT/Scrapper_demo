from bs4 import BeautifulSoup
import requests
import csv
import codecs

# csv_file = open('cms_scrape2.csv', 'w', encoding='utf-8')
# csv_writer = csv.writer(csv_file)

FILENAME = "test.csv"
ENCODING = 'utf-16'

with codecs.open(FILENAME, "w", ENCODING) as fp:
    writer = csv.writer(fp)

    source = requests.get("https://www.travelsmart.bg//").text
    soup = BeautifulSoup(source, 'lxml')
    for article in soup.find_all('a', class_='fusion-read-more')[:3]:
        currUrl = article['href']
        currSource = requests.get(currUrl).text
        currSoup = BeautifulSoup(currSource, 'lxml')
        content = currSoup.find('div', class_='fusion-text fusion-text-1')
        title = currSoup.find('h1').text
        text = currSoup.find('div', class_='fusion-text fusion-text-1').get_text()
        dateContent = currSoup.find('span', class_='updated rich-snippet-hidden').text
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        print(title.upper())
        print(article['href'])
        print(text)
        print(dateContent)
        writer.writerow([title, dateContent, text])
fp.close()
print("-----------")
with codecs.open(FILENAME, "r", ENCODING) as fp:
    csv_reader = csv.reader(fp)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)