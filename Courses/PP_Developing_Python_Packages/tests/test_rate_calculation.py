import pandas as pd
import pytest
from mysimplepackage.rate_calculation import grab_value, calculate_final_rate, grab_next_value


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

    def test_grab_next_value_mock(self, build_df, mocker):
        data_df = build_df

        mocker.patch("mysimplepackage.rate_calculation.grab_next_value", return_value=4)

        actual = calculate_final_rate()

        expected = "Rate too low"

        message = f"The expected value was {expected} and the actual value is {actual}"

        assert actual == expected, message
