def displayRecord():
    with open("pancakes.txt") as f:
        count = 0
        total_thickness = 0
        total_parameter = 0

        for number in f:
            number = number.strip("\n")  # to separate record line
            # to split each record into thickness and parameter
            value = number.split(",")
            print("Thickness: ", value[0], "\tParameters: ", value[1])

            total_thickness += float(value[0])
            total_parameter += float(value[1])

            count += 1

    print("\nTotal pancakes:", count)
    print("Average thickness:", total_thickness/count)
    print("Average parameter:", total_parameter/count)

    proceed = input("\nEnter 'y' to go back to main menu: ")

    if proceed == "y":
        main()


def addRecord():
    proceed = "y"
    while proceed == "y":
        print("\nAdd Pancake record:")
        thickness = input("Enter pancake thickness: ")
        parameter = input("Enter pancake parameter: ")

        with open("pancakes.txt", "a") as panckakef:
            panckakef.write("\n"+thickness+","+parameter)

        proceed = input("\nEnter 'y' to proceed: ")
    main()


def main():
    print("---------------")
    print("Pancake Kitchen")
    print("---------------")

    print("1. Add Pancake Record")
    print("2. Display Record")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addRecord()
    elif choice == 2:
        displayRecord()
    elif choice == 3:
        exit()
    else:
        print("Please Enter 1,2,and 3")


main()
