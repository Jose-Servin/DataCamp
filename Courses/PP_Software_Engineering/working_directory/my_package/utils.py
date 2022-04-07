import numpy as np


def secret_message(clearance=False):
    if clearance:
        print("The secret message is...")
    else:
        print("You cannot access the secret message")
