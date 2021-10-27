from googlesearch import search
from bs4 import BeautifulSoup as bs
import requests
import os

import time


# Get the links
def ScrapeLink(query, amount):
    result = search(query, stop=amount, pause=2)

    return result


# Get the HTML from the link
def getLinkData(link):
    response = requests.get(link)

    HTMLtxt = bs(response.text, 'html.parser')

    return HTMLtxt


# Breaking the webpage to chunks for improving time complexity.
def getChunks(link):
    chunks = link.find_all('h2')
    return chunks


# Write the HTML to a file and put inside directory
def writeToFile(data, index):
    # Declaring the paths
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


def readAndSaveLinksHTML(scrapedLinks):
    # Iterate through the links
    i = 1
    for links in scrapedLinks:
        start_time = time.time()

        # Get the full HTML file
        fileTxt = getLinkData(links)
        # Get chunks from the file by H2 tag
        print(getChunks(fileTxt))
        # Write to files
        #writeToFile(fileTxt, str(i))
        i += 1

        print("Stored in file in --- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    # Search Keyword
    Keyword = "how to data engineering"
    # Number of Links wanted
    number_of_links = 1

    # Get the links and store in result
    result = ScrapeLink(Keyword, number_of_links)

    readAndSaveLinksHTML(result)
