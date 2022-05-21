a = int(input("小明身上有幾元:"))
b=int(input("販賣機有幾種飲料:"))
z=0
if 0<=a<=100 and 1<=b<=50:
    array=[]
    for i in range(b):
        c=int(input("第"+str(i+1)+"種飲料:"))
        if 10<=c<=50:
            array.append(c)
        else:
            print("error")
            continue
    for i in range(b):
        if array[i]<=a:
            z=z+1
    print(z)
else:
    print("error")
    

    