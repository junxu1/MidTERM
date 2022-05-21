N= int(input("input N"))
M= int(input("input M"))
arr=["Array"]
Narr=["Array"]
for a in range(0,int(N),1):
    for b in range(0,int(M),1):
        arr.append(input("N"+str(a)+"*M"+str(b)+":"))
d=1
for g in range(0,int(N),1):
    print(arr[d:d+int(M)])
    d=d+int(M)
for e in range(1,M+1,1):
    d = e
    for f in range(0,N,1):
        Narr.append(arr[d])
        print (d)
        d = d + M
d=1
for c in range(0,int(M),1):
    print(Narr[d:d+int(N)])
    d=d+int(N)
