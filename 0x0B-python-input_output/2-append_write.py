#!/usr/bin/python3
""" function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends onto a utf-8 encoded text file
    """
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
