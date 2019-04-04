from bs4 import BeautifulSoup

import requests

import sys

class Hackathon:
    def __init__(self, name, date, place, link):
        self.name = name
        self.date = date
        self.place = place
        self.link = link
        
def hackclub():
    url = "http://hackathons.hackclub.com/"

    r = requests.get(url)

    data = r.content

    soup = BeautifulSoup(data, "html.parser")

    #try to get list of hackathon names
    try:
        nameList = soup.select('#___gatsby > div > div:nth-of-type(2) > div > div > a > div > [class*="sc-"]:nth-of-type(1)')

        #deleting unwanted img(?) between each title in nameList
        nameList = nameList[1::2]

    #        prints all the names in nameList
    #        for name in nameList:
    #            print(name.text)
    except IndexError:
        print('No matching element found.')

    #try to get list of hackathon dates
    try:
        dateList = soup.select('#___gatsby > div > div:nth-of-type(2) > div > div > a > div > [class*="sc-"] > p:nth-of-type(1)')
    #        prints all the dates in dateList
    #        for date in dateList:
    #            print(date.text)
    except IndexError:
        print('No matching element found.')

    #try to get list of hackathon places
    try:
        placeList = soup.select('#___gatsby > div > div:nth-of-type(2) > div > div > a > div > [class*="sc-"] > p:nth-of-type(2)')
    #    prints all the places in placeList
    #    for place in placeList:
    #        print(place.text)
    except IndexError:
        print('No matching element found.')
    
    #try to get list of hackathon links
    try: 
        linkList = soup.select('#___gatsby > div > div:nth-of-type(2) > div > div > a[href]')
    #    prints all the links in linkList 
    #    for link in linkList:
    #        print(link['href'])
    except IndexError:
        print('No matching element found.')
    

    #prints how many names, dates, and places were scraped
    #print("Names:", len(nameList), " Dates:", len(dateList), " Places:", len(placeList))

    #fills hack list with hackathon objects
    hackathons = []
    for index,x in enumerate(nameList):
        hackathons.append(Hackathon(nameList[index].text,dateList[index].text,placeList[index].text,linkList[index]['href']))
    return hackathons

def hackevents():
    url = "https://hackevents.co/search/anything/anywhere/anytime"

    r = requests.get(url)

    data = r.content

    soup = BeautifulSoup(data, "html.parser")
    
    try:
        nameList = soup.select('body > div.container > div:nth-child(2) > div > a > div > div > div > div > div > div > h3')

        #deleting unwanted img(?) between each title in nameList
#        nameList = nameList[1::2]
        print(nameList)
        for name in nameList:
            print(name.text)
    except IndexError:
        print('No matching element found.')
    
hackclubHacks = hackclub()
hackevents()
