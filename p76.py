a=str(input("請輸入傳送密碼(6位數):"))

if len(a)==6:
   print("解密後的密碼",int(a[0])*2%7,int(a[1])*2%7,int(a[2])*2%7,int(a[3])*2%7,int(a[4])*2%7,int(a[5])*2%7)
else:
    print("請重新輸入")

           

    