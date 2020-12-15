def student_all():
    print("\n*** Student Page! ***\n")
    print("\t1. View details of...")
    print("\t2. If new student Register to Access other Details")
    print("\t3. Exit")
    while True:
        choice = input("\nEnter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                view_details()
            elif choice == 2:
                student_signup()
            elif choice == 3:
                print("\nLog Out\n")
                break
            else:
                print("\nPlease enter 1 to 3")
                continue
        except:
            print("\n", choice, "is not a number")
            continue


def view_details():
    pass


def student_signup():
    print("\n*** Student Log In ***\n")
    print("Enter username and password")
    admin_username = input("User Name：")  # user name is 'yurikogoto34'
    admin_password = input("Password：")  # password is 'TP38121'
    if admin_username in student and student[admin_username] == admin_password:
        admin_function()
    else:
        print("\nIncorrect username or password\n")


def student_registered():
    pass
