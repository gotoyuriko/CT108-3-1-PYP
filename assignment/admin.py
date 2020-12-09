admin = {}
with open("admin_login.txt") as f:
    for line in f:
        (key, val) = line.split()
        admin[key] = val


def admin_login():
    print("\n*** Admin Log In ***\n")
    print("Enter username and password")
    admin_username = input("User Name：")  # user name is 'yurikogoto34'
    admin_password = input("Password：")  # password is 'TP38121'
    if admin_username in admin and admin[admin_username] == admin_password:
        admin_function()
    else:
        print("\nIncorrect username or password\n")


def admin_function():
    print("\n*** Welcome Admin! ***\n")
    print("\t1. Add Record")
    print("\t2. Display All Record")
    print("\t3. Search Specific Record")
    print("\t4. Sort and Display Record")
    print("\t5. Modify Record")
    print("\t6. Exit")

    while True:
        choice = input("\nEnter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                admin_add()
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                print("\nLog out\n")
                break
            else:
                print("\nPlease enter 1 to 6")
                continue
        except:
            print("\n", choice, "is not a number")
            continue

# uncompete


def admin_add():
    print("\n\ta. Coach")
    print("\tb. Sport")
    print("\tc. Sport Schedule")
    choice = input("Choose one：")
    if choice == "a":
        pass
    elif choice == "b":
        pass
    elif choice == "c":
        pass
    else:
        print("\nPlease Enter a, b or c")


def admin_display():
    print("\n\ta. Coach")
    print("\tb. Sport")
    print("\tc. Registered Students")
    choice = input("Choose one：")
    if choice == "a":
        pass
    elif choice == "b":
        pass
    elif choice == "c":
        pass
    else:
        print("\nPlease Enter a, b or c")


def admin_search():
    print("\n\ta. Coach by Coach ID")
    print("\tb. Coach by overall performance (Rating)")
    print("\tc. Sport by Sport ID")
    print("\td. Student by Student ID")
    choice = input("Choose one：")
    if choice == "a":
        pass
    elif choice == "b":
        pass
    elif choice == "c":
        pass
    elif choice == "d":
        pass
    else:
        print("\nPlease Enter a, b or c")


def admin_sort():
    print("\n\ta. Coaches in ascending order by names.")
    print("\tb. Coaches Hourly Pay Rate in ascending order")
    print("\tc. Coaches Overall Performance in ascending order")
    choice = input("Choose one：")
    if choice == "a":
        pass
    elif choice == "b":
        pass
    elif choice == "c":
        pass
    else:
        print("\nPlease Enter a, b or c")


def admin_modify():
    print("\n\ta. Coach")
    print("\tb. Sport")
    print("\tc. Sport Schedule")
    choice = input("Choose one：")
    if choice == "a":
        pass
    elif choice == "b":
        pass
    elif choice == "c":
        pass
    else:
        print("\nPlease Enter a, b or c")
