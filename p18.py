a = input("輸入五張牌")
b=0
for i in range(5):
    if a[i] =="j":
        b=b+11
    elif a[i] =="q":
        b=b+12
    elif a[i] =="k":
        b=b+13
    elif a[i] =="a":
        b=b+1  
    else:
        b=b+int(a[i])        
print(b)