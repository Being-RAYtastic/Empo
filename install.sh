#/bin/sh

# Code to get the dir path properly
projectDir=$PWD

# installs dependencies
pip install beautifulsoup4 requests argparse --break-system-packages

# alias command to register in $SHELLrc file
empo_cmd="alias empo='python3 $projectDir/main.py'"

# Getting the $SHELLrc file (.bashrc or .zshrc or etc.) - Default Shell
nonModified_default_shell_rc_file="$HOME/."
nonModified_default_shell_rc_file+=$SHELL 
nonModified_default_shell_rc_file+="rc"

replace_str="/bin/"
shell_rc_file=${nonModified_default_shell_rc_file/$replace_str/""}


# Registers the alias
echo $empo_cmd >> $shell_rc_file

echo "Successfully installed empo!"
exec $SHELL
