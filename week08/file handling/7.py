print("Enter your details here:\n")

student_name = input("Name: ")
student_id = input("Student ID: ")
student_email = input("Enail Address: ")

f = open("students.txt", "a")
f.write("\n"+student_name+","+student_id+","+student_email)
f.close()

print("\nRefistration Successful!!")
