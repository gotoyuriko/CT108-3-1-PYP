new_list = [3, 4, 5, 6]
for item in new_list:
    print("for loop:", item)
print()

for i in range(len(new_list)):
    print("for loop with range:", new_list[i])
print()

j = 0
while j < len(new_list):
    print("while loop", new_list[j])
    j += 1
print()

# search for an element
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in new_list:
    if item == 10:
        print("Search Element", item)
print()

# list
new_list = ["John", "Marry", "Cat", "Dog"]
name = input("Enter a name to search for: ")
for item in new_list:
    if name in item:
        print(name)
