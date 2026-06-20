from dotenv import load_dotenv
import sys
import os
import litellm

# CUSTOM IMPORTS
from commands.config import run_config
from commands.help import run_help
from commands.empo_respond import question_response

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.empo")
litellm.suppress_debug_info = True



if __name__ == "__main__":
    load_dotenv(CONFIG_FILE, override=True)

    # if no provider set, run config first
    if not os.getenv("PROVIDER"):
        run_config(CONFIG_FILE)
        load_dotenv(CONFIG_FILE, override=True)

    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])  # joins all words after "empo", " " means it will put a space between each word.

        if question == "--config":
            run_config(CONFIG_FILE)

        elif question == "--help":
            run_help()
     
        else:
            try: 
                answer = question_response(question)
                print(answer)
            except Exception as e:
                error = str(e)
    
                if "API key" in error or "api key" in error or "authentication" in error.lower():
                    print("Invalid or missing API key. Run 'empo --config' to update it.")
                elif "429" in error or "rate limit" in error.lower() or "quota" in error.lower():
                    print("Rate limit hit. Wait a moment and try again.")
                elif "connection" in error.lower() or "network" in error.lower():
                    print("No internet connection. Check your network and try again.")
                else:
                    print("Something went wrong. Run 'empo --config' to reconfigure.")

    else:
        print("Type 'empo --help'")
