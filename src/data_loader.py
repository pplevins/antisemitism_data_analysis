import pandas as pd


class DataLoader:
    """A class to load data from csv files"""

    @staticmethod
    def load_from_csv(path) -> pd.DataFrame:
        """Load data from csv file to a pandas dataframe"""
        return pd.read_csv(path)
