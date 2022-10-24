import pandas as pd


class DataFile:
    def get_data_from_file(self) -> pd.DataFrame:
        data = pd.read_csv("data.txt", sep=",")
        return data
