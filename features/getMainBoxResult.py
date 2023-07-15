import requests
# from bs4 import BeautifulSoup
from googlesearch import search

'''
It scrapes the info that comes on the main page of the google
'''
excluded_words = [
    ".com",
    ".org",
    ".in",
    ".net",
    ".int",
    ".gov",
    ".edu",
    "See results about",
    "|"
]
def getMainBoxResult(query):
    # url = f"https://google.com/search?q={query}"

    # # Sending HTTP request
    # response = requests.get(url)

    # # Pulling HTTP data from internet
    # soup = BeautifulSoup(response.text, "html.parser")

    # #! The mainBox class -> "BNeawe"
    # result = soup.find("div", class_='BNeawe').text
    results = search(query, advanced=True, num_results=1)
    for x in results:
        result =  x.description + f"\nSource: {x.url}"
    # if any(excluded_word in result for excluded_word in excluded_words ):
    #     # It will return nothing if any of the excluded_name from excluded_words[] is present
    #     return
    
    return print(result)