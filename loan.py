from datetime import date, timedelta, datetime
from typing import List, Optional
from book import Book
from user import User
from subscription_error import SubscriptionError
from library_item import LibraryItem


class Loan:
    """
    Class representing a loan in the library.
    """

    def __init__(self, library_item: LibraryItem, user: User, loan_date: date, return_date: Optional[date] = None):
        """
        Initialize a Loan.

        Parameters:
        - library_item (LibraryItem): Item being loaned.
        - user (User): User making the loan.
        - loan_date (date): Date when the loan was made.
        - return_date (Optional[date]): Date when the item is expected to be returned.
        """
        if not user._subscription_active:
            print("User does not have an active subscription.")
            raise SubscriptionError("User does not have an active subscription.")

        if return_date is not None and return_date < loan_date:
            raise ValueError("Return date cannot be before loan date.")

        if not library_item.is_available:
            print("Library item is not available.")
            raise ValueError("Library item is not available.")

        self._library_item = library_item
        self._user = user
        self._loan_date = loan_date
        self._return_date = return_date

        if return_date is None:
            self._is_active_loan = True
        else:
            self._is_active_loan = False
            self._library_item.is_available = True

        user.add_item(library_item)
        library_item.is_available = False

    def calculate_loan_days(self) -> int:
        """
        Calculate the number of days the item has been on loan.

        Returns:
        - int: Number of days on loan.
        """
        if self._return_date is None:
            return (date.today() - self._loan_date).days
        else:
            return (self._return_date - self._loan_date).days

    def __str__(self) -> str:
        """
        Represent the loan as a string.
        """
        return f"Loan: {self._library_item}, {self._user}, {self._loan_date}, {self._return_date}"
    

    
# b1 = Book("The Hobbit", 1937, "J.R.R. Tolkien", "Fantasy")
# b2 = Book("The Fellowship of the Ring", 1954, "J.R.R. Tolkien", "Fantasy")
# b3 = Book("The Two Towers", 1954, "J.R.R. Tolkien", "Fantasy")
# b4 = Book("The Return of the King", 1955, "J.R.R. Tolkien", "Fantasy")
# b5 = Book("The Silmarillion", 1977, "J.R.R. Tolkien", "Fantasy")

# u1 = User(1, "John", 20)
# u2 = User(2, "Jane", 25)
# # u2.deactivate_subscription()
# print(u2._subscription_active)



# l1 = Loan(b1, u1, date.today() - timedelta(days=10))
# l2 = Loan(b2, u1, date.today() - timedelta(days=5))
# l4 = Loan(b4, u1, date.today() - timedelta(days=5), date.today() - timedelta(days=1))
# l3 = Loan(b3, u2, date.today() - timedelta(days=3))

# print(l1.calculate_loan_days())
# print(l4.calculate_loan_days())

# # see the items that a user has borrowed
# u1.show_borrowed_items()
