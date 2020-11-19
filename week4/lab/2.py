male = 0
female = 0
student = 0

print("Enter ‘-1’ to stop or to any number to continue")
choice = int(input())

while choice!=-1:
    print("Enter student information")
    student_name = input("Name: ")
    gender = input("Gender (M for Male, F for Female): ")    
    age = int(input("Age: "))

    if gender=="M":
        male=male+1
    elif gender=="F":
        female=female+1
    else:
        print("Wrong Input")
        break

    student = student+1

    print("Enter ‘-1’ to stop or to any number to continue")
    choice = int(input())
    print("********************************")
    
print("Number of students entered: ", str(student))
print("Gender breakdown: ", str(male), "Male, ", str(female), "Female")
