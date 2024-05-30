"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
from Account import CDAccount
       
def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.
    my_acct = Account("Toyota", "Camry", "Sedan", "2.5L", 2022, "Silver", "Yes", "Yes", "No", "No")
    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    my_acct = CDAccount(balance,interest_rate, months)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    int_earned = ( ( balance * (interest_rate/100)) / 12 * months )


    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    my_acct.set_balance(my_acct.get_balance()+int_earned)
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    return_data = "The updated cd balance is "+format(my_acct.get_balance(), ',.2f') +" and interested earned is "+format(int_earned, ',.2f')
    return_data_list = [format(my_acct.get_balance(), ',.2f') ,format(int_earned, ',.2f')]

    # Return the updated balance and interest earned.
    return  return_data_list

if __name__ == "__main__":
    # Incorrect order.
    print(create_cd_account(1000,6,12))