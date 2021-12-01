import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.microcenter.com/product/623048/intel-core-i7-10700k-comet-lake-38ghz-eight-core-lga-1200-boxed-processor-heatsink-not-included").content
soup = BeautifulSoup(data,'html.parser')

##details = soup.findAll("div",{"class":re.compile('(total-wrapper)')})
details = soup.find("h1")

subjectspan = ""

for d in details:
    title = d.find("span")
    if title is not None and title != -1:
        subjectspan = title

print("The %s price is listed at %s. "% (subjectspan.get('data-name'), subjectspan.get('data-price')))
