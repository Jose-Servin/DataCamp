import math

import pytest

from mysimplepackage.simplemodule import count_words, add_floats, simple_sqrt


def test_count_words():
    actual = count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words'])
    expected = 6
    message = f"""
        count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words']) returned {actual} instead of 
        {expected}.
    """
    assert actual is expected, message


def test_add_floats():
    actual = add_floats(0.1, 0.2)
    expected = pytest.approx(0.3)
    message = f"""
        add_floats(0.1, 0.2) returns {actual} instead of {expected} 
    """

    assert actual == expected, message
    # here we will add a test for the return value type
    assert isinstance(actual, float)
    # here we will add a test for the expected value
    assert expected == 0.3


def test_valueerror_simple_sqrt():
    example_argument = -10
    with pytest.raises(ValueError) as exception_info:
        simple_sqrt(example_argument)
    # Check if ValueError contains the correct message
    assert exception_info.match("math domain error")


