""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

    def get_balance(self):
        return self.balance
    
    def get_interest(self):
        return self.interest
    
class CDAccount(Account):
    """Creating a CD Account class with parameters and methods"""
    def __init__(self, balance, interest, month): # ADD YOUR CODE HERE
       # Call the parent class's __init__ method and pass the required arguments
        Account.__init__(self, balance, interest)
        self.month=month
        # ADD YOUR CODE HERE

    # This method gets the length of months for the CD.
    def get_months(self):
        return self.month
        """Gets the length of the CD"""
        # ADD YOUR CODE HERE

class SavingsAccount(Account):
    """Creating a Savings Account class with parameters and methods"""
    def __init__(self, balance, interest, month): # ADD YOUR CODE HERE
       # Call the parent class's __init__ method and pass the required arguments
        Account.__init__(self, balance, interest)
        self.month=month
        # ADD YOUR CODE HERE

    # This method gets the length of months for the CD.
    def get_months(self):
        return self.month
        """Gets the length of the CD"""
        # ADD YOUR CODE HERE        