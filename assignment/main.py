import admin as ad
import student_all as st_a
import student_registered as st_r

print("\n*** Welcome to REAL CHAMPION APORT ACADEMY! ***\n")
print("\tWho are you?\n\t1. Admin\n\t2. All Students(Registered / Not-Registered)\n\t3. Registered Student")


# try:
user = int(input("\n\tEnter the number: "))
if(user == 1):
    if ad.admin_login():
        while 1:
            print("\n*** Admin Menu ***\n")
            print("\t1. Add Record\n\t2. Display All Records\n\t3. Search Specific Record\n\t4. Sort and Display Record\n\t5. Modify Record\n\t6. Exit")
            choice = input("\n\tEnter your choice: ")
            # try:
            choice = int(choice)
            if choice == 1:
                ad.admin_add()
            elif choice == 2:
                ad.admin_display()
            elif choice == 3:
                ad.admin_search()
            elif choice == 4:
                ad.admin_sort()
            elif choice == 5:
                ad.admin_modify()
            elif choice == 6:
                print("\n*** Log Out ***")
                break
            else:
                print("\n\tPlease enter 1 to 6")
                continue
            # except:
                # print("\n\t", choice, "is not a number")
                # continue
elif(user == 2):
    st_a.student_all()
elif(user == 3):
    st_r.student_login()
else:
    print("\nPlease enter 1 ,2 or 3\n")

print("\n★★★ See You ★★★\n")
