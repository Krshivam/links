import requests
from bs4 import BeautifulSoup

url = str(input())
r = requests.get(url)
soup = BeautifulSoup(r.content)
for link in soup.find_all("a"):
    print(link.get("href"))
