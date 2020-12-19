'''
As a form of quality control, the Pancake Kitchen has recorded, on “pancakes.txt’, two measurements for each of its pancakes made in a certain month: the thickness in mm (millimetres) and the diameter in cm (centimetres). Each record on the file contains the two measurements for a pancake, thickness followed by diameter. Write a program that will read “pancakes.txt”, calculate the total record in file and average of both thickness and parameter. Print these values at the end of the program.
'''
count = 0
total_thickness = 0
total_diameter = 0

with open("pancakes.txt", "r") as pancakef:
    for p in pancakef:
        number = p.strip('\n')
        value = number.split(",")
        print("Thickness: ", value[0], "\tParameters: ", value[1])

        total_thickness += float(value[0])
        total_diameter += float(value[1])

        count += 1

print("Total pancakes: ", count)
print("Average thickness: ", total_thickness/count)
print("Average parameter: ", total_diameter/count)
