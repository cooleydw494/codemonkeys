def summarize_special_file(special_file, summary_model, summary_prompt, gpt_client):
    with open(special_file, "r") as f:
        special_file_contents = f.read()
    special_file_summary = gpt_client(summary_model).prompt(summary_prompt + special_file_contents).choices[
        0].text.strip()
    return special_file_summary
