from codemonkeys.defs import nl
from codemonkeys.entities.command import Command
from codemonkeys.utils.gpt.model_info import update_gpt_model_cache, get_gpt_model_info
from codemonkeys.utils.monk.theme_functions import print_t


class GptModelsInfo(Command):
    """
    Retrieve and display information about various GPT models.

    This Command can be used to fetch the latest details about different GPT models
    available through the framework, such as model name and whether function calling
    is supported. If the update flag is set, the GPT Model Info Cache will be refreshed.

    :param update: Flag indicating if the GPT Model Info Cache needs to be updated.
    :type update: bool
    """
    named_arg_keys = ['update']
    update: bool = False

    def run(self) -> None:
        """
        Updates the GPT Model Info Cache if required and prints the
        information about available GPT Models.

        It checks if an update is requested via the command argument; if so, it 
        updates the GPT Model Info Cache. Afterwards, it retrieves and displays 
        a list of GPT Models along with their details.

        :raises Exception: Raises an exception if the information cannot be retrieved.
        """
        if self.update:
            print_t(f'Updating GPT Model Info Cache{nl}', 'loading')
            update_gpt_model_cache()

        model_info = get_gpt_model_info()
        if model_info is None:
            print_t('Model info is not cached. Please run `monk gpt-models-info --update`.', 'info')

        else:
            print()
            print_t(f'Available Models:', 'special')
            print_t('(most do not support function calling)', 'quiet')
            print()
            for model_name in model_info:
                print_t(f"{model_name}")
