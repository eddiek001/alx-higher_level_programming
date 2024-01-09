#!/usr/bin/python3
"""function that reads a text file """


def read_file(filename=""):
    """reads a file
    """
    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end='')
