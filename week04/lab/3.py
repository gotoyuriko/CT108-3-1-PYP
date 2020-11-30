days = int(input("Enter number of days taken to make payment "))
amount = int(input("Enter order amount "))
discount = 0

if days <= 10:
    if amount > 1000:
        discount = 4
    else:
        if ((amount >= 500) and (amount <= 1000)):
            discount = 2

discountedAmount = amount - (amount * discount/100)
print("The discounted amount is RM%.2f" % discountedAmount)
