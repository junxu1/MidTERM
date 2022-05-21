n =int(input("輸入整數n:"))
for i in range(1,n+1,1):
    if n/2>i:
        b=i*2-1
        print(" "*int((n-1)/2)+str(int(b)))   
    if int(n/2)==i:
        z=""
        for s in range(1,n+1,1):
            if(s>n/2+1):
                b=(n-s)*2+1
            if(s==int(n/2)+1):
                b=n
            if(s<n/2):
                b=(s-1)*2+1
            z=z+str(b)
        print(z)
    if n/2+1<i:
        b=(n-i+1)*2-1
        print(" "*int((n-1)/2)+str(int(b)))            


    