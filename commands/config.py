import questionary
from dotenv import set_key


def run_config(CONFIG_FILE):
    print("Welcome to the Empo Configurator!")

    provider = questionary.select(
        "Select your AI provider:",
        choices=["Gemini", "Groq"]
    ).ask()
    # print(f"You selected: {provider}")
    set_key(CONFIG_FILE, "PROVIDER", provider.upper())

    api_key = questionary.password("Enter your API key (Press Enter to keep using existing one): ").ask()
    # print(f"Your API key is: {api_key}")

    if not str(api_key).strip(): 
        pass
    else: 
        set_key(CONFIG_FILE, f"{str(provider).upper()}_API_KEY", api_key)

    return provider