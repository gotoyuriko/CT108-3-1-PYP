import file_handle as f


def admin_login():  # Login to Access System.
    continuey = "y"
    while continuey == "y":
        print("\n*** Admin Log In ***\n\tEnter username and password")
        admin_username = input("\tUser Name：")
        admin_password = input("\tPassword：")
        admin_dict = f.admin_login_read()
        if admin_username in admin_dict and admin_dict[admin_username] == admin_password:
            return True
        else:
            print("\n\tIncorrect username or password")
        continuey = input(
            "\n\tEnter 'y' to type username and password again: ")


def admin_add():  # Add Record
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("\n\ta. Coach\n\tb. Sport\n\tc. Sport Schedule")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            admin_add_a()
        elif choice == "b":
            admin_add_b()
        # Scedule
        elif choice == "c":
            admin_add_c()
        else:
            print("\n\tPlease Enter a, b or c")
        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def admin_add_a():
    coach = {}
    print("\n*** Add Records of Coach ***")
    print("\n\tPlease Fill in your information below")
    coach["Couach ID"] = input("\n\tCouach ID: ")
    coach["Name"] = input("\tName: ")
    coach["Date Joined"] = input("\tDate Joined: ")
    coach["Date Terminated"] = input("\tDate Terminated: ")
    while 1:
        try:
            coach["Horly Rate (RM/h)"] = int(input("\tHorly Rate (RM/h): "))
            break
        except:
            print("\tPlease Enter the number")
    coach["Phone"] = input("\tPhone: ")
    coach["Adress"] = input("\tAdress: ")

    # Check whether the input of Sport center code exits or not
    check_sport_center_code(coach)

    # Check whether the input of sport code exits or not
    check_sport_code(coach)

    # read coach files
    coach_list = f.coach_read()
    coach_list.append(coach)

    # write on coach files
    f.coach_write(coach_list)

    # print coach
    print("\n\t★★★ Complete ★★★\n")
    print_records(coach)


def admin_add_b():
    sport = {}
    # read sport files
    sport_list = f.sport_read()
    while 1:
        print("\n*** Add Records of Sport ***")
        print("\n\tPlease Fill in your information below")
        sport_code = input("\tSport Code: ")
        sport_name = input("\tSport Name: ")

        # Check if the sport.txt already had input or not
        if sport_code_check2(sport_list, sport_code, sport_name):
            continue
        else:
            sport["Sport Code"] = sport_code
            sport["Sport Name"] = sport_name
            break

    sport_list.append(sport)

    # write data into the file
    f.sport_write(sport_list)

    # print coach
    print("\n\t★★★ Complete ★★★\n")
    print_records(sport)


def admin_add_c():
    pass


def admin_display():  # Display All Records
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("\n\ta. Coach\n\tb. Sport\n\tc. Registered Students")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            admin_display_a()
        elif choice == "b":
            admin_display_b()
        elif choice == "c":  # Registered Students
            pass
        else:
            print("\n\tPlease Enter a, b or c")
        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def admin_display_a():
    coach_list = f.coach_read()

    print("\n*** Here are all records of coache ***\n")
    for coach in coach_list:
        print_records(coach)


def admin_display_b():
    sport_list = f.sport_read()

    print("\n*** Here are all records of sport ***\n")
    for sport in sport_list:
        print_records(sport)


def admin_display_c():
    pass


def admin_search():  # Search Specific Records of
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("\n\ta. Coach by Coach ID\n\tb. Coach by overall performance (Rating)\n\tc. Sport by Sport ID\n\td. Student by Student ID")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            admin_search_a()
        elif choice == "b":
            admin_search_b()
        elif choice == "c":
            admin_search_c()
        elif choice == "d":
            admin_search_d()
        else:
            print("\n\tPlease Enter a, b or c")
        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def admin_search_a():
    coach_list = f.coach_read()
    while 1:
        coach_id = input("\n\tEnter Coach ID: ")
        if search_print(coach_list, coach_id):
            break


def admin_search_b():
    coach_list = f.coach_read()
    while 1:
        try:
            rating = int(input("\n\tEnter overall performance (Rating): "))
            if search_print(coach_list, rating):
                break
        except:
            print("\n\tPlease Enter the Number.")
            continue


def admin_search_c():
    sport_list = f.sport_read()
    while 1:
        sport_id = input("\n\tEnter Sport ID: ")
        if search_print(sport_list, sport_id):
            break


def admin_search_d():
    pass


def admin_sort():  # Sort and Display Record
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("\n\ta. Coaches in ascending order by names.\n\tb. Coaches Hourly Pay Rate in ascending order\n\tc. Coaches Overall Performance in ascending order")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            admin_sort_a()
        elif choice == "b":
            admin_sort_b()
        elif choice == "c":
            admin_sort_c()
        else:
            print("\nPlease Enter a, b or c")
        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def admin_sort_a():
    coach_list = f.coach_read()
    name_list = []
    for coach in coach_list:
        name_list.append(coach["Name"])

    name_sorted = sorted(name_list)

    for name in name_sorted:
        for coach in coach_list:
            if name == coach["Name"]:
                print_records(coach)


