game=(input("請輸入遊戲時間:"))
min, sec = game.split(":")
gt=(int(min)*60+int(sec))-75
w = 1
s= 0
i=1
for i in range((gt//30)+1):
    i+=1
    if w%3==0:
        s+=7
    else:
        s+=6
    if w%2==0:
        s-=1
    w+=1
    gt-=30
print(s,"隻兵")





