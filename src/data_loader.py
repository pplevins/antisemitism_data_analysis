import pandas as pd


class DataLoader:

    @staticmethod
    def load_from_csv(path):
        return pd.read_csv(path)
