#!/bin/bash

# Function to append /aiqry.py if not present in the path
append_script_name_if_needed() {
  local input_path="$1"
  # Check if the input path ends with /aiqry.py. If not, append it.
  if [[ "$input_path" =~ /aiqry\.py$ ]]; then
    echo "$input_path"
  else
    # If the path ends with a slash or is empty, append directly; otherwise, add a slash before appending
    if [[ "$input_path" == */ || -z "$input_path" ]]; then
      echo "${input_path}aiqry.py"
    else
      echo "${input_path}/aiqry.py"
    fi
  fi
}

# Process the input parameter. If no parameter is provided, use the current directory's full path
if [ -z "$1" ]; then
  script_path="$(pwd)/aiqry.py"
else
  script_path=$(append_script_name_if_needed "$1")
fi

# Check if the script exists at the given path
if [ -f "$script_path" ]; then
    # If the file exists, proceed to add the function to .bashrc
    echo "ai() { python3 \"$script_path\" \"\$@\"; }" >> ~/.bashrc
    echo "Function 'ai' added to .bashrc successfully."
    echo "Please run 'source ~/.bashrc' to use the function immediately."
else
    # If the file does not exist, print an error message
    echo "Error: 'aiqry.py' not found at the specified location: $script_path"
fi
