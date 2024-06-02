import sys

class Book:
    def __init__(self, title, page_count) -> None:
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        """The title property getter"""
        return self._title

    @title.setter
    def title(self, title):
        """The title property setter"""
        self._title = title 

    @property
    def page_count(self):
        """The page_count property getter"""
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """The page_count property setter"""
        if not isinstance(page_count, int):
            print("page_count must be an integer", file=sys.stderr)
        else:
            self._page_count = page_count
