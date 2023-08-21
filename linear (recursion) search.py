
def lin(a, n, item,i,count):

    if a[i]==item:
        print("item is located at {}th location ".format(i+1))
        return 0;
    else:
        if count==n :
            print("Item is Not Present ")
        else:
            count = count+1
            i = i +1
            return lin(a,n,item,i,count)
item=2;
a=[0,1,2,3,4,5,6,7,8,9]
n=len(a)
i=0
count=0
lin(a,n,item,i,count)