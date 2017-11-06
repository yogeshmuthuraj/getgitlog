# getgitlog

Tool to output git commit messages in arrray format

## Installation
First, you'll want to get a python with pip. Every version newer than 3.4 ensures that pip is installed. If you don't have it, you can try running these commands:
```bash
brew install python
easy_install pip
```

Assuming you already have /usr/local/bin on your path (you should), you can do this to install the verificator:
```bash
pip install -r requirements.txt
ln -s "$(pwd)/getgitlog.py" /usr/local/bin/getgitlog
chmod +x /usr/local/bin/getgitlog
```

What these lines do is install the dependency libraries, copy the script from this folder to your user local binaries directory (typically installing things in /usr/local is safe), and set it as executable.

You can check if /usr/local/bin is on your path using `echo $PATH`

If it's not, you can add it using<br>
bash/zsh
`export PATH = $PATH:/usr/local/bin`

fish
`set PATH $PATH /usr/local/bin`


## Example usage

![gitgetlog](https://i.imgur.com/ImrcUOy.gif)
