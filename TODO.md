## TODO List
### Resources
[OpenAI Token Optimization Docs](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) | [OpenAI tiktoken Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb) | [placeholder](placeholder) | [placeholder](placeholder) | [placeholder](placeholder)
### Prompt Optimization
- Implement prompt/token optimization strategies (incl logit_bias).
- Implement add/customize for prompt/token optimization strategies.
- Automate (without AI) prompt/token optimizations (incl logit_bias)
- Consider using GPT to optimize prompts/tokens.
### The `monk` command
- Add a monk sub-command that allows the user to create or open a new version of an existing X after backing up old
- Add a monk sub-command that allows the user to create a new X from a template
### Project Organization
- Configs become subdirs of monkeys dir, and the monkey-manifest should be a file in the root directory
    These directories will store existing configs, enabling the new/backup functionality above for monkey configs.
    I had an idea related to internal/customizable but idk. Keep thinking, this is fertile ground.
### Automations
- Create first non-generic automation. It should write a usage guide for each script in the scripts directory to help/internal/script-usage-guides/[script-name].txt
  Crazy idea version: make them python scripts that interactively help a user understand whatever they need to about the command instead of giving all the info (unless requested)
- Create the same thing above for any other entities that should have documentation. Then make a monk command that will open the documentation for a given entity `monk explain [entity-type]/[entity-name]`
  - Add a storage/internal/logs/aborts directory to store logs regarding files that exceed some kind of bounds checked within an automation. 
    - Ex: An automation has checks on token length and aborts if it exceeds some length. Store the log in this directory with info on the file, the reason for aborting, and the full prompt that was too long.
- Implement, and make re-usable, some automations logic to:
    - use GPT review of a file being read to determine other files that need to be read for more context. If this can be added to the prompt without exceeding token limit, do so, otherwise either abort and log to storage/internal/logs/aborts or just don't add it.
### Integrations
- Add more specific model options for the openai api (perhaps adding some fine-tuning options) for usage in specialized contexts in which they are adequate and cheaper.
- Add whatever the best locally run AI that is easy-ish to package with the framework (probably something that isn't very good but its useful and a starting place for people with crazy GPUs and/or patience)
- Add a way to get the contents of google searches and webpages. This is inspired by AutoGPT but also will be used in a way that is more directly useful and less open-ended.

### Super Advanced
- Use "Embeddings" (numerical representations of text that can be used to measure how related the text is to another "embedded" text). This could be useful in automations that have steps that require only a similarity check between texts

### README
- Add section on token counting and mention that the one-shot prompt approach makes it more precise because the message-based formatting of Chat-based API calls to gpt 3/4 API makes it harder to accurately count tokens (CodeMonkeys' default automation uses the Chat Completions API which despite having the word "chat" in it is for making traditional completions tasks)
- Discuss how the project-wide env vars lend themselves to having a different CodeMonkeys per repo.

### TROUBLESHOOTING
- The root directory name of the project must be only letters and hyphens. The pseudo-package (default code_monkeys) must be the same as the root directory with underscores instead of hyphens. To verify that imports are changed properly as well, you should just run `monk fix-namespace`, which will ask for the desired directory name and make sure all of this is correct.