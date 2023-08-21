def bin(a,item,lb,ub):
    for i in range (ub):
        mid = int((lb + ub) / 2)
        if a[mid]==item:
            print("item is present at {}th location".format(mid+1))
            return 0
        else:
            if a[mid]<item:
                lb=mid+1
            else:
                ub=mid-1

item=23
a=[2,3,4,5,6,21,22,23,33]
lb=0
ub=len(a)
bin(a,item,lb,ub)
