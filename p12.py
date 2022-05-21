
arr=["Array"]
arrn=[0]
count = 0
while True:
    inp = input()
    count = count+1
    if inp=="$":
        count = count-1
        break
    Q=True
    for a in range(0,len(arr),1):
        if arr[a]==inp:
            Q=False
            b = a
    if Q==False:
        arrn[b] = arrn[b]+1
    else:
        arr.append(inp)
        arrn.append(1)
for e in range(0,len(arrn),1):
    if arrn[0]<arrn[e]:
        arrn[0] = arrn[e]
        p=e
if arrn[0]>count/2:
    print(arr[p])
else:
    print("NO")
    
