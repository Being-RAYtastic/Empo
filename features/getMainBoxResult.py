import requests
from bs4 import BeautifulSoup

'''
It scrapes the info that comes on the main page of the google
'''

def getMainBoxResult(query):
    url = f"https://google.com/search?q={query}"

    # Sending HTTP request
    response = requests.get(url)

    # Pulling HTTP data from internet
    soup = BeautifulSoup(response.text, "html.parser")

    #! The mainBox class -> "BNeawe"
    result = soup.find("div", class_='BNeawe').text

    return print(result)

getMainBoxResult("bday of linus tolvards")


