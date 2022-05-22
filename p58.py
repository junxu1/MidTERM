
i=0
array=[]
for i in range(0,10):
    a=(input("請輸入第"+str(i+1)+"個數字"))
    array.append(a)
array.sort()
array.reverse()
print("最大的3個數為:",array[0],",",array[1],",",array[2])
print("最小的3個數為:",array[7],",",array[8],",",array[9])
