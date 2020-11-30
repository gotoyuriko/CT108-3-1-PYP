print("Applicant qualified? [Enter 1 for Yes OR 0 for No]")
qualification = int(input())

print("Enter years of experience")
experience = int(input())

print("Enter age")
age = int(input())

decision=""

if qualification==1 and experience>5 and age>30:
    decision = "Call for interview"

if qualification==1 and experience>5 and age<=30:
    decision = "Call for interview"

if qualification==1 and experience<=5 and age>30:
    decision = "Keep in file"

if qualification==1 and experience<=5 and age<=30:
    decision = "Keep in file"

if qualification==0 and experience>5 and age>30:
    decision = "Call for interview"

if qualification==0 and experience>5 and age<=30:
    decision = "Keep in file"

if qualification==0 and experience<=5 and age>30:
    decision = "Reject application"

if qualification==0 and experience<=5 and age<=30:
    decision = "Reject application"

print("Action:",decision)
