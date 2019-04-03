from bs4 import BeautifulSoup

import requests

import sys

def scrape():

    url = "http://hackathons.hackclub.com/"

    r = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    #try to get list of hackathon names and print them

    try:
        nameList = soup.select('#___gatsby > div > div:nth-of-type(2) > div > div > a > div > [class*="sc-"]:nth-of-type(1)')
        
        #deleting unwanted filler stuff in nameList
        nameList = nameList[1::2]
        
#        for name in nameList:
#            print(name.text)
    except IndexError:
        print('No matching element found.')

    #try to get list of hackathon dates and print them
    try:
        dateList = soup.select('#___gatsby > div > div:nth-of-type(2) > div > div > a > div > [class*="sc-"] > p:nth-of-type(1)')
#        for date in dateList:
#            print(date.text)
    except IndexError:
        print('No matching element found.')

    #try to get list of hackathon places and print them
    try:
        placeList = soup.select('#___gatsby > div > div:nth-of-type(2) > div > div > a > div > [class*="sc-"] > p:nth-of-type(2)')
    #    for place in placeList:
    #        print(place.text)
    except IndexError:
        print('No matching element found.')

    print(len(nameList),
    len(dateList),
    len(placeList))

    for index,x in enumerate(nameList):
        print(nameList[index].text)
        print(dateList[index].text)
        print(placeList[index].text)
scrape()