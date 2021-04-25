import pandas as pd

from dataclasses import dataclass

from mmconv_cli.loaders import custom_file_loaders, default_loader
from mmconv_cli.formatters import formatters


DEFAULT_MM_ACCOUNT = 'Kuda'
DEFAULT_MM_MAIN_CAT = 'Other'


@dataclass
class ConvertOpts:
    file_path: str
    output_path: str
    bank: str = None
    file_type: str = 'xlsx'
    output_type: str = 'unicode'


def convert(opts: ConvertOpts) -> str:
    """Convert file to Money Manager style"""
    # Load into Pandas
    df = load_file(opts)

    # Load bank formatter
    df_new = load_formatter(df, opts.bank)

    output_path = create_output_file(df_new, opts.output_path)

    return output_path


def load_file(opts: ConvertOpts) -> pd.DataFrame:
    """Load file into Pandas."""
    file_path = opts.file_path
    file_type = opts.file_type
    bank = opts.bank

    loader = custom_file_loaders.get(bank, default_loader)

    return loader(file_path, file_type)


def load_formatter(df: pd.DataFrame, bank: str) -> pd.DataFrame:
    """Format file accordingly."""
    df_new = formatters[bank](df)

    df_new['Account'] = DEFAULT_MM_ACCOUNT
    df_new['Main Cat.'] = DEFAULT_MM_MAIN_CAT
    df_new['Sub Cat.'] = ''
    df_new['Details'] = ''

    # Reorganize Columns
    columns = [
        'Date',
        'Account',
        'Main Cat.',
        'Sub Cat.',
        'Contents',
        'Amount',
        'Income/Expense',
        'Details',
    ]
    df_ = df_new[columns]

    print(df_)

    return df_


def create_output_file(df: pd.DataFrame, output_path: str):
    return output_path
