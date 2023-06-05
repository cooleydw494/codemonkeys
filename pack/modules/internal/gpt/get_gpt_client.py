import os

import openai

from pack.modules.internal.cm_config_mgmt.env_class import ENV

# Set up OpenAI client with API key
ENV = ENV()
openai.api_key = ENV.OPENAI_API_KEY


def check_api_key():
    if not openai.api_key:
        raise Exception("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")


class GPTClient:
    def __init__(self, version, max_tokens=int(os.getenv("MAX_TOKENS", 4000)), temperature=0.5):
        self.engine_map = {
            '3': "gpt-3.5-turbo",
            '4': "gpt-4"
        }
        self.engine = self.engine_map.get(str(version))

        if not self.engine:
            raise ValueError(f"Unsupported GPT version: {version}")

        self.max_tokens = max_tokens
        self.temperature = temperature

    def generate(self, prompt, temperature=None):
        check_api_key()

        if temperature is None:
            temperature = self.temperature

        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=self.max_tokens,
            temperature=temperature
        )

        return response.choices[0].text.strip()


def instantiate_gpt_models():
    model_versions = {3, 4}
    gpt_models = {version: GPTClient(version) for version in model_versions}

    return gpt_models
