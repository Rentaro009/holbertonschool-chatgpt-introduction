Checkbook Program Documentation
Overview
The Checkbook program is a simple Python script that simulates a basic checkbook register. It allows a user to:

Deposit money
Withdraw money
Check the current balance
Exit the program
The program runs in an interactive loop, allowing the user to perform multiple transactions.

Requirements
Python 3.x
No additional dependencies
Class: Checkbook
The Checkbook class maintains a users balance and provides methods to modify and retrieve it.

Methods:
__init__(self)
Initializes the checkbook with a balance of $0.00.
deposit(self, amount)
Adds the specified amount to the balance.
Prints a confirmation message and displays the updated balance.
Example Usage:
python
Copy
Edit
cb.deposit(100.50)
Output:
bash
Copy
Edit
Deposited $100.50
Current Balance: $100.50
withdraw(self, amount)
Deducts the specified amount from the balance if funds are available.
If the withdrawal amount exceeds the balance, it prints an insufficient funds message.
Example Usage:
python
Copy
Edit
cb.withdraw(50)
Output (if sufficient funds):
bash
Copy
Edit
Withdrew $50.00
Current Balance: $50.50
Output (if insufficient funds):
css
Copy
Edit
Insufficient funds to complete the withdrawal.
get_balance(self)
Prints the current balance.
Example Usage:
python
Copy
Edit
cb.get_balance()
Output:
bash
Copy
Edit
Current Balance: $50.50
Function: main()
Handles user interaction by:

Creating an instance of Checkbook.
Running a loop to accept user input for depositing, withdrawing, checking balance, or exiting.
Performing the requested action.
Handling invalid inputs.
Example Interaction
vbnet
Copy
Edit
What would you like to do? (deposit, withdraw, balance, exit): deposit
Enter the amount to deposit: $200
Deposited $200.00
Current Balance: $200.00

What would you like to do? (deposit, withdraw, balance, exit): withdraw
Enter the amount to withdraw: $50
Withdrew $50.00
Current Balance: $150.00

What would you like to do? (deposit, withdraw, balance, exit): balance
Current Balance: $150.00

What would you like to do? (deposit, withdraw, balance, exit): exit
Possible Improvements
Input Validation: Ensure only valid numbers are entered for deposits/withdrawals.
Persistent Storage: Save the balance to a file so it persists across runs.
Error Handling: Handle cases where users enter non-numeric values.
User Authentication: Add a simple password system for security.
Running the Program
To execute the script:

bash
Copy
Edit
python3 checkbook.py
The program will prompt the user for input.
