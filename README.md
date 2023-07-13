# Empo
Command Line Web-Scraper Assistant

# Normal Installation (Script)
Clone this Github Repo `git clone https://github.com/Being-RAYtastic/Empo.git`
Paste the following code
```
cd Empo  
chmod +x install.sh
chmod +x main.py  
./install.sh
```
After this you'll be able to use Empo
# Temporary Installation (Dev)
- Install the following dependencies (Python Modules using pip)
    ```
    pip install beautifulsoup4 requests argparse
    ```

- Open your terminal in the directory where the project's `main.py` is present
- In terminal paste the following `alias empo='python3 main.py'`

- Now write your queries like this `empo "who is linus tolvards"` or maybe you can ask `empo "weather of delhi"`

# Use
- Try
    ```
    empo "weather of tokyo"

- `-s` or `--short` flag for short answers:
    ```
    empo "elon musk's birthday" -s
    ```
