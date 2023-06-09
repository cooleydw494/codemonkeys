from pack.modules.internal.config_mgmt.monkey_config.monkey_config_class import MonkeyConfig


def process_file(file_path, m: MonkeyConfig = None):
    with open(file_path, "r") as f:
        file_contents = f.read()

    # Apply the main prompt to generate updates
    main_input = main_prompt + special_file_summary + file_contents
    updates = gpt_client(main_prompt_model).prompt(main_input).choices[0].text.strip()

    # Write the updates back to the file
    with open(file_path, "w") as f:
        f.write(updates)
