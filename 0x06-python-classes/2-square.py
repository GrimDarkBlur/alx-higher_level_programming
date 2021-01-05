#!/usr/bin/python3
# 2-square.py

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, __size=0):
        """Initialize a new Square.

        Args:
            __size (int): The __size of the new square.
        """
        if not isinstance(__size, int):
            raise TypeError("__size must be an integer")
        elif __size < 0:
            raise ValueError("__size must be >= 0")
        self.__size = __size
