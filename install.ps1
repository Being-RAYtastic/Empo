echo "Installing Dependencies..."
pip install install beautifulsoup4 requests argparse duckduckgo-search

"Set-Alias -Name empo -Value python $PWD\main.py" >> $profile

echo "Successfully Installed empo!"
exit
