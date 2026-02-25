from abc import ABC, abstractmethod
import pandas as pd


class BaseFormatHandler(ABC):

    @abstractmethod
    def read(self, path: str) -> pd.DataFrame:
        pass

    @abstractmethod
    def write(self, df: pd.DataFrame, path: str):
        pass
