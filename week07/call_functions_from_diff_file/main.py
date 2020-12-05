from admin import *
from student import *

print("Welcome to Sport Academy System")
print("====================================\n")
print("Who are you?")
print("1. Admin")
print("2. Student\n")

choice = int(input("Enter your choice: "))

if choice == 1:
   admin_function()
else:
   student_function()
