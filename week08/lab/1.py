import math


def volume(radius):
    pie = 3.1415
    v = 4 * math.pi * pie*float(radius)**3/3
    return v


def main(radius):
    print("Volume: {:.2f}".format(volume(radius)))


choice = "y"
while choice == "y":
    radius = input("\nRadius value: ")
    main(radius)
    choice = input("Enter 'y' to proceed: ")
