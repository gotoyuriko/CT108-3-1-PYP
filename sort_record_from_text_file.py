std_file = open("students.txt", "r") #reading the contents in students.txt file
std_records = std_file.readlines() #readlines() return all lines in the file, as a list where each line is an item in the list object
print("Not sorted:")
record = 0
for std_record in std_records:
   print("[",(record+1),"]",std_record.strip()) #printing each line from text file
   record+=1

new_list = []

while std_records:
   minimum = std_records[0]
   for x in std_records:
      if x < minimum:
         minimum = x
   new_list.append(minimum)
   std_records.remove(minimum)

print()
print("Sorted:")
record = 0
for std_record in new_list:
   print("[",(record+1),"]",std_record.strip()) #printing each line from text file
   record+=1

