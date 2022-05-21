from array import array


a = int(input("輸入查詢組數N為"))
array=[]
for i in range(a):
    array.append(str(input("第"+str(i+1)+"組:")))
for i in range(a):
    print()

