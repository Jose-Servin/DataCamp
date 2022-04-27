import pandas as pd

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
def grab_next_value(df):
    """
    Here we will introduce a bug that grabs the wrong value from DF to learn more about Mocking.
    We will grab the first row, second column value since this can be a common mistake encountered.
    """
    value = df.iloc[0, 1]
    return value
