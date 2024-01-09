#!/usr/bin/python3
'''function that writes a string to a text file'''


def write_file(filename="", text=""):
    """writes to a utf-8 encoded text file
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(text)
