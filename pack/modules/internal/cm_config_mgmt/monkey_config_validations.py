import os

from pack.modules.internal.theme.theme_functions import input_t, print_t


def is_valid_path():
    while True:
        path = input_t("Please enter the path: ", "(absolute path or you can use ~ on Mac/Linux)")
        absolute_path = os.path.expanduser(path)
        if os.path.exists(absolute_path):
            return absolute_path
        else:
            print_t("Invalid path. Please try again.", 'error')


def is_valid_model():
    while True:
        model = int(input_t("Please enter the model: ", "(choose 3 (gpt-3.5-turbo) or 4 (gpt-4))"))
        if model in [3, 4]:
            return model
        else:
            print_t("Invalid model. Please try again.", 'error')


def is_valid_temp():
    while True:
        temp = float(input_t("Please enter the temperature: ", "(a value between 0 and 1)"))
        if 0 <= temp <= 1:
            return temp
        else:
            print_t("Invalid temperature. Please try again.", 'error')
