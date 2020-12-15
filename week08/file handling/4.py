student_file = open("students.txt")
for student_record in student_file:
    student_record = student_record.replace(" ", "")
    if not "TP830830" in student_record:
        continue
    print(student_record)
