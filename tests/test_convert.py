
import tempfile
import pytest
import pandas as pd

from mmconv_cli.convert import convert, load_file


# TODO: Use pytest-datafiles to load this file locally
@pytest.fixture
def xlsx_file():
    """Excel file fixture"""
    return 'https://download.microsoft.com/download/1/4/E/14EDED28-6C58-4055-A65C-23B4DA81C4DE/Financial%20Sample.xlsx'


@pytest.fixture
def app_opts(xlsx_file):
    """Fixture options for file conversion"""
    return {
        'file_path': xlsx_file,
        'file_type': 'xlsx',
        'output_path': tempfile.NamedTemporaryFile().name,
        'bank': 'KUDA',
    }


def test_convert_returns_a_valid_output_file(app_opts):
    """
    Arrange: Acquire the conversion options.
    Act: The supplied file path should return a valid output file path
    Assert: The output file is valid
    """
    result = convert(app_opts)

    assert (
        result == app_opts['output_path']
    ), 'Output file path is invalid'


def test_load_file_returns_a_dataframe(xlsx_file, app_opts):
    """
    Act: The supplied file path should return a valid output file path
    Assert: The output file is valid
    """
    result = load_file({
        **app_opts,
        'file_path': xlsx_file,
    })

    assert (
        isinstance(result, pd.DataFrame)
    ), 'Input file is invalid and does not provide a dataframe'
