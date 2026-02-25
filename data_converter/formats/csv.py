import pandas as pd
from .base import BaseFormatHandler


class CSVHandler(BaseFormatHandler):

    def read(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)

    def write(self, df: pd.DataFrame, path: str):
        df.to_csv(path, index=False)
