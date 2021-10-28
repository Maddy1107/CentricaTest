# CentricaTest

The following project is made in python where the code searches in Google and retrieves the first 5 links of the results.

How it works?

The code is divided in functions. 
 
ScrapeLink searches in google and returns 5 links.

getLinkHTMLData gets the HTML code from every link.

checkForInvalidName checks if the title has any special character.

readAndSaveLinksHTML reads the HTML code and saves in a file.

Commented data in the script is a way to minimise the run time by dividing the HTML code to chunks and save in separate file.