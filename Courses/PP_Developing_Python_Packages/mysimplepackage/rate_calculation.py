import pandas as pd
import time

# build DataFrame
charges = {
    'Fee': [8, 4, 2, 7],
    'Courses': ["Spark", "PySpark", "Python", "pandas"],
    'Duration': ['30days', '40days', '35days', '50days'],
    'Discount': [1000, 2300, 1200, 2000]
}
index_labels = ['r1', 'r2', 'r3', 'r4']
data_df = pd.DataFrame(charges, index=index_labels)


# helper function
def grab_value(df):
    """ grab first column first row value from DF

    """
    value = df.iloc[0, 0]
    return value


# process function
def calculate_final_rate():
    """Classify value from helper function"""
    value = grab_value(data_df)
    if value < 10:
        return "Rate too low"
    else:
        return "Rate approved"


# new function to mock
def next_value(df):
    """
    here we are introducing a bug by grabbing the wrong value.
    """
    value = df.iloc[0, 1]
    return value


# process function
def calculate_next_final_rate():
    """Classify value from helper function"""
    value = next_value(data_df)
    if value < 10:
        return "Rate too low"
    else:
        return "Rate approved"
