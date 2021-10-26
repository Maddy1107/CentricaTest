from googlesearch import search
from bs4 import BeautifulSoup as bs
import requests
import urllib


# Get the links
def ScrapeLink(query):
    result = search(query, tld="com", num=2, stop=2, pause=2)
    return result


# Get the HTML from the link
def getLinkData(link):
    response = requests.get(link)
    HTMLtxt = bs(response.text, 'html.parser')
    return HTMLtxt, HTMLtxt.title.text


# Write the HTML to a file
def writeToFile(title, data):
    print(type(title))
    filename = title + ".txt"
    f = open(filename, "w+")
    f.write(str(data.html.encode('utf8')))


if __name__ == "__main__":

    # Search Keyword
    Keyword = "how to data engineering"

    # Get the links and store in result
    result = ScrapeLink(Keyword)

    # Iterate through the links
    for j in result:
        fileTxt, t = getLinkData(j)
        writeToFile(t, fileTxt)

    print(t)
