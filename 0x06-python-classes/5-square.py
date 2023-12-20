#!/usr/bin/python3
"square module"


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        initialization function for our square clasee
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        getter for the size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for the size property
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square using '#' characters
        """
        for i in range(self.__size):
            print("#" * self.__size)

    def __validate_size(self, size):
        """
        validates the size, checking for errors
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
