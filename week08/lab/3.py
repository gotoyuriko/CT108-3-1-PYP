'''
The Domestic Gas Supply Company bills its customers according to the following rate: if the customer’s usage is 60 cubic metres or less, a rate of $2.00 per cubic metre is applied; if the customer’s usage is more than 60 cubic metres, then a rate of $1.75 per cubic metre is applied for the first 60 cubic metres and $1.50 per cubic metre for the remaining usage.
Design a program that will read the customer gas usage in cubic metres, calculate the amount owing for gas usage for each customer in function named calc_amount_owing(), and print a total of gas usage and the amount owing at the end of the program.
'''


def calc_amoubt_owning(gas_usage):
    if gas_usage <= 60:
        amount_owning = gas_usage * 2.00
    else:
        amount_owning = (60 * 1.75) + (gas_usage-60) * 1.50
    return amount_owning


customer = 0
choice = "y"
total_gas = 0
total_amount_owning = 0

while choice == "y":
    print("\nCustomer", customer+1)
    print("-------------")
    gas_usage = float(input("Enter gas usage: "))
    print("Amount owing:{:.2f}".format(calc_amoubt_owning(gas_usage)))
    total_gas += gas_usage
    total_amount_owning += calc_amoubt_owning(gas_usage)
    customer += 1
    choice = input("\nEnter 'y' to proceed:")

print("\nTotal Gas Usage:{:.2f}".format(total_gas))
print("Average Gas Usage:{:.2f}".format(total_gas/customer))
print("Total Gas Usage:{:.2f}".format(total_amount_owning))
