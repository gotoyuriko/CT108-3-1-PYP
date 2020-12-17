from admin import *
from student_all import *
from student_registered import *

print("*** Welcome to REAL CHAMPION APORT ACADEMY! ***\n")
print("\tWho are you?")
print("\t1. Admin")
print("\t2. All Students(Registered / Not-Registered)")
print("\t3. Registered Student\n")

while 1:
    user = input("Enter the number: ")
    # try:
    user = int(user)
    if(user == 1):
        admin_login()
        break
    elif(user == 2):
        student_all()
        break
    elif(user == 3):
        student_login()
        break
    else:
        print("\nPlease enter 1 ,2 or 3\n")
        continue
    # except:
    #     print("\n", user, "is not a number\n")
    #     continue

print("See You !!\n")
