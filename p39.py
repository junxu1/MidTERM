n =int(input("輸入整數n:"))
for i in range(1,n+1,1):
    if(1<=i and i<n/2+1):
        s = i*2-1
        a=(n-s)/2
    elif(i==n/2+1):
        s=n
        a=(n-s)/2
    elif(i/2+1<i and i<=n):
        s=(n+1-i)*2-1
        a=(n-s)/2
    print(" "*int(a)+"*"*int(s))
