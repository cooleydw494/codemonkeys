import os
import sys

import openai

from pack.modules.core.config_mgmt.env.env_class import ENV
from pack.modules.core.theme.theme_functions import print_t

# Set up OpenAI client with API key
ENV = ENV()
openai.api_key = ENV.OPENAI_API_KEY

# Singleton instance variable for GPT models
GPT_MODELS = None


def check_api_key():
    if not openai.api_key:
        raise Exception("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")


class GPTClient:
    def __init__(self, version, max_tokens=int(os.getenv("MAX_TOKENS", 4000)), temperature=1.0):
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

        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=self.max_tokens,
            temperature=temperature
        )

        # TODO: implement control of the number of options and selection
        return response.choices[0].message.content.strip()


def instantiate_gpt_models():
    global GPT_MODELS

    # Instantiate GPT models only if not done already
    if GPT_MODELS is None:
        print_t("Instantiating GPT models...", "info")
        model_versions = {3, 4}
        GPT_MODELS = {version: GPTClient(version) for version in model_versions}
        print_t("GPT models instantiated successfully.", "success")

    return GPT_MODELS


def gpt_client(model_name):
    # Get the GPT models
    gpt_models = instantiate_gpt_models()
    """Get the GPT client based on the model name"""
    client = gpt_models.get(model_name)
    if not client:
        print_t(f"Model '{model_name}' not found.", "error")
        sys.exit(1)
    return client
