a =int(input("組數:"))
array=[0]
for i in range(a):
    array.append(str(input("第"+str(i+1)+"組:")))
for i in range(a):
    print("第"+str(i+1)+"組應收費用",int(array[i+1][0])*250+int(array[i+1][2])*175)

