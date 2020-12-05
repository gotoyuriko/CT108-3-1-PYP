'''
Number of days spent in the hospital: 30
Medication charges: 100
Surgical charges: 100
Lab fees: 100
Physical rehabilitation charges: 100
Claim insurance? 0 = yes, 1 = no: 0
Hospital staff? 0 = yes, 1 = no: 1
Total charges: 0.00
'''
days = input("Number of days spent in the hospital:")
medication = input("Medication charges: ")
surgical = input("Surgical charges: ")
lab = input("Lab fees: ")
rehab = input("Physical rehabilitation charges: ")
insurance = input("Claim insurance? 0 = yes, 1 = no: ")
staff = input("Hospital staff? 0 = yes, 1 = no: ")

try:
    if int(days) >= 30:
        discount = 0.2
    else:
        discount = 0
    if staff == 0:
        lab = 0
        rehab = 0
    elif staff == 1:
        pass
    else:
        print("Please enter hospital staff 0 = yes, 1 = no")

    total_charge = int(days) * 350 + float(surgical) + \
        float(lab) + float(rehab)
    total_charge = total_charge * (total_charge * discount)

    if insurance == 0:
        total_charge = 0
    elif insurance == 1:
        pass
    else:
        print("Please enter Hospital staff 0 = yes, 1 = no")

    print("Total charges:", total_charge)
except:
    print("Make sure you enter the number")
