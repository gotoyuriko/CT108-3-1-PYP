#2D Array Example

num = ([8,55,46],[7,12,14])

#using while loop
print("Using while loop")
row = 0
col = 0
while row < 2:
  while col < 3:
    print(num[row][col], end = " ")
    col += 1
  col = 0
  row+=1
  print("")

print("***************************************")

#using for loop
print("Using for loop")
for r in range(2):
  for c in range(3):
    print(num[r][c],end = " ")
  print()