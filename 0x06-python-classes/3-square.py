#!/usr/bin/python3
# 3-square.py

"""Define a class Square."""


class Square:
    """Represent a square."""

    def.ini.(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """Return the current area of the square."""
        return (self.size * self.size)