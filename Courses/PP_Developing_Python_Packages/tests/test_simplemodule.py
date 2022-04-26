import math
import pytest
from mysimplepackage.simplemodule import count_words, add_floats, simple_sqrt
import sys
import os


class TestCountWords(object):
    def test_correct_file(self):
        self.actual = count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words'])
        self.expected = 6
        self.message = f"""
                count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words']) returned {self.actual} instead of 
                {self.expected}.
            """
        assert self.actual is self.expected, self.message

    # Add test that returns exception when word counts do not match (checking test fails as expected)
    def test_wrong_file(self):
        self.actual = count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words'])
        self.expected = 5
        self.message = f"""
                        count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words']) returned {self.actual} instead of 
                        {self.expected}.
                    """

        with pytest.raises(AssertionError) as exception_info:
            assert self.actual is self.expected, self.message

    # Add test that is expected to fail
    @pytest.mark.xfail(reason="Testing an expected fail")
    def test_expected_failure(self):
        self.actual = None

        assert self.actual is not None

    # Hypothetically adding a function that only works with Python 2.7 or lower
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="requires Python 2.7")
    def test_conditional_skip(self):
        """Only runs on Python 2.7 or lower"""
        self.actual = True

        assert self.actual
