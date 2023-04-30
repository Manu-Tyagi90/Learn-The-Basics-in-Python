#lists

#Program 1

list = []
list.append(1)
list.append(2)
list.append(3)
list.append(2)
list.append(2)
list.append(2)

for x in list :
    print(x, end=" ")

#Program 2

list=[1,2,3]
print(list[1])


'''Exercise
In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.
You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.'''

numbers = []
strings = []
names_list = ["raju", "shyam"]
second_name= names_list[1]

print(second_name)

numbers.append(1)
numbers.append(2)
numbers.append(3)
for x in numbers :
    print(x,end=" ")
    #or
print(numbers)

print("\n")
strings.append("hello")
strings.append("World")
for y in strings :
    print(y, end=" ")
print(strings)
    
