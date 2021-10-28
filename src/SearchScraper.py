from googlesearch import search
from bs4 import BeautifulSoup as bs
import requests
import os
import re


# Get the links
def ScrapeLink(query, amount):
    result = search(query, stop=amount, pause=2)

    return result


# Get the HTML from the link
def getLinkHTMLData(link):
    response = requests.get(link)

    HTMLtxt = bs(response.text, 'html.parser')

    return HTMLtxt, HTMLtxt.title.text


# --------------Code to minimize the run time by creating chunks---------------------
# # Breaking the webpage to chunks for improving time complexity.
# def getChunks(link):
#     try:
#         chunks = link.find_all('h2')
#         return chunks
#     except AttributeError:
#         print("No H2 tags")


def checkForInvalidName(name):
    invalid_symbols = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if invalid_symbols.search(name) is not None:
        name = re.sub(invalid_symbols, '', name)
    return name


# Write the HTML to a file and put inside directory
def writeToFile(data, FileTitle):
    # Declaring the paths
    parentDir = 'SearchResults/'

    # dirName = checkForInvalidName(PageTitle)

    if FileTitle is not None:
        filename = checkForInvalidName(FileTitle) + '.txt'
    else:
        filename = 'Link.txt'

    fullPath = os.path.join(parentDir, filename)

    # Creating the file
    f = open(fullPath, "w+")

    try:
        f.write(str(data.html.encode('utf8')))
    except AttributeError:
        print("Webpage Null")

    # --------------Code to create a directory when creating chunks---------------------
    # Creating directory
    # if not os.path.exists(fullPath):
    # os.mkdir(fullPath)


def readAndSaveLinksHTML(scrapedLinks):
    # Iterate through the links
    for links in scrapedLinks:
        # Get the full HTML file
        fileHTMLTxt, FileTitle = getLinkHTMLData(links)

        # Write to files
        writeToFile(fileHTMLTxt, FileTitle)

        # --------------Code to minimize the run time by creating chunks---------------------
        # Get chunks from the file by H2 tag
        # H2tags = getChunks(fileHTMLTxt)
        # for i in H2tags:
        #     FileTitle = i.get_text()
        #     # Write to files
        # writeToFile(fileHTMLTxt, FileTitle, PageTitle)


if __name__ == "__main__":
    # Search Keyword
    Keyword = "how to data engineering"

    # Number of Links wanted
    number_of_links = 1

    # Get the links and store in result
    result = ScrapeLink(Keyword, number_of_links)

    readAndSaveLinksHTML(result)
