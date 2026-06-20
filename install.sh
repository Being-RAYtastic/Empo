#!/usr/bin/env bash

# Code to get the dir path properly
projectDir=$PWD

# installs dependencies
echo -e "\033[0;32mInstalling Dependencies...\033[0m"

python3 -m venv venv
venv/bin/pip install -r requirements.txt

# alias command to register in $SHELLrc file
empo_cmd="alias empo='$projectDir/venv/bin/python $projectDir/main.py'"

# Getting the $SHELLrc file (.bashrc or .zshrc or etc.) - Default Shell
shell_name=$(basename $SHELL)
shell_rc_file="$HOME/.${shell_name}rc"


# remove old alias if exists, then add new one
sed -i '/alias empo=/d' "$shell_rc_file"
# Registers the alias
echo $empo_cmd >> $shell_rc_file

echo -e "\033[0;32mSuccessfully installed empo!\033[0m"
exec $SHELL
exit 0