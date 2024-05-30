"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
from Account import SavingsAccount

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    my_savings_acct = SavingsAccount(balance,interest_rate, months)
    # Calculate interest earned
     # ADD YOUR CODE HERE
    int_earned = ( ( balance * (interest_rate/100)) / 12 * months )
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    my_savings_acct.set_balance(my_savings_acct.get_balance()+int_earned)
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    return_savings_data = "The updated savings balance is "+format(my_savings_acct.get_balance(), ',.2f') +" and interested earned is "+format(int_earned, ',.2f')
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    return_savings_data_list = [format(my_savings_acct.get_balance(), ',.2f') ,format(int_earned, ',.2f')]
    # Return the updated balance and interest earned.
    return  return_savings_data_list

if __name__ == "__main__":
    # Incorrect order.
    print(create_savings_account(1000,6,12))