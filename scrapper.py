import requests
from bs4 import BeautifulSoup

URL = "https://www.scrapethissite.com/pages/simple/"
s = requests.Session()


r = s.get(URL)

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

classe_precise = soup.find_all("h3", class_="country-name")

for element in classe_precise: 
    print(element.text)