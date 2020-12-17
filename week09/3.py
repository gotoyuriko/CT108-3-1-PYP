# add / replace value of an element
new_list = [3, 4, 5, 6]
new_list.append(3)
print(new_list)
new_list[3] = 145
print(new_list)
print()


# list do not need to be unique
mylist = [3, 4, 5, 6]
print(mylist)
mylist.append("hello")
print(mylist)
mylist.append(123)
print(mylist)
mylist[3] = 345
print(mylist)
mylist[2] = "hi"
print(mylist)
mylist.insert(2, 88)  # (index, value)
print(mylist)
print()

# can ahve another list as an element
mylist2 = [1, 24, 45]
mylist[2] = mylist2
print(mylist)
mylist.append(mylist2)
print(mylist)
print()

# to combine elements using extend()
combine = [3, 4, 5, 6]
combine2 = [1, 24, 45]
combine.extend(new_list)
print(combine)
print()

a_list = [1, 2, 3, 4]
b_list = [5, 6, 7, 8]
for i in range(0, len(b_list)):
    a_list.append(b_list[i])
print(a_list)
print()

# remove specified items
remove_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove_list.remove(4)
print("remove specified items:", remove_list)
print()

# remove index
remove_list.pop(3)
print("remove index:", remove_list)
# if no idnex specified, it'll remove the last index
remove_list.pop()
print("remove index:", remove_list)
print()

# del keyword also removes specified idnex
del remove_list[5]
print("del keyword:", remove_list)
# if no idnex specified, it'll delete list entirely
del remove_list[0]
print("del keyword:", remove_list)
print()

# slice list
slice_list = [1, 2, 3, 4, 5, 6]
print("slice_list[0:3]:", slice_list[0:3])
print("slice_list[:4]:", slice_list[:4])
print("slice_list[2:]:", slice_list[2:])
print("slice_list[:]", slice_list[:])
print()
