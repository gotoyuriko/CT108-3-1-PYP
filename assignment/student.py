student = {}
with open("admin_login.txt") as f:
    for line in f:
        (key, val) = line.split()
        student[key] = val


def student():
    pass


def student_login():
    print("\n*** Admin Log In ***\n")
    print("Enter username and password")
    admin_username = input("User Name：")  # user name is 'yurikogoto34'
    admin_password = input("Password：")  # password is 'TP38121'
    if admin_username in student and student[admin_username] == admin_password:
        admin_function()
    else:
        print("\nIncorrect username or password\n")
