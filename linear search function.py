def lin(a,c,item):
    count = 0
    for i in range(c):
        if a[i] == item:
            print("item is present at {}th location".format(i+1))
            return 0
        else:
            if count == c:
                print("element is not present")
            else:
                count = count+1

a = [1,2,3,4,5,34,45,23]
c = len(a)
item=45
lin(a,c,item)