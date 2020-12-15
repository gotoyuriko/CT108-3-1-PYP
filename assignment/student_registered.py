def student_login():
    pass


def registered_student():
    while True:
        print("\n*** Student login successful ***\n")
        print("\t1. View details of...")
        print("\t2. Modify Self Record")
        print("\t3. Provide feedback and Star to Coach.")
        print("\t4. Exit")

        choice = input("\nEnter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                print("\nLog Out\n")
                break
            else:
                print("\nPlease enter 1 to 4")
                continue
        except:
            print("\n", choice, "is not a number")
            continue
