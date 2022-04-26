import pytest
import os
import pandas as pd
import csv


def remove_last_row(df):
    new_df = df.drop(df.tail(1).index)
    return new_df


def preprocess(raw_data_file_path, clean_data_file_path):
    """remove the last row of a csv file"""

    raw_data = pd.read_csv(raw_data_file_path, index_col=None)

    clean_data = remove_last_row(raw_data)

    clean_data.to_csv(clean_data_file_path, index=False)



