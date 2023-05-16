import os
import openai
import json
from dotenv import load_dotenv
from datetime import datetime

# Set up OpenAI client with API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define variables
codebase = "/path/to/your/codebase"  # replace with your codebase path
special_file = "/path/to/your/special/file"  # replace with your special file path
main_prompt = "Your main prompt here"  # replace with your main prompt
usage_prompt = "Your usage prompt here"  # replace with your usage prompt
summarization_prompt = "Your summarization prompt here"  # replace with your summarization prompt

# Define a class to handle the GPT API calls
class GPTCommunication:

    def __init__(self, version):
        self.version = version

    def prompt(self, text):
        if self.version == 3.5:
            # Call GPT-3.5 here
            response = openai.Completion.create(
              engine="text-davinci-03",
              prompt=text,
              max_tokens=4000
            )
        elif self.version == 4:
            # Call GPT-4 here
            response = openai.Completion.create(
              engine="text-davinci-04",
              prompt=text,
              max_tokens=8000
            )
        else:
            print(f"Unsupported GPT version: {self.version}")
            return None

        return response

# Create an instance of GPTCommunication for GPT-4
gpt_4 = GPTCommunication(4)

# Summarize the special file
with open(special_file, "r") as f:
    special_file_contents = f.read()
special_file_summary = gpt_4.prompt(summarization_prompt + special_file_contents).choices[0].text.strip()

# Iterate over each file in the codebase
for root, dirs, files in os.walk(codebase):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, "r") as f:
            file_contents = f.read()

        # Generate suggestions for implementing the special file
        usage_input = usage_prompt + special_file_summary + file_contents
        suggestions = gpt_4.prompt(usage_input).choices[0].text.strip()

        # Apply the main prompt to generate updates
        main_input = main_prompt + special_file_summary + suggestions + file_contents
        updates = gpt_4.prompt(main_input).choices[0].text.strip()

        # Write the updates back to the file
        with open(file_path, "w") as f:
            f.write(updates)

        # Stage the file
        repo.git.add(file_path)

        # Commit the changes
        commit_message = f"Applied AI suggestions to {file}"
        repo.git.commit('-m', commit_message)
