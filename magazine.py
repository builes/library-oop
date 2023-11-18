from typing import List, Optional
from library_item import LibraryItem

class Magazine(LibraryItem):
    """
    Class representing a magazine in the library.
    """

    total_magazines = 0

    def __init__(self, title: str, publication_year: int, editor: str):
        """
        Initialize a Magazine.

        Parameters:
        - title (str): Title of the magazine.
        - publication_year (int): Year of publication.
        - editor (str): Editor of the magazine.
        """
        super().__init__(title, publication_year)
        self._editor = editor.lower()
        self._is_borrowed = False

        Magazine.total_magazines += 1

    def __str__(self) -> str:
        """
        Represent the magazine as a string.
        """
        return f"{self._title} by {self._editor} and was published in ({self._publication_year})"

    def __lt__(self, other: 'Magazine') -> bool:
        """
        Compare two magazines based on publication year.

        Parameters:
        - other (Magazine): Another magazine for comparison.

        Returns:
        - bool: True if the current magazine is published earlier than the other.
        """
        if isinstance(other, Magazine):
            return self._publication_year < other._publication_year


# m1 = Magazine("The Economist", 2018, "Zanny Minton Beddoes")
# m2 = Magazine("The New Yorker", 2015, "David Remnick")
# m3 = Magazine("The Atlantic", 2021, "Jeffrey Goldberg")
# m4 = Magazine("Le Monde diplomatique", 2014, "Serge Halimi")
# m5 = Magazine("The New York Review of Books", 2010, "Ian Buruma")

# magazines = [m1, m2, m3, m4, m5]
# magazines.sort()
# for magazine in magazines:
#     print(magazine)
