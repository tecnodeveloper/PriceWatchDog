import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
result = soup.find(id="ResultsContainer")
job_cards = result.find_all("div", class_="card-content")
for job_card in job_cards:
    print(job_card, end="\n" * 2)