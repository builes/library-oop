class SubscriptionError(Exception):
    """
    Custom exception for subscription-related errors.
    """

    def __init__(self, message: str = "Subscription Error"):
        """
        Initialize a SubscriptionError.

        Parameters:
        - message (str): Error message.
        """
        self.message = message
        super().__init__(self.message)