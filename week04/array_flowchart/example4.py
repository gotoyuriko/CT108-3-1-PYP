#Read input into 2D Array Example
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of colums:"))

#Initialize 2D Array
num = []
print("Enter the entries row-wise:")

#For User Input
for r in range(row):      #A for loop for row entities
  val = []
  for c in range(col):      #A for loop for column entries
    val.append(int(input))
  num.append(val)

print("\n**************************************")
print("\nThe values entered are:")

#For printing the 2D Array

for r in range(row):
  for c in range(col):
    print(num[r][c], end = " ")
  print()