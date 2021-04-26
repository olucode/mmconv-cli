
import tempfile
import pytest
import pandas as pd

from mmconv_cli.convert import convert, load_file, ConvertOpts


# TODO: Use pytest-datafiles to load this file
@pytest.fixture
def xlsx_file():
    """Excel file fixture"""
    return '/Users/olumide/Downloads/statement.xls'


@pytest.fixture
def app_opts(xlsx_file):
    """Fixture options for file conversion"""
    return ConvertOpts(
        file_path=xlsx_file,
        file_type='xlsx',
        output_path=tempfile.NamedTemporaryFile().name,
        bank='Kuda',
    )


def test_convert_returns_a_valid_output_file(app_opts: ConvertOpts):
    """
    Arrange: Acquire the conversion options.
    Act: The supplied file path should return a valid output file path
    Assert: The output file is valid
    """
    result = convert(app_opts)

    assert (
        result == app_opts.output_path
    ), 'Output file path is invalid'


def test_load_file_returns_a_dataframe(app_opts):
    """
    Act: The supplied file path should return a valid output file path
    Assert: The output file is valid
    """
    result = load_file(app_opts)

    assert (
        isinstance(result, pd.DataFrame)
    ), 'Input file is invalid and does not provide a dataframe'
