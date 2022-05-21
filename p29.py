from array import array
import string

string0=""
a=str(input("甲方的數字:"))
b=str(input("乙方的數字:"))
if len(a)==len(b):
    for i in range(len(a)):
       if int(a[i])>int(b[i]):
           string0=string0+"贏"
       elif int(a[i])<int(b[i]):
            string0=string0+"輸"
       else:
            string0=string0+"和"
    print(string0)
else:
    print("error")

