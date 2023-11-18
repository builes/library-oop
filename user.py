from typing import List, Optional
from library_item import LibraryItem

class User:
    """
    Class representing a user in the library.
    """

    def __init__(self, user_id: int, name: str, age: int):
        """
        Initialize a User.

        Parameters:
        - user_id (int): Unique identifier for the user.
        - name (str): Name of the user.
        - age (int): Age of the user.
        """
        self._name = name.lower()
        self._age = age
        self._id = user_id
        self._subscription_active = True
        self._borrowed_items: List[LibraryItem] = []

    def __str__(self) -> str:
        """
        Represent the user as a string.
        """
        return f"{self._name} is {self._age} years old"

    def deactivate_subscription(self) -> None:
        """
        Deactivate the subscription of the user.
        """
        self._subscription_active = False

    def activate_subscription(self) -> None:
        """
        Activate the subscription of the user.
        """
        self._subscription_active = True

    def add_item(self, item: LibraryItem) -> None:
        """
        Add an item to the list of items borrowed by the user.

        Parameters:
        - item (LibraryItem): Item to be added.
        """
        self._borrowed_items.append(item)

    def remove_item(self, item: LibraryItem) -> None:
        """
        Remove an item from the list of items borrowed by the user.

        Parameters:
        - item (LibraryItem): Item to be removed.
        """
        self._borrowed_items.remove(item)

    def show_borrowed_items(self) -> None:
        """
        Display the items borrowed by the user.
        """
        for item in self._borrowed_items:
            print(item)
    

    
# u1 = User(1, "John", 20)
# print(u1)
   