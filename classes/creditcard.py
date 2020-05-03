class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, account, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g., 'Maninder Singh')
        bank      the name of the bank (e.g., 'HDFC Bank')
        account   the account identifier (e.g., '5391 01234 9862')
        limit     credit limit (measured in rupees)
        """ 