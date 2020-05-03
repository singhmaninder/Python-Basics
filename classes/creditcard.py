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

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0
    
    def get_customer(self):
        """Return name of the customer."""
        return self._customer
    
    def get_bank(self):
        """Return the bank's name."""
        return self._bank
    
    def get_account(self):
        """Return the card identifying number."""
        return self._account
    
    def get_limit(self):
        """Return current credit limit."""
        return self._limit
    
    def get_balance(self):
        """Return current balance."""
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:    # if charge would exceed limit,
            return False                           # can't accept charge
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

if __name__ == '__main__':
    my_card = CreditCard('Maninder Singh', 'HDFC BANK', '9810 1234', 100000)

    assert my_card.get_customer() == 'Maninder Singh'
    assert my_card.get_bank() == 'HDFC BANK'
    assert my_card.get_account() == '9810 1234'
    assert my_card.get_limit() == 100000
    assert my_card.get_balance() == 0
    my_card.charge(5000)
    assert my_card.get_balance() == 5000
    my_card.make_payment(800)
    assert my_card.get_balance() == 4200
    assert my_card.charge(200000) == False