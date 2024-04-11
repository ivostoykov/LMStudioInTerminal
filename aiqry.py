import requests
import json
import sys
import os
import platform
import datetime

messages = [{"role": "system", "content": f"Local date and time is {datetime.datetime.now()}.Unless prompted otherwise, when needed and related, assume this OS: {platform.uname()}"}]
streamContent = ''

def process_line(line):
    global streamContent
    global messages
    # if line:
        # decoded_line = line.decode('utf-8').strip()

        # Ensure the line starts with 'data:' and extract everything after it
    if not line.startswith('data:'):
        return
    
    json_data = line.split("ata: ", 1)[-1]
    if json_data.lower() == "[done]":
        messages.append({"role": "assistant", "content": streamContent})
        sys.stdout.writelines("\n")
        sys.stdout.flush()
        return;

    try:
        stream_data = json.loads(json_data)
    except json.JSONDecodeError as e:
        messages.append({"role": "assistant", "content": streamContent})
        print(f"\nError decoding JSON: {e};\nData: {json_data}")
        return

    # Extract 'content' if available and concatenate
    choices = stream_data.get("choices")
    if choices is None or len(choices) < 1:
        return

    finish_reason = choices[0].get('finish_reason')
    if finish_reason == "stop":
        return
    
    delta = choices[0].get("delta")
    if delta is None:
        return

    choice_content = delta.get("content", "")
    if choice_content is None:
        return

    streamContent += choice_content
    sys.stdout.write(choice_content)
    sys.stdout.flush()

def load_config():
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(dir_path, 'config.json')
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    except Exception as e:
        print(f"Error loading config: {e}")
        return None

def send_request_and_process_response(q):

    if config is None:
        return

    try:
        response = requests.post(config['url'], headers=config['headers'], data=json.dumps(config['data']), stream=True)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return


    for line in response.iter_lines():
        if not line or line is None:
            continue

        process_line(line.decode('utf-8').strip())

def append_message_and_send(config, message):
    messages.append({"role": "user", "content": message})
    config['data']['messages'] = messages
    sys.stdout.write("\nAssistant:\n\t")
    sys.stdout.flush()
    send_request_and_process_response(config)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <model_name>")
        sys.exit(1)

    config = load_config()
    append_message_and_send(config, ' '.join(sys.argv[1:]))
    
    try:
        while True:
            user_input = input("\n\nUser (Ctrl+C to exit): ")
            append_message_and_send(config, user_input)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)


