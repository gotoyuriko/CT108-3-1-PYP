'''
Account Number: 4266839393939
Credit Limit (before recession): 1000
Current debt balance: 200
=============================
Account Number: 4266839393939
Old Credit Limit: 1000
New Credit Limit: 500.0
The current debt balance not exceeded the new credit limit
=============================
Type 'y' to proceed to next account: y
Account Number: 4567890
Credit Limit (before recession): 890
Current debt balance: 900
=============================
Account Number: 4567890
Old Credit Limit: 890
New Credit Limit: 445.0
The current debt balance exceeded the new credit limit
=============================
Type 'y' to proceed to next account: n
'''
account_number = input("Account Number: ")
old_credit_limit = input("Credit Limit (before recession): ")
balance = ("Current debt balance: ")
print("=============================")
choice = "y"
while choice == "y":
    try:
        new_credit_limit = int(old_credit_limit) / 2
        new_balance = int(balance) - new_credit_limit

        if new_balance < 0:
            status = "exceeded"
        else:
            status = "not exceeded"

        print("=============================")
        print("Account Number:", account_number)
        print("Old Credit Limit:", old_credit_limit)
        print("New Credit Limit:", new_credit_limit)
        print("The current debt balance", status, "the new credit limit")

    except:
        print("Please Enter the Number")
        continue

    print("=============================")
    choice = input("Type 'y' to proceed to next account: ")
