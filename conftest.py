import pytest
from unittest import mock


# Mock for external API calls like OpenAI
@pytest.fixture
def mock_openai_api():
    with responses.RequestsMock() as rsps:
        rsps.add(responses.POST, 'https://api.openai.com/v1/engines', json={"data": "mock_response"}, status=200)
        yield rsps


# Mock for file operations
@pytest.fixture
def mock_file_io():
    with mock.patch("builtins.open", mock.mock_open(read_data="mock data")) as mock_file:
        yield mock_file


# Mock for environment variables
@pytest.fixture
def mock_env_vars():
    with mock.patch.dict('os.environ', {'ENV_VAR': 'mock_value'}):
        yield


# Mock for time-dependent code
@pytest.fixture
def freeze_time_fixture():
    with freeze_time("2023-01-01"):
        yield

# Add more fixtures as needed
