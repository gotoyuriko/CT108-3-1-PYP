choice = "y"

while choice == "y":
    marks = input("Enter your marks: ")
    try:
        marks = int(marks)
        if marks > 100 or marks < 0:
            grade = "invalid"
        else:
            if marks <= 49:
                grade = "F"
            elif marks <= 59:
                grade = "D"
            elif marks <= 69:
                grade = "C"
            elif marks <= 79:
                grade = "B"
            elif marks <= 100:
                grade = "A"

        print("Your grade is", grade)

    except:
        print(marks, "is not a nubmer")

    choice = input("\nEnter 'y' to proceed or other character to end: ")
