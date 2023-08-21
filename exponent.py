def exponent(n,m):
    if n<1:
        print("1")
        return 0;
    else:
        print("the exponent of {} & {} is : {}".format(n,m,n**m))

a=int(input("Enter the number "))
b=int(input("Enter the number "))
exponent(a,b);


