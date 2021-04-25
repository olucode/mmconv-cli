import logging
import pandas as pd

from mmconv_cli.utils import filter_expense, filter_income

column_mapper = {
    'Date': 'Date',
    'Description': 'Contents',
    'Paid Out': 'expense',
    'Paid In': 'income',
    'Balance': 'balance',
}


def format_stmt(df: pd.DataFrame) -> pd.DataFrame:
    """Format Kuda account statement"""
    df_new: pd.DataFrame = df.rename(columns=column_mapper, errors='raise')

    # Figure out amount column
    frames = [filter_income(df_new), filter_expense(df_new)]
    df_new = pd.concat(frames)
    df_new.drop(['balance', 'expense', 'income'],
                inplace=True, axis='columns')

    return df_new
