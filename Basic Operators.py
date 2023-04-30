#Arithmetic Operators

a= 4*5-5**5+5//5
print(a)

print(203.45//45.0)

#%mod operators

print(234%45)

#exponent Operators
print(5**7)  #power operator

#or
import math
print(math.pow(5,7))


#Using Operators with Strings
# add operator works as contatination
print("Hello" + " " + "World")

#multiplication operator works as repeatition
print("hello "*10)

#Using Operators with Lists
    #Lists can be joined with the addition operators:
odd_numbers =[2,4,6,8]
even_numbers = [1,3,5,7,9]
print(odd_numbers+even_numbers)
    #multiplication
print(odd_numbers*3)

               #Exercise
#The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x_list = [1,2,3,4,5,6,66]
y_list = [2,3,4,5,6,7,88]
big_list = x_list+y_list
print(big_list)


