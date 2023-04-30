name = "Manu Tyagi"
print("Hello %s"%name)

#To use two or more argument specifiers, use a tuple (parentheses):
name ="renu"
age = 44
print ("my mother name is %s. she is %d Year Old "%(name,age))

#Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string. For example:
list=[1,2,3,4,5]
print("my list is %s " %list)


'''Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)'''

print("%x"%23)

'''Exercise
You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.
'''
name ="John Doe"
amount ="$53.44"
print("Hello %s. Your current balance is %s."%(name, amount))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)