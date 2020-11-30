# try-except
astr = "Hello Bob"
istr = int(astr)
print("First", istr)
astr = "123"
istr = int(astr)
print("Second", istr)
'''
Traceback (most recent call last):
  File "7.py", line 3, in <module>
    istr = int(astr)
ValueError: invalid literal for int() with base 10: 'Hello Bob'
'''
