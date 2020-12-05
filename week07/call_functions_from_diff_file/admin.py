def admin_function():
  print("\nAdmin Login")
  print("===================\n")
  admin_uname = input("Username: ")
  admin_pwd = input("Password: ")

  if admin_uname=="a" and admin_pwd=="p":
    print("\nWelcome Admin!")
    print("===================")
    print("\n1. Add Record")
    print("2. Display All Record")
    print("3. Search Specific Record")
    print("4. Sort and Display Record")
    print("5. Modify Record")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))      
    
  else:
    print("\nWrong credentials!")
