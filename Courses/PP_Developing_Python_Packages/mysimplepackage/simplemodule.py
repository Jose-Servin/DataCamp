"""
A module for counting certain words in a text file.
"""
import math
import pytest
import os
import numpy as np
import pandas as pd


def count_words(filepath, words_list):
    """
    Count the total number of times these words appear.

    The count is performed on a text file at a given location

    Parameters
    ----------
    filepath : str
        Path to text file
    words_list : list of str
        Count the total number of appearances of these words.

    Returns
    -------

    """
    # Open the text file
    with open(filepath) as file:
        text = file.read()
    # Count number of times these words appear
    n = 0
    for word in text.split():
        if word.lower() in words_list:
            n += 1
    return n


def add_floats(float_1, float_2):
    return float_1 + float_2


def simple_sqrt(num):
    answer = math.sqrt(num)
    return answer
