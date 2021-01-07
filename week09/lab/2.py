def displayRecord():
    file_name = "pancakes.txt"

    f = open(file_name)

    count=0
    total_thickness=0
    total_parameter=0

    for number in f:
        number = number.strip("\n") #to separate record line
        value = number.split(",") #to split each record into thickness and parameter
        print("Thickness: ",value[0],"\tParameters: ",value[1])

        total_thickness+=float(value[0])
        total_parameter+=float(value[1])
            
        count+=1

    print("\nTotal pancakes:",count)
    print("Average thickness:",total_thickness/count)
    print("Average parameter:",total_parameter/count)

    f.close()

    proceed = input("\nEnter 'y' to go back to main menu: ")

    if proceed=="y":
        main()

def addRecord():
    proceed="y"
    while proceed=="y":
        print("\nAdd Pancake record:")
        thickness=input("Enter pancake thickness: ")
        parameter=input("Enter pancake parameter: ")

        file_name = "pancakes.txt"
        f = open(file_name, "a")
        f.write("\n"+thickness+","+parameter)
        f.close()

        proceed = input("\nEnter 'y' to proceed: ")
    main()

def main():
    print("\n----------------\nPancake Kitchen\n----------------\n")
    print("1. Add Pancake Record\n2. Display Record\n3. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice==1:
        addRecord()
    elif choice==2:
        displayRecord()
    elif choice==3:
        exit()
    else:
        print("Wrong input!")

main()
