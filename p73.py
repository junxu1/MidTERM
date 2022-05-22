time1 = input("請輸入時間 1(時:分:秒):")
hr, min, sec = time1.split(":")
time2 = int(input("請輸入時間 2(秒):"))
ans1 = int(hr)*3600 + int(min)*60 + int(sec)
hr2=time2//3600
min2=(time2-3600)//60
sec2=(time2-3600)%60
print("時間1",time1,"格式轉換後為",ans1,"秒")
print("時間2",time2,"秒","=",hr2,":",min2,":",sec2)



