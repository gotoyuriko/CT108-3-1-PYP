#Array Example

print("Enter 5 values:")
count = 0
val = []
while count < 5:
  num = int(input())
  val.append(num)
  count+=1


print("\nThe values entered are:")
count = 0
while count < 5:
  print(val[count])
  count+=1