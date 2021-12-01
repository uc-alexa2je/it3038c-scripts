from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://analytics.usa.gov').content
soup =BeautifulSoup(r, "lxml")
print(type(r))
print(type(soup))
print(soup.prettify()[:100])
