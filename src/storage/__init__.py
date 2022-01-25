# Storage
# Contributors: Jacob Nettleship
# Date edited: 25/01/22
"""
File containing functions for storing and retrieving data
"""


def write_file(file, string):
    with open(file, 'a') as f:
        f.write(f"{string}\n")
