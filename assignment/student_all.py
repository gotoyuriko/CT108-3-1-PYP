import file_handle as f
import admin as a


def view_details():
    continuey = "y"
    while continuey == "y":
        print("====================================================\n\n\t*** View Datail of ***\n\ta. Coach\n\tb. Sport\n\tc. Sport Schedule")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            view_details_a()
        elif choice == "b":
            view_details_b()
        else:
            print("\n\tPlease Enter a or b")
        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def view_details_a():
    print("\n*** View Detail of Sport ***\n\n\t")


def view_details_b():
    print("\n*** View Detail of Sport Schedule ***\n\n\t")


def student_signup():
    student = {}
    print("\n*** Student Sign Up ***")
    student["Student ID"] = input("\n\tEnter your email: ")
    student["Password"] = input("\n\tEnter your password: ")
    student["Name"] = input("\n\tEnter your name: ")
    student_list = f.student_read()
    student_list.append(student)
    f.student_write(student_list)

    print("\n\t★★★ Complete ★★★\n")
    a.print_records(student)
