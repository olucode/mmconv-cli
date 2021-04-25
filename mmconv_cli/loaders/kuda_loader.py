import logging
import pandas as pd


KUDA_ROW_SKIP = 14


def load_file(file_path: str, file_type: str) -> pd.DataFrame:
    logging.info('Load Kuda Bank Statement')

    if file_type == 'xlsx':
        df = pd.read_excel(file_path, skiprows=KUDA_ROW_SKIP)

    return df
