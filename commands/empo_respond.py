import litellm
import os
import re
from ddgs import DDGS


from datetime import datetime

current_date = datetime.now().strftime("%A, %B %d, %Y")  # "Saturday, June 20, 2026"

MODELS = {
    "GEMINI": "gemini/gemini-3.1-flash-lite",
    # "GROQ": "groq/qwen/qwen3.6-27b",
    "GROQ": "groq/llama-3.3-70b-versatile"
    # "GROQ": "groq/compound-beta"
}

suppress_debug_info = True # disables litellm logs in result

def search_web(question):

    try:
        results = DDGS().text(question, max_results=3, region="wt-wt")   # region=wt-wt for worldwide
        all_snippets = ""

        if not results:
            return None
        
        for result in results:
            all_snippets = all_snippets + result["body"] + "\n"
        return all_snippets

    except:
        return None

def strip_thinking_text(response):
    # This is needed so that the response given doesn't include show the THINKING portion of the AI

    # case 1: both <think> and </think> present -> removes everything between them
    response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)
    # case 2: only <think> present, no closing tag -> removes everything from <think> onwards
    response = re.sub(r'<think>.*', '', response, flags=re.DOTALL)

    return response.strip()

def question_response(question):
    provider = os.getenv("PROVIDER")  # reads from .env

    search_results = search_web(question)
    # print(search_results)
    # search_results = None

    response = litellm.completion(
            model=MODELS[provider], 
            messages=[
                {"role": "system", 
                 "content": f"""You are Empo, a terminal AI assistant.                  
                    - Today is {current_date} 
                 Rules:
                    - Answer in 1-3 sentences only
                    - UNLESS the question requires a complete list - then list everything
                    - Answer ONLY what was asked, nothing extra 
                    - No filler words, no fluff, No explanations or sources
                    - If temperature is asked, answer in both degree celsius and fahrenheit
                    - Use search results below for real-time data if needed; Search results:{search_results}
                    - For historical facts, use YOUR OWN KNOWLEDGE, ignore search results
                    - ONLY use search results for real-time data (weather, news, prices, current events)
                    - If all points are equally important, list everything.
                """},

                {"role": "user", "content": question}
            ],
            num_retries=1
        )
    return strip_thinking_text(response.choices[0].message.content)

