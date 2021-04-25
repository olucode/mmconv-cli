import pandas as pd


def filter_expense(df: pd.DataFrame):
    """Remove income values"""
    df_new = df.dropna(subset=['income']).copy()

    df_new['Income/Expense'] = 'Income'
    df_new['Amount'] = df_new['expense']

    return df_new


def filter_income(df: pd.DataFrame):
    """Remove expense values"""
    df_new = df.dropna(subset=['expense']).copy()

    df_new['Income/Expense'] = 'Expense'
    df_new['Amount'] = df_new['income']

    return df_new
