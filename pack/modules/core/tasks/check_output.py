from definitions import nl2, nl
from pack.modules.core.abilities.gpt_client import GPTClient
from pack.modules.core.config.monkey_config.monkey_config_class import MonkeyConfig
from pack.modules.core.theme.theme_functions import print_t


def check_output(updates: str, m: MonkeyConfig) -> bool:
    check_prompt = f"{m.OUTPUT_CHECK_PROMPT}{nl2}{updates}"
    print_t(f"Checking output with prompt:{nl}{m.OUTPUT_CHECK_PROMPT}", 'info')
    check_output_gpt_client = GPTClient(m.OUTPUT_CHECK_MODEL, m.OUTPUT_CHECK_TEMP, m.MAX_TOKENS)
    check_result = check_output_gpt_client.generate(check_prompt)

    if check_result.lower() == 'true':
        print_t(f"Output is valid: {check_result}", 'special')
        return True
    else:
        print("Output did not pass the check. Retrying...", 'warning')
        return False
