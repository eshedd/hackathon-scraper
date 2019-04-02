from bs4 import BeautifulSoup

import requests

url = "lite.cnn.io/en/article/h_8bb48757ef80597c3c142ebfe96db668"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

print(soup.(find_all('p')).string)


#for link in soup.find_all('p'):
#    print(link.get('p'))