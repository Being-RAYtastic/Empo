import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

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
    "|",
    "Wikipedia"
]
def getMainBoxResult(query, search_engine="google"):
    if search_engine == None:
        # Sets the default searchengine 
        search_engine = "google"
        
    if search_engine == "google":
        url = f"https://google.com/search?q={query}"

        # Sending HTTP request
        response = requests.get(url)

        # Pulling HTTP data from internet
        soup = BeautifulSoup(response.text, "html.parser")

        #! The mainBox class -> "BNeawe"
        result = soup.find("div", class_='BNeawe').text

        if any(excluded_word in result for excluded_word in excluded_words ):
            # It will return nothing if any of the excluded_name from excluded_words[] is present
            return

        return print(result)
    
    elif search_engine == "duckduckgo":
        with DDGS() as ddgs:
            for r in ddgs.answers(query):
                try: 
                    return print(r["text"])
                except Exception:
                    return print(r)

