import math
import pytest
from mysimplepackage.simplemodule import count_words, add_floats, simple_sqrt


class TestCountWords(object):
    def test_correct_file(self):
        self.actual = count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words'])
        self.expected = 6
        self.message = f"""
                count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words']) returned {self.actual} instead of 
                {self.expected}.
            """
        assert self.actual is self.expected, self.message

    # Add test that returns exception when word counts do not match
