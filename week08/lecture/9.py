# String Library

# upper or lower character
greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(greet)
print("Hi there,".upper())

# searching
fruit = "banana"
pos = fruit.find("na")
print(pos)

aa = fruit.find("z")
print(aa)

#search and replace
nstr = greet.replace("Bob", "Jane")
print(nstr)

nstr = greet.replace("o", "X")
print(nstr)


# Stripping Whitespace
name = " Yuriko "
n1 = name.lstrip()
n2 = name.rstrip()
n3 = name.strip()
print(n1)
print(n2)
print(n3)
n4 = "".join(name.split())
print(n4)
