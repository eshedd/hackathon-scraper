from bs4 import BeautifulSoup

import requests

url = "hackathons.hackclub.com/"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

#nameList = soup.select('#___gatsby > div > div > div > div > a > div > h3')
#
#for name in nameList:
#    print(name.text)

dateList = soup.select('#___gatsby > div > div > div > div > a > div > div:nth-of-type(3) > p:nth-of-type(1)')

for date in dateList:
    print(date.text)