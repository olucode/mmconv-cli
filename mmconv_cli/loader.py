# pylint: disable-msg=C0103

"""
This contains the different custom file loaders

.. currentmodule:: mmconv_cli.loader
.. moduleauthor:: olucode <olucode6379@gmail.com>
"""

import pandas as pd

custom_file_loaders = {}


def default_loader(file_path: str, file_type: str):
    """Default file loader used across all banks"""

    if file_type == 'xlsx':
        df = pd.read_excel(file_path)

    return df


def get_read_func(file_type):
    """Returns the correct IO read function based on file type"""
    file_types = {
        'xlsx': pd.read_excel,
        'csv': pd.read_csv
    }

    return file_types[file_type]
