from googlesearch import search
from bs4 import BeautifulSoup as bs
import requests
import os

import time

start_time = time.time()


# Get the links
def ScrapeLink(query):
    result = search(query, stop=40, pause=2)

    return result


# Get the HTML from the link
def getLinkData(link):
    response = requests.get(link)

    HTMLtxt = bs(response.text, 'html.parser')

    return HTMLtxt


# Write the HTML to a file and put inside directory
def writeToFile(data, index):
    # Declaring the path
    parentDir = "SearchResults/"
    # dirName = "Link" + index
    filename = "Link" + index + ".txt"

    # fullPath = os.path.join(parentDir, dirName)

    # Creating directory
    # if not os.path.exists(fullPath):
    # os.mkdir(fullPath)

    # Creating the file
    f = open(parentDir + filename, "w+")
    try:
        f.write(str(data.html.encode('utf8')))
    except AttributeError:
        print("Webpage Null")


if __name__ == "__main__":

    # Search Keyword
    Keyword = "how to data engineering"

    # Get the links and store in result
    result = ScrapeLink(Keyword)
    print(result)
    print("Links found in --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # Iterate through the links
    i = 1
    for links in result:
        fileTxt = getLinkData(links)
        writeToFile(fileTxt, str(i))
        i += 1

    print("Stored in file in --- %s seconds ---" % (time.time() - start_time))
