a=input("請輸入考試次數及學生數")
b=float(input("每次考試比率"))
array=[0]
for i in range(a):
    array.append(str(input("第"+str(i+1)+"組:")))
for i in range(a):
    print("第"+str(i+1)+"組應收費用",int(array[i+1][0])*250+int(array[i+1][2])*175)

