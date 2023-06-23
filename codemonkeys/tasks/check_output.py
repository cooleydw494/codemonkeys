from defs import import_monkey_config_class
from defs import nl2, nl
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.abilities.gpt_client import GPTClient

MonkeyConfig = import_monkey_config_class()


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
