class Admin:
    def __init__(self, admin_username, admin_password):
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.admin = {'yurikogoto': 'TP028457209'}


class Login_System(Admin):
    def __init__(self, admin_username, admin_password):
        super().__init__(admin_username, admin_password)

    def login_valid(self):
        if self.admin_username in self.admin:
            print("\nConguratulation\n")
        else:
            print("\nIncorrect username or password\n")


print("***** Welcome to Admin System ***** \n")

print("*** LOG IN ***")
print("Enter username and password")
username = input("User Name：")  # user name is 'yurikogoto'
password = input("Password：")  # password is 'TP028457209'
login = Login_System(username, password)
login.login_valid()
