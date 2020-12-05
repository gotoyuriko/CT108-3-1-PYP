def student_registration():
   print("Enter your details here:\n")

   student_name = input("Name: ")
   student_id = input("Student ID: ")
   student_email = input("Email Address: ")
   student_password = input("Password: ")

   f = open("students.txt", "a")
   f.write("\n"+student_name+","+student_id+","+student_email+","+student_password)
   f.close()

