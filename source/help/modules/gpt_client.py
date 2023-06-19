from source.utils.monk.theme.theme_functions import print_t


def main():
    print_t("GPT Client Help", "important")
    print_t("The gpt_client module offers a GPTClient class and several helper functions to "
            "interact with OpenAI's GPT-3 and other versions of the transformers. "
            "This includes generating text from prompts, encoding and decoding text tokens, "
            "token counting, and handling tokens for large text chunks.", "info")

    print_t("Usage Example", "input")
    print_t("1. Import the GPTClient class from the module.", "info")
    print_t("   from gpt_client import GPTClient", "file")
    
    print_t("2. Set model_name to '3' for GPT-3.5-Turbo or '4' for GPT-4.", "info")
    print_t("   model_name = '3'", "file")
    
    print_t("3. Optionally, set additional parameters such as temperature and max_tokens.", "info")
    print_t("   temperature = 0.8", "file")
    print_t("   max_tokens = 100", "file")
    
    print_t("4. Create an instance of the GPTClient class.", "info")
    print_t("   gpt_client = GPTClient(model_name, temperature, max_tokens)", "file")

    print_t("5. Generate text with given prompt.", "info")
    print_t("   prompt = 'Once upon a time...'", "file")
    print_t("   response = gpt_client.generate(prompt)", "file")
    print_t("   print(response)", "file")

    print_t("You can also utilize other functions like tokenize, detokenize, count_tokens, "
            "shorten_to_n_tokens, and split_into_chunks for a variety of text processing tasks.", "tip")

if __name__ == "__main__":
    main()