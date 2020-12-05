from admin import *

print("*** Welcome to Sport Academy System ***\n")
print("\tWho are you?")
print("\t1. Admin")
print("\t2. Student\n")

while True:
    user = input("Enter the number: ")
    try:
        user = int(user)
        if(user == 1):
            admin_login()
            break
        elif(user == 2):
            student_function()
            break
        else:
            print("\nPlease enter 1 or 2.\n")
            continue
    except:
        print("\n", user, "is not a number\n")
        continue
