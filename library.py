from typing import List, Optional, Union
from datetime import date, timedelta
from book import Book
from magazine import Magazine
from user import User
from loan import Loan

class Library:
    """
    Class representing a library.
    """

    def __init__(self):
        """
        Initialize a Library.
        """
        self._books: List[Book] = []
        self._magazines: List[Magazine] = []
        self._users: List[User] = []
        self._loans: List[Loan] = []

    def add_library_item(self, library_item: Union[Book, Magazine]):
        """
        Add a library item to the library's collection.

        Parameters:
        - library_item: The library item to be added.
        """
        if isinstance(library_item, Book):
            self._books.append(library_item)
        elif isinstance(library_item, Magazine):
            self._magazines.append(library_item)
        else:
            raise TypeError("Library item must be of type Book or Magazine.")

    def remove_library_item(self, library_item: Union[Book, Magazine]):
        """
        Remove a library item from the library's collection.

        Parameters:
        - library_item: The library item to be removed.
        """
        if isinstance(library_item, Book):
            self._books.remove(library_item)
        elif isinstance(library_item, Magazine):
            self._magazines.remove(library_item)
        else:
            raise TypeError("Library item must be of type Book or Magazine.")

    def add_user(self, user: User):
        """
        Add a user to the library's user list.

        Parameters:
        - user: The user to be added.
        """
        self._users.append(user)

    def remove_user(self, user: User):
        """
        Remove a user from the library's user list.

        Parameters:
        - user: The user to be removed.
        """
        self._users.remove(user)

    def show_library_items(self):
        """
        Display all library items in the collection.
        """
        for item in self._books:
            print(item)
        for item in self._magazines:
            print(item)

    def show_users(self):
        """
        Display all users in the library.
        """
        for user in self._users:
            print(user)

    def make_loan(self, loan: Loan):
        """
        Make a loan and add it to the library's list of loans.

        Parameters:
        - loan: The loan to be added.
        """
        self._loans.append(loan)

    def search_library_items(self, title: str) -> Optional[Union[Book, Magazine]]:
        """
        Search for a library item by title.

        Parameters:
        - title (str): The title of the item to be searched.

        Returns:
        - LibraryItem or None: The found library item or None if not found.
        """
        title = title.lower()
        for item in self._books:
            if item.title == title:
                return item
        for item in self._magazines:
            if item.title == title:
                return item
        return None


       

library = Library()

b1 = Book("The Hobbit", 1937, "J.R.R. Tolkien", "Fantasy")
b2 = Book("The Fellowship of the Ring", 1954, "J.R.R. Tolkien", "Fantasy")
b3 = Book("The Two Towers", 1954, "J.R.R. Tolkien", "Fantasy")
b4 = Book("The Return of the King", 1955, "J.R.R. Tolkien", "Fantasy")
b5 = Book("The Silmarillion", 1977, "J.R.R. Tolkien", "Fantasy")
b6 = Book("Crime and Punishment", 1866, "Fyodor Dostoevsky", "Philosophical fiction")
b7 = Book("The Brothers Karamazov", 1880, "Fyodor Dostoevsky", "Philosophical fiction")


m1 = Magazine("The Economist", 1843,  "Business and Finance")
m2 = Magazine("National Geographic", 1888,  "Science")
m3 = Magazine("Time", 1923,  "News")
m4 = Magazine("The New Yorker", 1925, "News")

u1 = User(1, "John", 20)
u2 = User(2, "Jane", 25)

# if deactivate_subscription() is called, the user will not be able to make loans
# u2.deactivate_subscription()
# u2.activate_subscription()

l1 = Loan(b1, u1, date.today() - timedelta(days=10), date.today() - timedelta(days=5))
l2 = Loan(b2, u1, date.today() - timedelta(days=5))
l3 = Loan(b3, u2, date.today() - timedelta(days=3))
l4 = Loan(b4, u1, date.today() - timedelta(days=5), date.today() - timedelta(days=1))



# add library items to the library
library.add_library_item(b1)
library.add_library_item(b2)
library.add_library_item(b3)
library.add_library_item(b4)
library.add_library_item(b5)
library.add_library_item(b6)
library.add_library_item(b7)

library.add_library_item(m1)
library.add_library_item(m2)
library.add_library_item(m3)
library.add_library_item(m4)

# add users to the library
library.add_user(u1)
library.add_user(u2)


# make loans
library.make_loan(l1)
library.make_loan(l2)
library.make_loan(l3)
library.make_loan(l4)


# show library items
library.show_library_items()


print('------------------\n')

# search for a library item
item1 = library.search_library_items("The Hobbit")
item2 = library.search_library_items("The Economist")
item3 = library.search_library_items("The Economist2")
print(item1)
print(item2)
print(item3) # should be None

print('------------------\n')


# show the items that a user has borrowed
items_borrowed_by_u1 = u1.show_borrowed_items()