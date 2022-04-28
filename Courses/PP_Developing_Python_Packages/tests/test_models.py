import pytest
import numpy as np
from mysimplepackage.models import train_model


class TestModels(object):
    def test_train_model(self):
        test_argument = np.array(
            [
                [1.0, 3.0],
                [2.0, 5.0],
                [3.0, 7.0]
            ]
        )
        expected_slope = 2.0
        expected_intercept = 1.0

        slope, intercept = train_model(test_argument)
        assert slope == pytest.approx(expected_slope)
        assert intercept == pytest.approx(expected_intercept)

    def test_on_positive_correlated_data(self):
        test_argument = np.array(
            [
                [1.0, 4.0], [2.0, 4.0],
                [3.0, 9.0], [4.0, 10.0],
                [5.0, 7.0], [6.0, 13.0],
            ]
        )

        slope, intercept = train_model(test_argument)

        assert slope > 0
