import os

from pack.modules.internal.config_mgmt.monkey_config.monkey_config_class import MonkeyConfig
from pack.modules.internal.gpt.gpt_client import GPTClient
from pack.modules.internal.gpt.token_counter import TokenCounter
from pack.modules.internal.theme.theme_functions import print_t

sep2 = os.linesep * 2


def check_output(updates: str, m: MonkeyConfig) -> bool:
    check_prompt = f"{m.OUTPUT_CHECK_PROMPT}{sep2}{updates}"
    print_t(f"Checking output with prompt:{os.linesep}{m.OUTPUT_CHECK_PROMPT}", 'info')
    check_prompt_tokens = TokenCounter('gpt-4').count_tokens(check_prompt)
    remaining_tokens = m.MAX_TOKENS - check_prompt_tokens - 5  # 5 is just meant to be a counting imprecision buffer
    check_output_gpt_client = GPTClient(m.OUTPUT_CHECK_MODEL, remaining_tokens, m.OUTPUT_CHECK_TEMP)
    check_result = check_output_gpt_client.generate(check_prompt)

    if check_result.lower() == 'true':
        print_t(f"Output is valid: {check_result}", 'special')
        return True
    else:
        print("Output did not pass the check. Retrying...", 'warning')
        return False
