import sys

class Shoe:
    def __init__(self, brand, size) -> None:
        self.brand = brand
        self.size = size

    @property
    def brand(self):
        """The brand property getter"""
        return self._brand

    @brand.setter
    def brand(self, brand):
        """The brand property setter"""
        self._brand = brand 

    @property
    def size(self):
        """The size property getter"""
        return self._size

    @size.setter
    def size(self, size):
        """The size property setter"""
        if not isinstance(size, int):
            sys.stderr.write("size must be an integer\n")
        else:
            self._size = size

    def cobble(self):
        """Method to repair the shoe"""
        print("Your shoe is as good as new!")
        self.condition = "New"
