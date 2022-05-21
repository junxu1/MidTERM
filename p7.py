a=input("輸入月租費及通話時間:").split(",")

if int(a[0]) == 186:
    if int(a[1])*0.09<186*2:
        print("通話費為:",round(int(a[1])*0.09*0.9))
    else:
        print("通話費為:",round(int(a[1])*0.09*0.8))
elif int(a[0]) == 386:
    if int(a[1])*0.08<386*2:
        print("通話費為:",round(int(a[1])*0.08*0.8))
    else:
        print("通話費為:",round(int(a[1])*0.08*0.7))
elif int(a[0]) == 586:
    if int(a[0])*0.07<586*2:
        print("通話費為:",round(int(a[1])*0.07*0.7))
    else:
        print("通話費為::",round(int(a[1])*0.07*0.6))
elif int(a[0])== 986:
    if int(a[1])*0.06<986*2:
        print("通話費為:",round(int(a[1])*0.06*0.6))
    else:
        print("通話費為:",round(int(a[1])*0.06*0.5))



