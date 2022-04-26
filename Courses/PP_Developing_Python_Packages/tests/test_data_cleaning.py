from mysimplepackage.data_cleaning import remove_last_row, preprocess
import pytest
import os
import pandas as pd
import csv


@pytest.fixture
def raw_and_clean_data_file():
    # Setup process
    raw_data_path = '/Users/joseservin/DataCamp/Courses/PP_Developing_Python_Packages/raw_data.csv'
    clean_data_path = '/Users/joseservin/DataCamp/Courses/PP_Developing_Python_Packages/clean_data.csv'

    fieldnames = ['A', 'B', 'C']

    rows = [
        {
            'A': 'Good',
            'B': 'Good',
            'C': 'Good'
        },
        {
            'A': 'Good',
            'B': 'Good',
            'C': 'Good'
        },
        {
            'A': 'Good',
            'B': 'Good',
            'C': 'Good'
        },
        {
            'A': 'Bad',
            'B': 'Bad',
            'C': 'Bad'
        },

    ]

    with open(raw_data_path, mode='w', newline='') as raw_csv_file:
        writer = csv.DictWriter(raw_csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # yield data
    yield raw_data_path, clean_data_path

    # Teardown
    os.remove(raw_data_path)
    os.remove(clean_data_path)


def test_on_data(raw_and_clean_data_file):
    raw_path, clean_path = raw_and_clean_data_file
    preprocess(raw_path, clean_path)

    with open(clean_path) as clean_csv_file:
        last_line = clean_csv_file.readlines()[-1].strip()

    actual = last_line
    expected = 'Good,Good,Good'
    message = f"The actual row data is {actual} and the expected is {expected}"

    assert actual == expected, message
