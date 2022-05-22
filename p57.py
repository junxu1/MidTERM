
from telnetlib import PRAGMA_HEARTBEAT


meal=(input("請選擇主餐及升級的套餐:").split(' '))
drink=(input("是否升級成大杯飲料:"))
fries=(input("是否換成大薯:"))
money=0
if meal[0]=="1":
    money=money+72
elif meal[0]=="2":
    money=money+62
elif meal[0]=="3":
    money=money+82
elif meal[0]=="4":
    money=money+44
elif meal[0]=="5":
    money=money+60

if meal[1]=="A":
    money=money+55
elif meal[1]=="B":
    money=money+68
if drink=='是':
    money=money+7
elif drink=='否':
    money=money+0

if fries=='是':
    money=money+13
elif fries=='否':
    money=money+0
print('總共為:',money)   

