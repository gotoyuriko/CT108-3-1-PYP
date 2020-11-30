shipping_charges = [2.99, 5.99, 10.99, 15.99]

print("Enter Zone:")
zone = int(input())

print("Enter Weight:")
weight = int(input())

i = 0
while i < 4:
    if (zone == (i+1)):
        t = weight * shipping_charges[i]
    i += 1

print("Total charges: ", str("%.2f"))
