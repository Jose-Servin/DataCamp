from scipy.stats import linregress


# build training set


def train_model(training_set):
    """"
    function that returns slope and intercept of a provided training set

    """
    slope, intercept, _, _, _ = linregress(training_set[:, 0], training_set[:, 1])
    return slope, intercept
