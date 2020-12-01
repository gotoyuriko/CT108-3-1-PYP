choice = "y"

while choice == "y":
    selling_price = input("Enter selling price($): ")
    buying_price = input("Enter buying price($): ")

    try:
        profit_or_loss = selling_price - buying_price

        if profit_or_loss < 0:
            print("You have loss of " + str(profit_or_loss) +
                  " in trading of this system.")
        else:
            print("You have profit of " + str(profit_or_loss) +
                  " in trading of this system.")
    except:
        print("wrong input")

    choice = input("\nEnter 'y' to proceed or other character to end: ")
