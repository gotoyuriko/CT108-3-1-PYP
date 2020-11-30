# try-except
istr = -1
astr = "Hello Bob"

try:
    istr = int(astr)
except:
    print("Cannot Convert String to Int")
print("First", istr)


astr = "123"
try:
    istr = int(astr)
except:
    istr = -1
print("Second", istr)
