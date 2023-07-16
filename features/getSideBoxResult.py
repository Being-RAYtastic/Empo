from bs4 import BeautifulSoup
import requests
from duckduckgo_search import DDGS

'''
It scrapes the info that is shown in the right side card/box of the google
'''


def getSideBoxResult(query, search_engine="google"):
    if search_engine == None:
        # Sets the default searchengine 
        search_engine = "google"
    
    if search_engine == "google":
        url = "https://www.google.com/search"
        params = {
            "q": query,
            "hl": "en",
            "gl": "us"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        }

        # Sending HTTP request
        response = requests.get(url, params=params, headers=headers)

        # Pulling HTTP data from internet
        soup = BeautifulSoup(response.text, "html.parser")

        #! Right side Card first description class --> .kno-rdesc
        result = soup.select_one(".kno-rdesc span").text

        return print(result)
    
    elif search_engine == "duckduckgo":
        with DDGS() as ddgs:
            ddgs_gen = ddgs.text(query)
            res = []
            for r in ddgs_gen:
                res.append(r)
            return print(res[0]["body"])