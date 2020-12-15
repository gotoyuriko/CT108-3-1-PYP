import json


def admin_login():  # Login to Access System.
    while True:
        print("\n*** Admin Log In ***\n")
        print("Enter username and password")
        admin_username = input("User Name：")  # user name is 'yurikogoto5839'
        admin_password = input("Password：")  # password is 'iDpDZO871dAn'

        adminf = open("admin_login.txt")
        admin_data = adminf.read()
        admin_dict = json.loads(admin_data)

        if admin_username in admin_dict and admin_dict[admin_username] == admin_password:
            admin_function()
            break
        else:
            print("\nIncorrect username or password\n")

        adminf.close()


def admin_function():  # after login
    while True:
        print("\n*** Admin login successful! ***\n")
        print("\t1. Add Record")
        print("\t2. Display All Records")
        print("\t3. Search Specific Record")
        print("\t4. Sort and Display Record")
        print("\t5. Modify Record")
        print("\t6. Exit")

        choice = input("\nEnter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                admin_add()
            elif choice == 2:
                admin_display()
            elif choice == 3:
                admin_search()
            elif choice == 4:
                admin_sort()
            elif choice == 5:
                pass
            elif choice == 6:
                print("\nLog Out\n")
                break
            else:
                print("\nPlease enter 1 to 6")
                continue
        except:
            print("\n", choice, "is not a number")
            continue


def admin_add():  # Add Record
    print("==================================")
    print("\n\ta. Coach")
    print("\tb. Sport")
    print("\tc. Sport Schedule")
    choose = input("Choose one：")
    if choose == "a":
        coachf = open("coach.txt")
        coachf.close()
    elif choose == "b":
        pass
    elif choose == "c":
        pass
    else:
        print("\nPlease Enter a, b or c")


def admin_display():  # Display All Records
    print("==================================")
    print("\n\ta. Coach")
    print("\tb. Sport")
    print("\tc. Registered Students")
    choose = input("\nChoose one：")

    if choose == "a":  # Coach
        coachf = open("coach.txt")
        coach_data = coachf.read()
        coach_dict = json.loads(coach_data)

        print("\n*** Here are all records of coaches ***\n")
        for coach in coach_dict:
            print("\tCouach ID:", coach["Couach ID"])
            print("\tName:", coach["Name"])
            print("\tDate Joined:", coach["Date Joined"])
            print("\tDate Terminated:", coach["Date Terminated"])
            print("\tHorly Rate (RM/h):", coach["Horly Rate (RM/h)"])
            print("\tSport Center Code:", coach["Sport Center Code"])
            print("\tSport Center Name:", coach["Sport Center Name"])
            print("\tSport Code:", coach["Sport Code"])
            print("\tSport Name:", coach["Sport Name"])
            print("\tRating:", coach["Rating"], "\n")
        coachf.close()
    elif choose == "b":  # Sport
        sportf = open("coach.txt")
        sport_data = sportf.read()
        sport_dict = json.loads(sport_data)

        print("\n*** Here are all records of sports ***\n")
        for coach in sport_dict:
            print("\tSport Code:", coach["Sport Code"])
            print("\tSport Name:", coach["Sport Name"], "\n")
        sportf.close()
    elif choose == "c":  # Registered Students
        pass
    else:
        print("\nPlease Enter a, b or c")


def admin_search():  # Search Specific Records of
    print("==================================")
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


def admin_sort():  # Sort and Display Record
    print("==================================")
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


def admin_modify():  # Modify Record
    print("==================================")
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
