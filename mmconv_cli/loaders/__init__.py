# pylint: disable-msg=C0103

"""
This contains the different custom file loaders

.. currentmodule:: mmconv_cli.loader
.. moduleauthor:: olucode <olucode6379@gmail.com>
"""

import pandas as pd

from . import kuda_loader


custom_file_loaders = {
    'Kuda': kuda_loader.load_file,
}


def default_loader(file_path: str, file_type: str) -> pd.DataFrame:
    """Default file loader used across all banks"""

    if file_type == 'xlsx':
        df = pd.read_excel(file_path)

    return df
