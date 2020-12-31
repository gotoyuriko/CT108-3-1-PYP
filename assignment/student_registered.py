import file_handle as f


def student_login():
    continuey = "y"
    while continuey == "y":
        print("\n*** Student Log In ***\n\tEnter your email and password")
        student_username = input("Email：")
        student_password = input("Password：")
        student_list = f.student_read()
        for student in student_list:
            if student_username == student["Student ID"] and student_password == student["Password"]:
                return True
        print("\nIncorrect username or password\n")
        continuey = input(
            "\n\tEnter 'y' to type username and password again: ")


def view_detail_of():
    pass


def modify_selfrecord():
    pass


def feedback_star():
    pass
