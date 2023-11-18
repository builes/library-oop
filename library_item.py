from abc import ABC, abstractmethod
from typing import List

class LibraryItem(ABC):
    """
    Abstract base class for library items.
    """

    def __init__(self, title: str, publication_year: int):
        """
        Initialize a LibraryItem.

        Parameters:
        - title (str): Title of the library item.
        - publication_year (int): Year of publication.
        """
        self._title = title.lower()
        self._publication_year = publication_year
        self._is_available = True

    @abstractmethod
    def __str__(self) -> str:
        """
        Represent the library item as a string.
        """
        pass

    @property
    def title(self) -> str:
        """
        Get the title of the library item.
        """
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        """
        Set the title of the library item.

        Parameters:
        - title (str): New title.
        """
        self._title = title

    @property
    def is_available(self) -> bool:
        """
        Check if the library item is available for loan.
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available: bool) -> None:
        """
        Set the availability status of the library item.

        Parameters:
        - is_available (bool): New availability status.
        """
        self._is_available = is_available