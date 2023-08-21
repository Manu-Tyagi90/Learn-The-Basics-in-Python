item=12
count=0
a=[1,2,3,4,5,6,7,8,9,10,12,34,554,6666]
b=len(a);
for i in range (b) :
    if item==a[i]:
        print("the item is located at {}th location".format(i+1))
        exit()
    else:
        if count ==len(a)-1:
            print("item is not Present");
        else:
            count=count+1;