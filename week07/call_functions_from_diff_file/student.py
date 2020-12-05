from register_student import *

def student_function():
  print("\nStudent Menu:")
  print("\n1. Login")
  print("2. View Sports Details")
  print("3. View Sports Schedule")
  print("4. Register as member")
  print("5. Exit")

  choice = int(input("\nPlease enter your choice: "))

  if choice == 1:
    print("Login")
  elif choice == 2:
    print("Sports Details")
  elif choice == 3:
    print("Sports Schedule")
  elif choice == 4:
    student_registration()
  elif choice == 5:
    exit()
