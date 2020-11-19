#Read input into 2D Array Example
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of colums:"))

#Initialize 2D Array
num = []
print("Enter the entries row-wise:")

#For User Input
r = 0
c = 0
while r < row:      #A while loop for row entities
  val = []
  while c < col:      #A while loop for column entries
    val.append(int(input))
    c+=1
  num.append(val)
  c=0
  r+=1

print("\n**************************************")
print("\nThe values entered are:")

#For printing the 2D Array
r = 0
c = 0
while r < row:
  while c < col:
    print(num[r][c], end = " ")
    c+=1
  c=0
  r+=1
  print("")