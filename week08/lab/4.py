'''
Write a program that will process the weekly employee time cards for all the employees of an
organisation. Each employee time card will have three data items: an employee number, an hourly wage rate and the number of hours worked during a given week. Each employee is to be paid 5% higher from their hourly wage rate for all hours worked over 35. Calculate the gross salary in a function called calc_gross_salary(). A tax amount of 15% of gross salary is to be deducted. At the end of the run, display the total payroll amount and the average amount paid for each employee.
'''


def calc_gross_salary(wage, hours):
    if hours > 35:
        gross_salary = (wage*35)+((wage * 1.05) * (hours-35))
    else:
        gross_salary = wage * hours
    return gross_salary


choice = "y"
count = 0
total_payroll_amount = 0
while choice == "y":
    try:
        employee_num = int(input("\nEnter employee number: "))
        hourly_wage_rate = int(input("Hourly wage rate: "))
        weekly_wroking_hours = int(input("Weekly working hours: "))

        gross_salary = calc_gross_salary(
            hourly_wage_rate, weekly_wroking_hours)

        print("Net Salary: {:.2f}".format(gross_salary*0.85))

        total_payroll_amount = total_payroll_amount+(gross_salary * 0.85)
        count += 1
        choice = input("\nEnter 'y' to proceed: ")

    except:
        print("Wrong input!")

print("\nTotal Payroll:{:.2f}".format(total_payroll_amount))
print("Average Salary:{:.2f}".format(total_payroll_amount/count))
