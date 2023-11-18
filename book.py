from typing import List, Optional
from library_item import LibraryItem

class Book(LibraryItem):
    """
    Class representing a book in the library.
    """

    total_books = 0
    books: List['Book'] = []

    def __init__(self, title: str, publication_year: int, author: str, genre: str):
        """
        Initialize a Book.

        Parameters:
        - title (str): Title of the book.
        - publication_year (int): Year of publication.
        - author (str): Author of the book.
        - genre (str): Genre of the book.
        """
        super().__init__(title, publication_year)
        self._author = author.lower()
        self._genre = genre.lower()

        Book.total_books += 1
        Book.books.append(self)

    def __str__(self) -> str:
        """
        Represent the book as a string.
        """
        return f"{self._title} by {self._author} and was published in ({self._publication_year})"

    @classmethod
    def find_book_by_title(cls, title: str) -> Optional['Book']:
        """
        Find a book by title.

        Parameters:
        - title (str): Title to search for.

        Returns:
        - Optional[Book]: Found book or None if not found.
        """
        for book in cls.books:
            if book.title == title.lower():
                return book
        return None


    
# instantiate some books
# b1 = Book("The Hobbit", 1937, "J.R.R. Tolkien", "Fantasy")
# b2 = Book("The Fellowship of the Ring", 1954, "J.R.R. Tolkien", "Fantasy")
# b3 = Book("The Two Towers", 1954, "J.R.R. Tolkien", "Fantasy")
# b4 = Book("The Return of the King", 1955, "J.R.R. Tolkien", "Fantasy")
# b5 = Book("The Silmarillion", 1977, "J.R.R. Tolkien", "Fantasy")

# here we find the book by title
# print(Book.find_book_by_title("The Hobbit" ))
# print(Book.find_book_by_title("The Return of the King" ))
# print(Book.find_book_by_title("The Return of the Kingg" ))

# getter and setter are inherited from the parent class
# print(b1.is_available)
# b1.is_available = False
# print(b1.is_available)

# access the class attribute
# print(Book.total_books)
