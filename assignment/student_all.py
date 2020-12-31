import file_handle as f


def view_details():
    continuey = "y"
    while continuey == "y":
        print("====================================================")
        print("*** View Datail of ***\n\ta. Coach\n\tb. Sport\n\tc. Sport Schedule")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            view_sport()
        elif choice == "b":
            view_schedule()
        else:
            print("\n\tPlease Enter a, b or c")
        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def student_signup():
    pass


def student_registered():
    pass


def view_sport():
    pass


def view_schedule():
    pass
