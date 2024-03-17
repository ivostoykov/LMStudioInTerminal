import requests
import json
import sys

def process_line(line):
    global concatenated_content
    # if line:
        # decoded_line = line.decode('utf-8').strip()

        # Ensure the line starts with 'data:' and extract everything after it
    if not line.startswith('data:'):
        return
    
    json_data = line.split("ata: ", 1)[-1]
    if json_data.lower() == "[done]":
        sys.stdout.writelines("\n")
        sys.stdout.flush()
        return;

    try:
        stream_data = json.loads(json_data)
    except json.JSONDecodeError as e:
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

    # print(choice_content, end="")
    sys.stdout.write(choice_content)
    sys.stdout.flush()

def load_config():
    try:
        with open('config.json', 'r') as config_file:
            return json.load(config_file)
    except Exception as e:
        print(f"Error loading config: {e}")
        return None

def send_request_and_process_response(q):

    config = load_config()
    # Exit the function if the config could not be loaded
    if config is None:
        return

    # Insert the dynamic content into the messages
    config['data']['messages'][0]['content'] = q
    
    try:
        response = requests.post(config['url'], headers=config['headers'], data=json.dumps(config['data']), stream=True)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return


    for line in response.iter_lines():
        if not line or line is None:
            continue

        process_line(line.decode('utf-8').strip())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <model_name>")
        sys.exit(1)

    q = ' '.join(sys.argv[1:])
    send_request_and_process_response(q)
