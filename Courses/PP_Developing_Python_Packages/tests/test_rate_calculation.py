import pandas as pd
import pytest
from mysimplepackage.rate_calculation import grab_value, calculate_final_rate, slow_function


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


class TestSlowFunction(object):
    def test_slow_function_mock(self, mocker):
        mocker.patch(
            "mysimplepackage.rate_calculation.api_call",
            return_value=5
        )
        expected = 5
        actual = slow_function()
        assert actual == expected
