student_file = open("students.txt")
for student_record in student_file:
    if student_record.startswith("David"):
        student_record = student_record.replace(" ", "")
        continue
    print(student_record)
