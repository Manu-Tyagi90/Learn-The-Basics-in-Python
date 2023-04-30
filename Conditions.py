#Notice that variable assignment is done using a single equals operator "=", whereas comparison between two variables is done using the double equals operator "==". The "not equals" operator is marked as "!=".

x=2
print(x==2)
print(x==3)
print(x<3)
print(x>3)

#Boolean operators
    #The "and" and "or" boolean operators allow building complex boolean expressions, for example:
name="John"
age=34

if name=="John" and age ==34: #True only When Both statements are True Else False
    print("Your Name is %s and You Are %d Year Old"%(name,age))

if name=="John" or age == "Rick": #True only When atleat one statement is True Else False
    print("Your Name is %s or You Are Rick"%(name))

#The "in" operator or Membership Operators
name="Manu"
if name in ["Manu","Drashti"]:
    print("Your Name is Either Manu Or Drashti")

#The 'is' operator or Identity Operartors
x=[1,2,3]
y=[1,2,3] #For list
print(x==y)
print(x is y) #false

x=(1,2,3)
y=(1,2,3) #For tuple
print(x==y)
print(x is y) #true


#The "not" operator
print(not False)
print(not True)

