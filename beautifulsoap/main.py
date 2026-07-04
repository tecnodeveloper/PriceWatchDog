import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/tag/inspirational/"
# url = "https://www.daraz.pk/products/-i563806129-s2610082283.html?pvid=754560f2-14af-4aa1-a81d-a57fe4194764&search=jfy&scm=1007.51705.413671.0&spm=a2a0e.tm80335142.just4u.d_563806129"
res = requests.get(url)

soup = BeautifulSoup(res.text,"html.parser")
print(soup)
# Get all the paragraphs using for loop
# for para in soup.find_all("p"):
#     print(para.get_text())

# https://realpython.com/beautiful-soup-web-scraper-python/#what-is-web-scraping