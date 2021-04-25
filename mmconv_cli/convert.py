# pylint: disable-msg=C0103
import pandas as pd

from mmconv_cli.loader import custom_file_loaders, default_loader
from mmconv_cli.formatters import formatters


def convert(opts: dict) -> str:
    """Convert file to Money Manager style

    Args:
        OPTS (dict): Conversion options

    Returns:
        str: Returns file path to new file
    """
    # Load into Pandas
    df = load_file(opts)

    # Load bank formatter
    # df_new = load_formatter(df, opts['bank'])

    return opts['output_path']


def load_file(opts: dict) -> pd.DataFrame:
    """Load file into Pandas."""
    file_path = opts['file_path']
    file_type = opts.get('file_type', 'xlsx')
    bank = opts.get('bank', None)

    loader = custom_file_loaders.get(bank, default_loader)

    return loader(file_path, file_type)


def load_formatter(df: pd.DataFrame, bank: str):
    """Format file into Pandas."""
    return formatters[bank](df)
