'''
Code Destination
-----------------------------
1 Melaka
2 Kuala Terengganu
3 Penang
Destination Code: 1
Age: 20
Discounted ticket price: 10.68
Type 'y' to proceed: y
Code Destination
-----------------------------
1 Melaka
2 Kuala Terengganu
3 Penang
Destination Code: 4
Age: 55
Destination not available
Discounted ticket price: 0.00
Type 'y' to proceed: y
Code Destination
-----------------------------
1 Melaka
2 Kuala Terengganu
3 Penang
Destination Code: 3
Age: x
Wrong Code/ Age input
Type 'y' to proceed: n
'''
print("Code Destination")
print("-----------------------------")
print("1 Melaka")
print("2 Kuala Terengganu")
print("3 Penang")
code = input("Destination Code: ")
age = input("Age: ")
price = 0
choice = "y"

while choice == "y":
    try:
        if code == 1:
            price = 35.60
        elif code == 2:
            price = 55.90
        elif code == 3:
            price = 47.80
        else:
            print("Please Enter code 1 to 3")
            continue

        if age <= 19:
            discout_price = price * 0.5
        else:
            discout_price = price * 0.7

        print("Discounted ticket price: ", discout_price)
    except:
        print("Code/age should be number")
        continue
    choice = input("Type 'y' to proceed: ")
