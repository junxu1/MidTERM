a1=int(input("請輸入第一個要判斷的數字:"))
a2=int(input("請輸入第二個要判斷的數字:"))
if a1%2==1 and a2%2==1 and a1-a2==2 or a2-a1==2:
    print("Y")
else:
    print("N")