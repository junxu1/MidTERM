a = int(input("輸入整數n:"))
list=[a]
if 0<a<10**6:
    while a !=1:
        if a%2 !=0:
            a=3*a+1
        else:
            a=int(a/2)
        list.append(a)
print("數列",list)