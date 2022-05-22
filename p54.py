a1=float(input("請輸入路程公里數km:"))
if a1<1.5:
    print("所需車資為:",75)
elif a1>1.5:
    km=1.5
    money=75
    while True:
        if a1<= km:
            break
        km=km+0.25
        money=money+5
        
    print(money)