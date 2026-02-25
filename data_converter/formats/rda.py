import pyreadr
import pandas as pd
from .base import BaseFormatHandler


class RDAHandler(BaseFormatHandler):

    def read(self, path: str) -> pd.DataFrame:
        result = pyreadr.read_r(path)
        return list(result.values())[0]

    def write(self, df: pd.DataFrame, path: str):
        raise NotImplementedError("Writing to RDA is not supported.")
