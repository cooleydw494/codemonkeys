import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI client with API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get the maximum tokens value from the environment variable
max_tokens = int(os.getenv("MAX_TOKENS", 4000))

# Create and return the GPT client
def create_gpt_client(version):
    engines = {
        3.5: "text-davinci-03",
        4: "text-davinci-04"
    }

    engine = engines.get(version)
    if engine:
        return openai.Completion.create(
            engine=engine,
            max_tokens=max_tokens
        )
    else:
        print(f"⚠️ Unsupported GPT version: {version}")
        return None

# Check if the API key is available
if not openai.api_key:
    print("⚠️ OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

