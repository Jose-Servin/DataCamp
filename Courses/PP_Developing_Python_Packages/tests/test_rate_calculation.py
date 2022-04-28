import pandas as pd
import pytest
from mysimplepackage.rate_calculation import grab_value, calculate_final_rate, calculate_next_final_rate
from unittest.mock import call


def next_value_bug_free(df):
    """

    this bug free function will return the value 4 from the dataframe built by the pytest fixture
    """
    value = df.iloc[1, 0]
    return value


class TestFinalRateCalc(object):

    # build pytest fixture function
    @pytest.fixture
    def build_df(self):
        # build DataFrame
        charges = {
            'Fee': [8, 4, 2, 7],
            'Courses': ["Spark", "PySpark", "Python", "pandas"],
            'Duration': ['30days', '40days', '35days', '50days'],
            'Discount': [1000, 2300, 1200, 2000]
        }
        index_labels = ['r1', 'r2', 'r3', 'r4']
        data_df = pd.DataFrame(charges, index=index_labels)

        return data_df

    def test_calculate_final_rate(self, build_df):
        data_df = build_df

        actual = calculate_final_rate()

        expected = "Rate too low"

        message = f"The expected value was {expected} and the actual value is {actual}"

        assert actual == expected, message


class TestNextFinalRate(object):
    # build pytest fixture function
    @pytest.fixture
    def build_df(self):
        # build DataFrame
        charges = {
            'Fee': [8, 4, 2, 7],
            'Courses': ["Spark", "PySpark", "Python", "pandas"],
            'Duration': ['30days', '40days', '35days', '50days'],
            'Discount': [1000, 2300, 1200, 2000]
        }
        index_labels = ['r1', 'r2', 'r3', 'r4']
        data_df = pd.DataFrame(charges, index=index_labels)

        return data_df

    def test_next_value_mocking(self, build_df, mocker):
        data_df = build_df
        next_value_mock = mocker.patch(
            "mysimplepackage.rate_calculation.next_value",
            side_effect=next_value_bug_free)

        actual = calculate_next_final_rate()
        expected = "Rate too low"

        assert actual == expected
