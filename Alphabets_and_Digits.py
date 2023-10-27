#. Alphabets and Digits.py
''' 5 Write a Python program that accepts a string and calculate the number of digits and letters.

Sample Data : hey am cemputus12980
Expected Output :
hey am cemputus12980
Letter:  13
Digits:  5 '''

str = input("Please enter the string: ")
a = b = 0

for i in str:
    if i.isdigit():
        a = a + 1
    elif i.isalpha():
        b = b + 1
    
print(str)
print("Letter: ", b)
print("Digits: ", a)
