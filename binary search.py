a=[2,4,6,7,8,9,10,11,12,13]
b=0
c=len(a)
item=12
for i in range (b,c):
    mid=int((b+c)/2)
    if a[mid]<item:
        b=mid
    elif a[mid]==item :
        print("item is located at {}th location".format(mid+1))
        exit()
    else:
        c=mid-1;