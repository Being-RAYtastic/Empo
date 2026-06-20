# Empo
Your AI-powered search assistant that lives in the terminal.

No browser. No tabs. Just ask.

```bash
empo "age of elon musk"
empo "what are the evolutions of eevee"
empo "what is recursion"
empo "weather of tokyo"
```

---

## Features
- Ask anything directly from your terminal
- Real-time web search via DuckDuckGo - no extra API key needed
- Supports multiple AI providers (for now only two) - bring your own API key
- Works on Linux, macOS and Windows

---

### Supported Providers

| Provider | Model |
|---|---|
| Gemini | gemini-3.1-flash-lite |
| Groq | llama-3.3-70b-versatile |
> NOTE: Devs who want to try out different models, can check ./commands/empo_respond.py file

---

## Installation

### Linux / macOS
```bash
git clone https://github.com/Being-RAYtastic/Empo.git
cd Empo
chmod +x install.sh
./install.sh
```

### Windows (PowerShell)
```powershell
git clone https://github.com/Being-RAYtastic/Empo.git
cd Empo
.\install.ps1
```

The install script will:
- Set up a virtual environment
- Install all dependencies
- Register the `empo` command globally

---

## Setup

On first use, configure your API key and provider:

```bash
empo --config
```

You'll get an interactive prompt to select your provider and enter your API key.

Getting a free API key:
- **Gemini**: [aistudio.google.com](https://aistudio.google.com) (free, no credit card)
- **Groq**: [console.groq.com](https://console.groq.com) (free, no credit card)

---

## Usage
1. Ask Question
```bash
empo "your question here"
```
<br>

2. Change provider or API key
```bash
empo --config
```

<br>

3. Show Help    
```bash        
empo --help                    
```
<br>

> ⚠️ Always wrap your question in quotes, especially if it contains special characters like `?`, `!`, or `&`, etc.
>
> ✅ `empo "what is recursion?"`
>
> ❌ `empo what is recursion`

---

## How It Works

```
empo "question"
```
1. You ask a question
2. Empo searches DuckDuckGo for real-time data
3. AI processes search results combined with its own knowledge
4. Clean, concise answer printed in your terminal



---

## Project Structure

```
Empo/
├── main.py              # entry point
├── install.sh           # Linux/macOS installer
├── install.ps1          # Windows installer
├── requirements.txt     # dependencies
├── .env                 # API key and PROVIDER info 
└── commands/
    ├── config.py        # --config logic
    ├── empo_respond.py  # AI + search logic
    └── help.py          # --help logic
```

---

