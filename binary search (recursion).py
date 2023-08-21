def bin(a,lb,ub,item):
    mid=int((lb+ub)/2)
    if(a[mid]==item):
        print("item is located at {}th Location".format(mid+1))
        return 0;
    elif(a[mid]<item):
        lb=mid
        return bin(a, lb, ub, item)

    else:
        ub=mid
        return bin(a, lb, ub, item)
item=45
a=[1,2,3,4,5,6,7,10,11,12,23,45,67]
lb=0;
ub=len(a)
bin(a,lb,ub,item)





