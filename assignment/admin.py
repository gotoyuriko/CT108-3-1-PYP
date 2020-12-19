import json


def admin_login():  # Login to Access System.
    while 1:
        print("\n*** Admin Log In ***\n")
        print("Enter username and password")
        admin_username = input("User Name：")  # user name is 'yurikogoto5839'
        admin_password = input("Password：")  # password is 'iDpDZO871dAn'

        with open("admin_login.txt") as adminf:
            admin_data = adminf.read()
            admin_dict = json.loads(admin_data)

            if admin_username in admin_dict and admin_dict[admin_username] == admin_password:
                admin_function()
                break
            else:
                print("\nIncorrect username or password\n")


def admin_function():  # after login
    while 1:
        print("\n*** Admin Page ! ***\n")
        print("\t1. Add Record")
        print("\t2. Display All Records")
        print("\t3. Search Specific Record")
        print("\t4. Sort and Display Record")
        print("\t5. Modify Record")
        print("\t6. Exit")

        choice = input("\nEnter your choice: ")
        # try:
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
            admin_modify()
        elif choice == 6:
            print("\nLog Out\n")
            break
        else:
            print("\nPlease enter 1 to 6")
            continue
        # except:
            # print("\n", choice, "is not a number")
            # continue


def admin_add():  # Add Record
    print("==================================")
    print("\n\ta. Coach")
    print("\tb. Sport")
    print("\tc. Sport Schedule")
    choice = input("\nChoose one：")

    # coach
    if choice == "a":
        coach = {}
        print("\n*** Please Fill in your information below ***")
        coach["Couach ID"] = input("Couach ID: ")
        coach["Name"] = input("Name: ")
        coach["Date Joined"] = input("Date Joined: ")
        coach["Date Terminated"] = input("Date Terminated: ")
        coach["Horly Rate (RM/h)"] = input("Horly Rate (RM/h): ")
        coach["Phone"] = input("Phone: ")
        coach["Adress"] = input("Adress: ")

        # Check Sport center code in this system
        flag = 0
        while flag == 0:
            sport_center_code = input("Sport Center Code: ")
            with open("sport_center.txt") as sportcenterf:
                sportcenter_data = sportcenterf.read()
                sportcenter_list = json.loads(sportcenter_data)

                for sportcenter in sportcenter_list:
                    if sportcenter["Sport Center Code"] == sport_center_code:
                        coach["Sport Center Code"] = sport_center_code
                        coach["Sport Center Name"] = sportcenter["Sport Center Name"]
                        flag = 1
                        break
            if flag == 1:
                break
            print("There is no", sport_center_code, "in this system")

        # Check sport code in this system
        flag = 0
        while flag == 0:
            sport_code = input("Sport Code: ")
            with open("sport.txt") as sportf:
                sport_data = sportf.read()
                sport_list = json.loads(sport_data)
                for sport in sport_list:
                    if sport["Sport Code"] == sport_code:
                        coach["Sport Code"] = sport_code
                        coach["Sport Name"] = sport["Sport Name"]
                        flag = 1
                        break
            if flag == 1:
                break
            print("There is no", sport_code, "in this system")

        # read coach files and append data
        with open("coach.txt", "r") as coachf:
            coach_data = coachf.read()
            coach_list = json.loads(coach_data)
            coach_list.append(coach)
            encode_coach = json.dumps(coach_list)
        with open("coach.txt", "w") as coachf:
            coachf.write(encode_coach)

        print("\n★★★Complete★★★")

    # sport
    elif choice == "b":
        sport = {}

        # read sport files and append data
        with open("sport.txt", "r") as sportf:
            sport_data = sportf.read()
            sport_list = json.loads(sport_data)

            flag = 0
            while flag == 0:
                print("\n*** Please Fill in your information below ***")
                sport_code = input("Sport Code: ")
                sport_name = input("Sport Name: ")
                # Check if the sport.txt already had input or not
                for sport in sport_list:
                    if sport["Sport Code"] == sport_code or sport["Sport Name"] == sport_name:
                        print(sport_code, "or", sport_name,
                              "are already stored")
                        flag = 0
                        break
                    else:
                        flag = 1
                if flag == 1:
                    sport["Sport Code"] = sport_code
                    sport["Sport Name"] = sport_name
                    break

        sport_list.append(sport)
        encode_sport = json.dumps(sport_list)

        with open("sport.txt", "w") as sportf:
            sportf.write(encode_sport)

        print("\n★★★Complete★★★")

    # Scedule
    elif choice == "c":
        pass
    else:
        print("\nPlease Enter a, b or c")


def admin_display():  # Display All Records
    print("==================================")
    print("\n\ta. Coach")
    print("\tb. Sport")
    print("\tc. Registered Students")
    choice = input("\nChoose one：")

    if choice == "a":  # Coach
        with open("coach.txt") as coachf:
            coach_data = coachf.read()
            coach_list = json.loads(coach_data)

            print("\n*** Here are all records of coaches ***\n")
            for coach in coach_list:
                print("\tCouach ID:", coach["Couach ID"])
                print("\tName:", coach["Name"])
                print("\tDate Joined:", coach["Date Joined"])
                print("\tDate Terminated:", coach["Date Terminated"])
                print("\tHorly Rate (RM/h):", coach["Horly Rate (RM/h)"])
                print("\tPhone:", coach["Phone"])
                print("\tAdress", coach["Adress"])
                print("\tSport Center Code:", coach["Sport Center Code"])
                print("\tSport Center Name:", coach["Sport Center Name"])
                print("\tSport Code:", coach["Sport Code"])
                print("\tSport Name:", coach["Sport Name"])
                print("\tRating:", coach["Rating"], "\n")

    elif choice == "b":  # Sport
        with open("sport.txt") as sportf:
            sport_data = sportf.read()
            sport_list = json.loads(sport_data)

            print("\n*** Here are all records of sports ***\n")
            for coach in sport_list:
                print("\tSport Code:", coach["Sport Code"])
                print("\tSport Name:", coach["Sport Name"], "\n")

    elif choice == "c":  # Registered Students
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
