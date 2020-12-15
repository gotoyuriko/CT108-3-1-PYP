student_file = open("students.txt")
print(student_file)
count = 0
for student_record in student_file:
    count += 1
    if student_record.startswith("Mary"):
        # student_record = student_record.lstrip()
        student_record = student_record.replace(" ", "")
        print(student_record)
print("Total acount", count)
