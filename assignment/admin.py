import json


def admin_login():  # Login to Access System.
    continuey = "y"
    while continuey == "y":
        print("\n*** Admin Log In ***\n")
        print("\tEnter username and password")
        admin_username = input("\tUser Name：")
        admin_password = input("\tPassword：")

        with open("admin_login.txt") as adminf:
            admin_data = adminf.read()
            admin_dict = json.loads(admin_data)

        if admin_username in admin_dict and admin_dict[admin_username] == admin_password:
            admin_function()
            break
        else:
            print("\n\tIncorrect username or password\n")

        continuey = input("\tEnter 'y' to type username and password again: ")


def admin_function():  # admin page
    while 1:
        print("\n*** Admin Page ! ***\n")
        print("\t1. Add Record")
        print("\t2. Display All Records")
        print("\t3. Search Specific Record")
        print("\t4. Sort and Display Record")
        print("\t5. Modify Record")
        print("\t6. Exit")

        choice = input("\n\tEnter your choice: ")
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
            break
        else:
            print("\n\tPlease enter 1 to 6")
            continue
        # except:
            # print("\n", choice, "is not a number")
            # continue


def admin_add():  # Add Record
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("\n\ta. Coach")
        print("\tb. Sport")
        print("\tc. Sport Schedule")
        choice = input("\n\tEnter your choice: ")

        # coach
        if choice == "a":
            coach = {}
            print("\n*** Please Fill in your information below ***\n")
            coach["Couach ID"] = input("\tCouach ID: ")
            coach["Name"] = input("\tName: ")
            coach["Date Joined"] = input("\tDate Joined: ")
            coach["Date Terminated"] = input("\tDate Terminated: ")
            coach["Horly Rate (RM/h)"] = input("\tHorly Rate (RM/h): ")
            coach["Phone"] = input("\tPhone: ")
            coach["Adress"] = input("\tAdress: ")

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

            # read coach files and write data
            with open("coach.txt", "r") as coachf:
                coach_data = coachf.read()
                coach_list = json.loads(coach_data)
                coach_list.append(coach)
                encode_coach = json.dumps(coach_list)
            with open("coach.txt", "w") as coachf:
                coachf.write(encode_coach)

            print("\n\t★★★ Complete ★★★")

        # sport
        elif choice == "b":
            sport = {}

            # read sport files and append data
            with open("sport.txt", "r") as sportf:
                sport_data = sportf.read()
                sport_list = json.loads(sport_data)

                flag = 0
                while flag == 0:
                    print("\n*** Please Fill in your information below ***\n")
                    sport_code = input("\tSport Code: ")
                    sport_name = input("\tSport Name: ")

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

            # write data into the file
            with open("sport.txt", "w") as sportf:
                sportf.write(encode_sport)

            print("\n\t★★★Complete★★★")

        # Scedule
        elif choice == "c":
            pass

        else:
            print("\nPlease Enter a, b or c")

        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def admin_display():  # Display All Records
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("\n\ta. Coach")
        print("\tb. Sport")
        print("\tc. Registered Students")
        choice = input("\n\tEnter your choice: ")

        if choice == "a":  # Coach
            with open("coach.txt") as coachf:
                coach_data = coachf.read()
                coach_list = json.loads(coach_data)

            print("\n*** Here are all records of coaches ***\n")
            for coach in coach_list:
                for coach_info in coach:
                    print("\t"+coach_info+": "+str(coach[coach_info]))
                print()

        elif choice == "b":  # Sport
            with open("sport.txt") as sportf:
                sport_data = sportf.read()
                sport_list = json.loads(sport_data)

            print("\n*** Here are all records of sports ***\n")
            for sport in sport_list:
                for sport_info in sport:
                    print("\t"+sport_info+": "+str(sport[sport_info]))
                print()

        elif choice == "c":  # Registered Students
            pass
        else:
            print("\n\tPlease Enter a, b or c")

        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def admin_search():  # Search Specific Records of
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("\n\ta. Coach by Coach ID")
        print("\tb. Coach by overall performance (Rating)")
        print("\tc. Sport by Sport ID")
        print("\td. Student by Student ID")
        choice = input("\n\tEnter your choice: ")

        # Coach by Coach ID
        if choice == "a":
            with open("coach.txt") as coachf:
                coach_data = coachf.read()
                coach_list = json.loads(coach_data)

            flag = 0
            while flag == 0:
                coach_id = input("\n\tEnter Coach ID: ")
                for coach in coach_list:
                    if coach_id == coach["Couach ID"]:
                        print()
                        for coach_info in coach:
                            print("\t", coach_info, ":", coach[coach_info])
                        flag = 1

                if flag == 0:
                    print("\n\tWe couldn't find " +
                          coach_id+", please try again.")
                if flag == 1:
                    break

        # Coach by overall performance (Rating)
        elif choice == "b":
            with open("coach.txt") as coachf:
                coach_data = coachf.read()
                coach_list = json.loads(coach_data)

            flag = 0
            while flag == 0:
                try:
                    rating = int(
                        input("\n\tEnter overall performance (Rating): "))
                    for coach in coach_list:
                        if rating == coach["Rating"]:
                            print()
                            for coach_info in coach:
                                print("\t", coach_info,
                                      ":", coach[coach_info])
                            flag = 1

                except:
                    print("\n\tPlease Enter the Number.")
                    continue

                if flag == 0:
                    print("\n\tWe couldn't find rating " +
                          str(rating)+", please try again.")
                if flag == 1:
                    break

        # Sport by Sport ID
        elif choice == "c":
            with open("sport.txt") as sportf:
                sport_data = sportf.read()
                sport_list = json.loads(sport_data)

            flag = 0
            while flag == 0:
                sport_id = input("\n\tEnter Sport ID: ")
                for sport in sport_list:
                    if sport_id == sport["Sport Code"]:
                        print()
                        for sport_info in sport:
                            print("\t", sport_info, ":", sport[sport_info])
                        flag = 1
                if flag == 0:
                    print("\n\tWe couldn't find " +
                          sport_id+", please try again.")
                if flag == 1:
                    break

        elif choice == "d":
            pass
        else:
            print("\nPlease Enter a, b or c")

        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def admin_sort():  # Sort and Display Record
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("\n\ta. Coaches in ascending order by names.")
        print("\tb. Coaches Hourly Pay Rate in ascending order")
        print("\tc. Coaches Overall Performance in ascending order")
        choice = input("\n\tEnter your choice: ")

        # Coaches in ascending order by names.
        if choice == "a":
            with open("coach.txt") as coachf:
                coach_data = coachf.read()
                coach_list = json.loads(coach_data)

            name_list = []
            for coach in coach_list:
                name_list.append(coach["Name"])

            name_sorted = sorted(name_list)

            for name in name_sorted:
                for coach in coach_list:
                    if name == coach["Name"]:
                        print()
                        for coach_info in coach:
                            print("\t", coach_info, ":", coach[coach_info])

        # Coaches Hourly Pay Rate in ascending order
        elif choice == "b":
            with open("coach.txt") as coachf:
                coach_data = coachf.read()
                coach_list = json.loads(coach_data)

            hourlyrate_list = []
            for coach in coach_list:
                hourlyrate_list.append(coach["Horly Rate (RM/h)"])

            hourlyrate_sorted = sorted(hourlyrate_list, reverse=True)

            for hourlyrate in hourlyrate_sorted:
                for coach in coach_list:
                    if hourlyrate == coach["Horly Rate (RM/h)"]:
                        print()
                        for coach_info in coach:
                            print("\t", coach_info, ":", coach[coach_info])

        # Coaches Overall Performance in ascending order
        elif choice == "c":
            with open("coach.txt") as coachf:
                coach_data = coachf.read()
                coach_list = json.loads(coach_data)

            rating_list = []
            for coach in coach_list:
                rating_list.append(coach["Rating"])

            rating_sorted = sorted(rating_list, reverse=True)

            for rating in rating_sorted:
                for coach in coach_list:
                    if rating == coach["Rating"]:
                        print()
                        for coach_info in coach:
                            print("\t", coach_info, ":", coach[coach_info])
        else:
            print("\nPlease Enter a, b or c")

        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def admin_modify():  # Modify Record
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("\n\ta. Coach")
        print("\tb. Sport")
        print("\tc. Sport Schedule")
        choice = input("\n\tEnter your choice: ")

        # Coach
        if choice == "a":
            coach_id = input("\n\tEnter Coach ID to modify: ")
            with open("coach.txt") as coachf:
                coach_data = coachf.read()
                coach_list = json.loads(coach_data)

            for coach in coach_list:
                if coach_id == coach["Couach ID"]:
                    comtinue_modify = "m"
                    while comtinue_modify == "m":
                        print("\n\t*** Which record do you want to modify***\n?")
                        print("\n\t1. Name")
                        print("\n\t2. Date Joined")
                        print("\n\t3. Date Terminated")
                        print("\n\t4. Horly Rate (RM/h)")
                        print("\n\t5. Phone")
                        print("\n\t6. Adress")
                        print("\n\t7. Sport Center")
                        print("\n\t8. Sport")
                        num = input("\n\tEnter your choice: ")
                        try:
                            num = int(num)
                            if num == 1:
                                coach["Name"] = input("Please Enter Name: ")
                            elif num == 2:
                                coach["Date Joined"] = input(
                                    "Please Enter Date Joined: ")
                            elif num == 3:
                                coach["Date Terminated"] = input(
                                    "Please Enter Date Terminated: ")
                            elif num == 4:
                                try:
                                    coach["Horly Rate (RM/h)"] = int(input(
                                        "Please Enter Horly Rate (RM/h): "))
                                except:
                                    print("Please Enter the number")
                            elif num == 5:
                                coach["Phone"] = input("Please Enter Phone: ")
                            elif num == 6:
                                coach["Adress"] = input(
                                    "Please Enter Adress: ")
                            elif num == 7:
                                # Check Sport center code in this system
                                flag = 0
                                while flag == 0:
                                    sport_center_code = input(
                                        "Please Enter Sport Center Code: ")
                                    with open("sport_center.txt") as sportcenterf:
                                        sportcenter_data = sportcenterf.read()
                                        sportcenter_list = json.loads(
                                            sportcenter_data)

                                    for sportcenter in sportcenter_list:
                                        if sportcenter["Sport Center Code"] == sport_center_code:
                                            coach["Sport Center Code"] = sport_center_code
                                            coach["Sport Center Name"] = sportcenter["Sport Center Name"]
                                            flag = 1
                                            break

                                    if flag == 1:
                                        break
                                    print("There is no",
                                          sport_center_code, "in this system")

                            elif num == 8:
                                # Check sport code in this system
                                flag = 0
                                while flag == 0:
                                    sport_code = input(
                                        "Please Enter Sport Code: ")
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
                                    print("There is no", sport_code,
                                          "in this system")
                        except:
                            print("Wrong Input")

                        comtinue_modify = input(
                            "\n\tEnter \'y\' to continue to modify: ")
                else:
                    print("\n\tThere is no " + coach_id + " in this sysmtem")

        elif choice == "b":
            pass
        elif choice == "c":
            pass
        else:
            print("\nPlease Enter a, b or c")

        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break
