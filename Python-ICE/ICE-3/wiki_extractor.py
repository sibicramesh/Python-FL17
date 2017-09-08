import requests
from bs4 import BeautifulSoup

# URl link
url = "https://en.wikipedia.org/wiki/Hurricane_Irma"

# Get the content and store it in variable
source = requests.get(url)

text = source.text

# Parse the html content using beautifysoup
beautify = BeautifulSoup(text, "html.parser")


# Function to extract header
def headerExtractor():
    result = beautify.findAll("head")

    for i in result:
        print(i.text)


# Function to extract body
def bodyExtractor():
    result = beautify.findAll("body")

    for i in result:
        r1 = i.find("p")
        print(r1.text)


print("******* HEADER ********")
headerExtractor()
print("******* BODY **********")
bodyExtractor()
