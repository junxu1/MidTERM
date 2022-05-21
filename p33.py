chinese=int(input("國文:"))
en=int(input("英文:"))
pe=int(input("體育:"))
py=int(input("程式設計:"))
cal=int(input("微積分:"))
list=[chinese,en,pe,py,cal]
list.sort()
if list[4]==chinese:
    print("成績最好的科目","國文",list[4])
elif list[4]==en:
    print("成績最好的科目","英文",list[4])
elif list[4]==pe:
    print("成績最好的科目","體育",list[4])
elif list[4]==py:
    print("成績最好的科目","程式設計",list[4])
elif list[4]==cal:
    print("成績最好的科目","微積分",list[4]) 
if list[0]==chinese:
    print("成績最差的科目","國文",list[0])
elif list[0]==en:
    print("成績最差的科目","英文",list[0])
elif list[0]==pe:
    print("成績最差的科目","體育",list[0])
elif list[0]==py:
    print("成績最差的科目","程式設計",list[0])
elif list[0]==cal:
    print("成績最差的科目","微積分",list[0])                 
avg=(chinese+en+pe+py+cal)/5
list.append(avg)
print("平均分數",list[5])


