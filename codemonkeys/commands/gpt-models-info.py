from codemonkeys.base_entities.command_class import Command
from codemonkeys.defs import nl
from codemonkeys.utils.gpt.model_info import update_gpt_model_cache, get_gpt_model_info
from codemonkeys.utils.monk.theme_functions import print_t


class GptModelsInfo(Command):
    
    named_arg_keys = ['update']
    update: bool = False

    def run(self):

        if self.update:
            print_t(f'Updating GPT Model Info Cache{nl}', 'loading')
            update_gpt_model_cache()

        model_info = get_gpt_model_info()
        if model_info is None:
            print_t('Model info is not cached. Please run `monk gpt-models-info --update`.', 'info')

        else:
            print_t(f'Available Models{nl}', 'special')
            for model_name, model_data in model_info.items():
                print_t(f"{model_name}", 'option')
