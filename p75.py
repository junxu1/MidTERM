i=0
while i>=0:
    array=[]
    things = input("請輸入事項(若以無事項,請輸入end):")
    array.append(things)
    i+=1
    if things=="end":
        break
    else:
        print(i,".",things)