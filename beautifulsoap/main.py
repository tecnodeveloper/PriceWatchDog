import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/tag/inspirational/"
res = requests.get(url)

soup = BeautifulSoup(res.text,"html.parser")
print(soup)
# Get all the paragraphs using for loop
# for para in soup.find_all("p"):
#     print(para.get_text())

# https://realpython.com/beautiful-soup-web-scraper-python/#what-is-web-scraping