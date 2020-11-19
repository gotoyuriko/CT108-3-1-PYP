print("Enter ‘n’ to stop or to any letter to continue")
choice = input()

while choice!="n":
    print("Enter your age in year and month")
    year = int(input("Year: "))
    month = int(input("Month: "))

    month = month + (year * 12)

    if month>500:
        remarks = "***"
    else:
        remarks = ""

    

    print("Your age in month: ", str(month),remarks)

    print("Enter ‘n’ to stop or to any letter to continue")
    choice = input()
    print("**********************************")
    
