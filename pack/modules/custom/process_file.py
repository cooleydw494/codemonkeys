def process_file(file_path, usage_prompt, special_file_summary, usage_prompt_model, main_prompt, main_prompt_model,
                 gpt_client):
    with open(file_path, "r") as f:
        file_contents = f.read()

    # Generate suggestions for implementing the special file
    usage_input = usage_prompt + special_file_summary + file_contents
    usage_suggestions = gpt_client(usage_prompt_model).prompt(usage_input).choices[0].text.strip()

    # Apply the main prompt to generate updates
    main_input = main_prompt + usage_suggestions + special_file_summary + file_contents
    updates = gpt_client(main_prompt_model).prompt(main_input).choices[0].text.strip()

    # Write the updates back to the file
    with open(file_path, "w") as f:
        f.write(updates)
