import requests
from bs4 import BeautifulSoup

'''
It scrapes the info that comes on the main page of the google
'''
domain_names = [
    ".com",
    ".org",
    ".in",
    ".net",
    ".int",
    ".gov",
    ".edu",
]
def getMainBoxResult(query):
    url = f"https://google.com/search?q={query}"

    # Sending HTTP request
    response = requests.get(url)

    # Pulling HTTP data from internet
    soup = BeautifulSoup(response.text, "html.parser")

    #! The mainBox class -> "BNeawe"
    result = soup.find("div", class_='BNeawe').text

    if any(domain in result for domain in domain_names ):
        # will return nothing if any of the domain_name from domain_names[] is present
        return
    
    return print(result)




