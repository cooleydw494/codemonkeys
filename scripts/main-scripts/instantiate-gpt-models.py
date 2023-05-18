def instantiate_gpt_models(main_model, summary_model, usage_model):
    gpt_models = {}
    for model in {main_model, summary_model, usage_model}:
        if model == '3' and '3' not in gpt_models:
            gpt_models['3'] = create_gpt_client(3.5)
        elif model == '4' and '4' not in gpt_models:
            gpt_models['4'] = create_gpt_client(4)
    return gpt_models
