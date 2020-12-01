choice = "y"

while choice == "y":
    student_name = input("Enter your name : ")
    student_marks = input("Enter your marks: ")

    try:
        student_marks = int(student_marks)
    except:
        print(student_marks, " is not a number")
        student_marks = -1

    if student_marks != -1:
        if student_marks < 0 or student_marks > 100:
            print("Out of Range")
        else:
            if student_marks >= 50 and student_marks <= 100:
                result = "Passed"
            else:
                result = "Failed"
            print(student_name + ", you have", result, "the module")

    choice = input("\nEnter 'y' to proceed or other character to end: ")
