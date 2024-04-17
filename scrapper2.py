import requests
from bs4 import BeautifulSoup

URL = "https://www.scrapethissite.com/pages/simple/"
s = requests.Session()


r = s.get(URL)

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

classe_pays = soup.find_all("h3", class_="country-name")
classe_capital = soup.find_all("span", class_="country-capital")

for pays, capital in zip(classe_pays, classe_capital):
    print("Pays :", pays.text, "- Capitale :", capital.text)