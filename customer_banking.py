# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print(" Enter the Savings Account details ")
    savings_balance = float(input("Enter the Savings Account Balance "))
    print(" Enter the interests in in percentage format ex 6% is 6 ")
    savings_interest = float(input("Enter the Savings Interest Rate "))

    savings_maturity = float(input("Enter the Maturity for Savings in months "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print("The interest earned for given months :" + str(interest_earned)  + " updated Savings with interest earned for the given months :" + str(updated_savings_balance) )
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print(" Enter the Savings Account details ")
    cd_balance = float(input("Enter the CD Account Balance "))
    print(" Enter the interests in in percentage format ex 6% is 6 ")
    cd_interest = float(input("Enter the CD Interest Rate "))

    cd_maturity = float(input("Enter the Maturity for CD in months "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    print("The interest earned for given months :" + str(interest_earned)  + " updated CD with interest earned for the given months :" + str(updated_cd_balance) )
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

if __name__ == "__main__":
    # Call the main function.
    main()
