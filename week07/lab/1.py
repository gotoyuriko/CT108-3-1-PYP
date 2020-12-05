product_code = ["s101", "x667", "d870", "c489", "k567"]
product_name = ["Writing Pad", "Envelope", "Pen", "Stapler", "Planner"]
price_per_unit = [5.00, 4.50, 2.99, 15.99, 59.99]
choice = "y"
sum = 0
while choice == "y":

    code = input("\nProduct Code: ")
    quantity = input("Quantity: ")
    try:
        quantity = int(quantity)

        if code in product_code:
            index = product_code.index(code)
            price = price_per_unit[index] * float(quantity)
            print(product_name[index], "×", quantity,
                  "=", '{:.2f}'.format(price))
            sum = sum + price
            choice = input("\nType 'y' to proceed: ")
        else:
            print("Product Code Not Exist\n")
            continue
    except:
        print(quantity, "is not a number")
        continue

print("\n===============")
print("Total Price: ", '{:.2f}'.format(sum))
