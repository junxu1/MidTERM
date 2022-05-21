n =int(input("可能會跑到n個點"))
list=[]
if 2<=n<=10:
    for i in range(n):                      
        k=int(input("第"+str(i+1)+"個點:"))
        if 1<=k<=1000:
            list.append(k)
    for s in range(n):
        if list[s]%9==0 or list[s]%11==0:
            print("第",s+1,"個點:",list[s])
           






