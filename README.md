# LMStudioInTerminal

This is a small project I created for fun and to facilitate the use of local AI everywhere I need it.

## Prerequisites

This project requires LM Studio. Please follow the instructions on how to install and download GGUF of your choice at [LM Studio](https://lmstudio.ai/). LM Studio provides a server that can be used to query the running AI instance.

Python is also required. Check it:
```
python3 --version
```
or
```
python --version
```

## Installation

1. Clone this repository:
```
git clone https://github.com/ivostoykov/LMStudioInTerminal.git
```
3. (Optional) Under Linux Bash, open a terminal, make `setup.sh` executable by running:
```
chmod +x setup.sh
```
Then execute it:
```
./setup.sh /path/to/location/of/aiqry.py
```
or if you run it from the directory the project was cloned just:
```
./setup.sh
```
This will add a function to your `.bashrc` used to query the AI.
If you want to use it immediately in the same terminal you should manually execute:
```
source ~/.bashrc
```

## Use
In a terminal (Ctrl+Alt+T) type your question prefixed with `ai `:
```
ai Tell me who you are.
```

## Other
This software is provided as-is. Please ensure it is not harmful to your system. Check it carefully before use. Always use third-party software with caution.

