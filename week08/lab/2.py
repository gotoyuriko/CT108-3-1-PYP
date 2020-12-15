'''
Write a program which will accepts item prices from the user. It will then calls a function called calculatediscount() to calculate the total price by deducting the discount offered in the following table.
'''


def calculatediscount(count, total):
    if count == 1:
        total = float(total)*0.8
    elif count == 2:
        total = float(total)*0.7
    elif count >= 3:
        total = float(total)*0.6
    return total


def tax(total):
    if total <= 100:
        after_tax = total*1.05
    else:
        after_tax = total*1.10
    return after_tax


count = 0
choice = "y"
total = 0
while choice == "y":
    print("\nItem ", count+1)
    price = input("Price: ")

    total += float(price)
    count += 1

    choice = input("\nEnter 'y' to proceed: ")


print("Total price for", count,
      "item(s) before discount: {:.2f}".format((total)))
print("Total price for", count, "item(s) after discount: {:.2f}".format(
    calculatediscount(count, total)))
print("Total price for 2 item(s) after tax: {:.2f}".format(
    tax(calculatediscount(count, total))))
