#The "for" loop

primes = (2,3,5,7)

for prime_number in primes :
    print(prime_number,end=" ")
print("")

#Example 2

for i in range(1,11,2):
    print(i,end=" ")
print("")


#"while" loops
i=0
print("While loop")
while i<11:
    print(i,end=" ")
    i+=1
print("")

#Break & Continue Statements
    #break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement. A few examples:

i = 1
while i < 10:
    print(i,end=" ")
    i += 1
    if i>5:
        break #exit the loop

for i in range(1,12,1):
    if(i%2==0):
        continue #skip the current block
    print(i)


#Can we use "else" clause for loops?

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

    

