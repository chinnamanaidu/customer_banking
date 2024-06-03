"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
       
def create_cd_account(balance, interest_rate, months):
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    my_acct = Account(balance,interest_rate)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    int_earned = ( ( balance * (interest_rate/100) / 12) * months )


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