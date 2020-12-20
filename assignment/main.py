from admin import *
from student_all import *
from student_registered import *

print("\n*** Welcome to REAL CHAMPION APORT ACADEMY! ***\n")
print("\tWho are you?\n\t1. Admin\n\t2. All Students(Registered / Not-Registered)\n\t3. Registered Student\n")

while 1:

    # try:
    user = int(input("\tEnter the number: "))
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

print("\n*** Log Out ***")
print("★★★ See You ★★★\n")
