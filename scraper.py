from bs4 import BeautifulSoup

import requests

import sys

class Hackathon:
    def __init__(self, name, date, place):
        self.name = name
        self.date = date
        self.place = place
        
def hackclub():
    url = "http://hackathons.hackclub.com/"

    r = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    #try to get list of hackathon names and print them
    try:
        nameList = soup.select('#___gatsby > div > div:nth-of-type(2) > div > div > a > div > [class*="sc-"]:nth-of-type(1)')

        #deleting unwanted img(?) between each title in nameList
        nameList = nameList[1::2]

    #        prints all the names in nameList
    #        for name in nameList:
    #            print(name.text)
    except IndexError:
        print('No matching element found.')

    #try to get list of hackathon dates and print them
    try:
        dateList = soup.select('#___gatsby > div > div:nth-of-type(2) > div > div > a > div > [class*="sc-"] > p:nth-of-type(1)')
    #        prints all the dates in dateList
    #        for date in dateList:
    #            print(date.text)
    except IndexError:
        print('No matching element found.')

    #try to get list of hackathon places and print them
    try:
        placeList = soup.select('#___gatsby > div > div:nth-of-type(2) > div > div > a > div > [class*="sc-"] > p:nth-of-type(2)')
    #    prints all the places in placeList
    #    for place in placeList:
    #        print(place.text)
    except IndexError:
        print('No matching element found.')


    #prints how many names, dates, and places were scraped
    #print("Names:", len(nameList), " Dates:", len(dateList), " Places:", len(placeList))

    #fills hack list with hackathon objects
    hackathons = []
    for index,x in enumerate(nameList):
        hack.append(Hackathon(nameList[index].text,dateList[index].text,placeList[index].text))

    return hackathons