def admin_sort_b():
    coach_list = f.coach_read()

    hourlyrate_list = []
    for coach in coach_list:
        hourlyrate_list.append(coach["Horly Rate (RM/h)"])

    hourlyrate_sorted = sorted(hourlyrate_list, reverse=True)

    for hourlyrate in hourlyrate_sorted:
        for coach in coach_list:
            if hourlyrate == coach["Horly Rate (RM/h)"]:
                print_records(coach)


def admin_sort_c():
    coach_list = f.coach_read()

    rating_list = []
    for coach in coach_list:
        rating_list.append(coach["Rating"])

    rating_sorted = sorted(rating_list, reverse=True)

    for rating in rating_sorted:
        for coach in coach_list:
            if rating == coach["Rating"]:
                print_records(coach)


def admin_modify():  # Modify Record
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("\n\ta. Coach\n\tb. Sport\n\tc. Sport Schedule")
        choice = input("\n\tEnter your choice: ")
        # Coach
        if choice == "a":
            admin_modify_a()

        # Sport
        elif choice == "b":
            admin_modify_b()

        # Sport Schedule
        elif choice == "c":
            pass
        else:
            print("\nPlease Enter a, b or c")

        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def admin_modify_a():
    # read coach files
    coach_list = f.coach_read()

    while 1:
        coach_id = input("\n\tEnter Coach ID to modify: ")
        # check coach id
        for coach in coach_list:
            if coach_id == coach["Couach ID"]:
                continue_modify = "m"
                while continue_modify == "m":
                    print("\n*** Which record do you want to modify?***\n")
                    print("\t1. Name\n\t2. Date Joined\n\t3. Date Terminated\n\t4. Horly Rate (RM/h)\n\t5. Phone\n\t6. Adress\n\t7. Sport Center\n\t8. Sport")
                    num = input("\n\tEnter your choice: ")
                    try:
                        num = int(num)
                        if num == 1:
                            coach["Name"] = input("\n\tPlease Enter Name: ")
                        elif num == 2:
                            coach["Date Joined"] = input(
                                "\n\tPlease Enter Date Joined: ")
                        elif num == 3:
                            coach["Date Terminated"] = input(
                                "\n\tPlease Enter Date Terminated: ")
                        elif num == 4:
                            try:
                                coach["Horly Rate (RM/h)"] = int(
                                    input("\n\tPlease Enter Horly Rate (RM/h): "))
                            except:
                                print("\n\tPlease Enter the number")
                        elif num == 5:
                            coach["Phone"] = input("\n\tPlease Enter Phone: ")
                        elif num == 6:
                            coach["Adress"] = input(
                                "\n\tPlease Enter Adress: ")
                        elif num == 7:
                            # Check Sport center code in this system
                            check_sport_center_code(coach)
                        elif num == 8:
                            # Check sport code in this system
                            check_sport_code(coach)
                    except:
                        print("\n\tWrong Input")

                continue_modify = input(
                    "\n\tEnter \'m\' to continue to modify: ")

                if continue_modify != "m":
                    f.coach_txt_write(coach_list)
                    print("\n\t★★★Complete★★★")
                    print_records(coach)
                    return

        print("\n\tThere is no " + coach_id + " in this sysmtem")


def admin_modify_b():
    while 1:
        sport_id = input("\n\tEnter Sport ID to modify: ")
        sport_list = f.sport_txt_read()
        for sport in sport_list:
            # check coach id
            if sport_id == sport["Sport Code"]:
                sport["Sport Name"] = input("\n\tPlease Enter Sport Name: ")
                f.sport_txt_write(sport_list)
                print("\n\t★★★Complete★★★")
                print_records(sport)

        print("\n\tThere is no " + sport_id + " in this sysmtem")


def print_records(dict_items):
    for dict_key in dict_items:
        print("\t"+str(dict_key)+": "+str(dict_items[dict_key]))
    print()


def check_sport_center_code(coach):
    while 1:
        sport_center_code = input("\tSport Center Code: ")
        sport_center_list = f.sport_center_read()
        for sportcenter in sport_center_list:
            if sportcenter["Sport Center Code"] == sport_center_code:
                coach["Sport Center Code"] = sport_center_code
                coach["Sport Center Name"] = sportcenter["Sport Center Name"]
                return

        print("\n\tThere is no", sport_center_code, "in this system\n")


def check_sport_code(coach):
    while 1:
        sport_code = input("\tSport Code: ")
        sport_list = f.sport_read()
        for sport in sport_list:
            if sport["Sport Code"] == sport_code:
                coach["Sport Code"] = sport_code
                coach["Sport Name"] = sport["Sport Name"]
                return

        print("\n\tThere is no", sport_code, "in this system\n")


def sport_code_check2(sport_list, sport_code, sport_name):
    for sport in sport_list:
        if sport["Sport Code"] == sport_code or sport["Sport Name"] == sport_name:
            print("\n\t", sport_code, "or",
                  sport_name, "are already stored")
            return True

    return False


def search_print(list, search_key):
    for dict in list:
        if search_key == dict["Couach ID"]:
            print("\t*** Here are the results ***\n")
            print_records(dict)
            return True
    print("\n\tWe couldn't find " + search_key + ", please try again.")
    return False
