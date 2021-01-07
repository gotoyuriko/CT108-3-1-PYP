import datetime as d
while 1:
    try:
        joined_year = int(input("\tDate Joined (Year): "))
        joined_month = int(input("\tDate Joined (Month): "))
        joined_day = int(input("\tDate Joined (Day): "))
        terminated_year = int(input("\tDate Terminated (Year): "))
        terminated_month = int(input("\tDate Terminated (Month): "))
        terminated_day = int(input("\tDate Terminated (Day): "))

        date_joined = d.date(joined_year, joined_month, joined_day)
        date_terminated = d.date(
            terminated_year, terminated_month, terminated_day)

        print(date_joined)
        print(date_terminated)
        if date_joined < date_terminated:
            coach["Date Joined"] = d.datetime.strptime(
                str(date_joined), '%Y-%m-%d').strftime('%Y/%m/%d')
            coach["Date Terminated"] = d.datetime.strptime(
                str(date_terminated), '%Y-%m-%d').strftime('%Y/%m/%d')
        else:
            print("\n\tYour Date is not correct. Pleaset try again.")
            continue

    except:
        print("\n\tWrong Input. Please try again.")
        continue
