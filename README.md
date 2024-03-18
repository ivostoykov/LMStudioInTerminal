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
3.1 If you prefer, you can edit the ~/.bashrc directly: Open the file
```
nano ~/.bashrc
```
Add the following line somewhere:
```
ai() { python3 full/path/to/aiqry.py "$@"; }
```
Save the file.

## Configuration

The configuration file is expected to be `config.json`.

**Using the Default Configuration:**

If you're using the default LM Studio configuration, you don't need to modify the `url` value.

**Custom Configuration:**

* **`url`:** Change this value according to your specific settings if you're not using the default LM Studio configuration.
* **`headers`:** This is the server response format (default JSON) and should not be modified for now.
* **`messages`:** This mandatory key and its subkeys (`role`, `content`) names should not be changed. You can adjust the `role` value.
* **`max_tokens`:** This key defines the maximum number of tokens allowed in a response. The default value is 1024. You can modify this value if needed.
* **`stream`:** As LM Studio streams the generated AI response by default, this key and its value (`true`) should not be changed.


## Use
1. Ensure LM Studio server is started.
2. In a terminal (Ctrl+Alt+T) type your question prefixed with `ai `:
```
ai Tell me who you are.
```
![Screencast](https://github.com/ivostoykov/LMStudioInTerminal/assets/889184/b7710e7e-575d-461b-9a43-2df50d3578bf)


## Other
This software is provided as-is. Please ensure it is not harmful to your system. Check it carefully before use. Always use third-party software with caution.

