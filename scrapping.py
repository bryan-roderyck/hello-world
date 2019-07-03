import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.jobs.mu/")
r.content
soup = BeautifulSoup(r.content)
print (soup.prettify())
soup.find_all("a")
for link in soup.find_all("a"):
  print (link.get("href"))
