import file_handle as f
import student_all as st_a


def student_login():
    continuey = "y"
    while continuey == "y":
        print("\n*** Student Log In ***\n\n\tEnter your email and password")
        student_username = input("\tEmail：")
        student_password = input("\tPassword：")
        student_list = f.student_read()
        for student in student_list:
            if student_username == student["Student ID"] and student_password == student["Password"]:
                student_id = student["Student ID"]
                return True, student_id  # login sccessgul with your student ID
        print("\n\tIncorrect username or password\n")
        continuey = input(
            "\n\tEnter 'y' to type username and password again: ")


def view_details(id):
    continuey = "y"
    while continuey == "y":
        print("====================================================\n\n\t*** View Datail of ***\n\ta. Coach\n\tb. Self-Record\n\tc. Registered Sport Schedule")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            view_details_a()
        elif choice == "b":
            view_details_b(id)
        elif choice == "c":
            view_details_c(id)
        else:
            print("\n\tPlease Enter a or b")
        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def view_details_a():
    print("\n*** View Detail of Coach ***\n")
    coach_list = f.coach_read()
    for coach in coach_list:
        print("\tCoach: "+str(coach["Name"]))
        print("\tSport Center: "+str(coach["Sport Center Name"]))
        print("\tSport: "+str(coach["Sport Name"]))
        print("\tSport Fees: "+str(coach["Horly Rate (RM/h)"]) + "(RM/h)")
        print("\tOverall performance (Rating): "+str(coach["Rating"]))
        print()


def view_details_b(student_id):
    print("\n*** View Detail of Self-Record ***\n")
    read_selfrecord(student_id)


def view_details_c(student_id):
    coach_id = ""
    coach_name = ""
    student_list = f.student_read()
    for student in student_list:
        if student["Student ID"] == student_id:
            coach_id = student["Coach ID"]

    coach_list = f.coach_read()
    for coach in coach_list:
        coach_name = coach["Name"]

    schedule_list = f.schedule_read()
    print("\n\t*** The schedule of your Coach 【"+coach_name+"】is Below ***\n")
    for schedule in schedule_list:
        if schedule["Coach ID"] == coach_id:
            print("\tDate: "+str(schedule["Date"]))
            print("\tStart Time: "+str(schedule["Start Time"]))
            print("\tEnd Time: "+str(schedule["End Time"]))
            print()


def modify_selfrecord(student_id):
    print("\n*** Modify Records of Self-Record ***")
    student_list = f.student_read()
    for student in student_list:
        if student["Student ID"] == student_id:
            while 1:
                continue_modify = "m"
                while continue_modify == "m":
                    print("\n\tWhich record do you want to modify?")
                    print("\t1. Student ID")
                    print("\t2. Password")
                    print("\t3. Your Name")
                    print("\t4. Select Coach")
                    num = input("\n\tEnter your choice: ")
                    modify_coach(num, student)
                    continue_modify = input(
                        "\n\tEnter \'m\' to continue to modify: ")

                    if continue_modify != "m":
                        f.student_write(student_list)
                        for student in student_list:
                            if student["Student ID"] == student_id:
                                print("\n\t★★★Complete★★★\n")
                                read_selfrecord(student_id)
                                return


def feedback_star(student_id):
    coach_id = ""
    student_list = f.student_read()
    for student in student_list:
        if student["Student ID"] == student_id:
            coach_id = student["Coach ID"]
    print("\n*** Please give us your feedback on your coach【"+coach_id+"】***\n")
    print("1: \"very poor performance\" * * * 5: \"excellent performance\"")
    rating = input("\tEnter the number")
    while 1:
        try:
            coach_list = f.coach_read()
            for coach in coach_list:
                if coach["Coach ID"] == coach_id:
                    old_rating = coach["Rating"]
                    old_rating += rating
                    print("*** Thank you !! ***")
                    return
        except:
            print("wrong input")


def modify_coach(num, student):
    try:
        num = int(num)
        if num == 1:
            student["Student ID"] = input(
                "\n\tPlease Enter your email: ")
            return
        elif num == 2:
            old_passowrd = input(
                "\n\tPlease Enter the current Password: ")
            student_list = f.student_read()
            for student in student_list:
                if old_passowrd == student["Password"]:
                    student["Password"] = input(
                        "\n\tPlease Enter the new Password: ")
                    return
            print("\n\tIncorrect Password")
            return
        elif num == 3:
            student["Name"] = input("\n\tPlease Enter your name: ")
            return
        elif num == 4:
            st_a.select_coach(student)
            return
    except:
        print("\n\tWrong Input")


def read_selfrecord(student_id):
    student_list = f.student_read()
    for student in student_list:
        if student["Student ID"] == student_id:
            print("\tYour Email: "+student["Student ID"])
            print("\tYour Name: "+student["Name"])
            coach_list = f.coach_read()
            for coach in coach_list:
                if coach["Coach ID"] == student["Coach ID"]:
                    print("\tCoach Name: "+coach["Name"])
                    print("\tSport Center: " + coach["Sport Center Name"])
                    print("\tSport: "+coach["Sport Name"])
                    print("\tSport Fees: " +
                          str(coach["Horly Rate (RM/h)"])+"(RM/h)")
