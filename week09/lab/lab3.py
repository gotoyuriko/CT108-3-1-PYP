def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


proceed = "y"

while proceed == "y":
    print("\nCalculator Program\n------------------")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = int(input("\nChoose the operation from the options above: "))

    if choice < 1 or choice > 4:
        result = 0
        operator = ""
        print("\nChoice out of range")
        continue
    else:
        first = int(input("\nEnter first number: "))
        second = int(input("Enter second number: "))

        if choice == 1:
            result = add(first, second)
            operator = "+"
        elif choice == 2:
            result = subtract(first, second)
            operator = "-"
        elif choice == 3:
            result = multiply(first, second)
            operator = "×"
        elif choice == 4:
            result = divide(first, second)
            operator = "÷"

    if operator != "":
        print("\nResult:", first, operator, second, "=", result)
        # file control starts from here
        file_name = "numbers.txt"

        # to check if the file is available
        try:
            f = open(file_name, "x")
            mode = "r"  # to be used in line 56
        except:
            mode = "r"  # to be used in line 56
        # ---------------------------------
        # to check if the file is empty or not
        count = 0
        f = open(file_name, mode)
        for number in f:
            count += 1
        # ---------------------------------
        # if file is empty, the first line should be without \n
        if count == 0:
            new_line = ""  # to be used in line 67
        else:
            new_line = "\n"  # to be used in line 67
        # write into file
        f = open(file_name, "a")
        f.write(new_line+str(result))
        f.close()
        # file control ends here

        proceed = input("\nEnter 'y' to proceed: ")

f = open(file_name)
count = 0
grand_total = 0
for number in f:
    number = number.strip()  # read each record, strip new line
    grand_total += float(number)
    count += 1
f.close()

print("\nTotal numbers in file: ", count)
print("Total sum of numbers in file: ", grand_total)
print("Average: ", (grand_total/count))
