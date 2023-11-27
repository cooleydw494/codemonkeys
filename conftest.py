import argparse
from unittest import mock

import pytest

from codemonkeys.utils.git import gitter
from codemonkeys.utils.gpt import gpt_client, model_info
from codemonkeys.utils.misc import defs_utils
from codemonkeys.utils.monk import theme_functions


# Mock for GPT Client
@pytest.fixture
def mock_gpt_client(response=None, token_count=10):
    with mock.patch.object(gpt_client, 'generate',
                           return_value=response if response is not None else "Mocked GPT response"):
        with mock.patch.object(gpt_client, 'count_tokens', return_value=token_count):
            yield


# Mock for File Operations
@pytest.fixture
def mock_file_ops(read_data="Mock file content", write_data=None):
    mock_read = mock.mock_open(read_data=read_data)
    with mock.patch('builtins.open', mock_read):
        mock_write = mock.patch('codemonkeys.utils.misc.file_ops.write_file_contents',
                                return_value=write_data) if write_data is not None else mock.DEFAULT
        with mock_write as mock_write_obj:
            yield mock_read, mock_write_obj


# Mock for Git Operations (Gitter)
@pytest.fixture
def mock_gitter():
    with mock.patch.object(gitter, 'clone', return_value=None) as mock_clone:
        with mock.patch.object(gitter, 'pull', return_value=None) as mock_pull:
            with mock.patch.object(gitter, 'push', return_value=None) as mock_push:
                with mock.patch.object(gitter, 'commit', return_value=None) as mock_commit:
                    yield mock_clone, mock_pull, mock_push, mock_commit


# Mock for Network Operations (Model Info)
@pytest.fixture
def mock_model_info(model_info_response={'model': 'mock_info'}):
    with mock.patch.object(model_info, 'get_gpt_model_info', return_value=model_info_response):
        with mock.patch.object(model_info, 'update_gpt_model_cache', return_value=None):
            yield


# Mock for User Interactions (Theme Functions)
@pytest.fixture
def mock_theme_functions(input_responses=None, print_outputs=None):
    input_side_effect = input_responses if input_responses is not None else ["Mock input"]
    print_side_effect = print_outputs if print_outputs is not None else [None]
    with mock.patch.object(theme_functions, 'input_t', side_effect=input_side_effect) as mock_input:
        with mock.patch.object(theme_functions, 'print_t', side_effect=print_side_effect) as mock_print:
            yield mock_input, mock_print


# Mock for Miscellaneous Operations (Defs Utils)
@pytest.fixture
def mock_defs_utils(project_root="/mock/project/root", load_class_response=None):
    with mock.patch.object(defs_utils, 'find_project_root', return_value=project_root):
        mock_load_class = mock.MagicMock() if load_class_response is None else load_class_response
        with mock.patch.object(defs_utils, 'load_class', return_value=mock_load_class):
            yield


# Mock for CLI User Inputs
@pytest.fixture
def mock_cli_user_input(input_sequence=None):
    input_side_effect = input_sequence if input_sequence is not None else ["mock_input1", "mock_input2"]
    with mock.patch('builtins.input', side_effect=input_side_effect):
        yield


# Mock for CLI Arguments
@pytest.fixture
def mock_cli_arguments(args=None):
    default_args = argparse.Namespace(arg1="value1", arg2="value2")
    parsed_args = args if args is not None else default_args
    with mock.patch('argparse.ArgumentParser.parse_args', return_value=parsed_args):
        yield


# Mock for Theme Configuration
@pytest.fixture
def mock_theme_config(config=None):
    mock_config = {'THEME_CONFIG': 'mock_theme'} if config is None else config
    with mock.patch.dict('os.environ', mock_config):
        yield
