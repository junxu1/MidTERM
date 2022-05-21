a=int(input("輸入第一行正整數為:"))
b =str(input("輸入第二行正整數為:"))
array=[]
for i in range(0,len(b),1):
    if i%2 ==0:
        array.append(int(b[i]))
if a==len(array):
    intmax=max(array,key=array.count)
  
    if array.count(intmax) ==1:
        print("每個數值剛好出現1次")
    else:
          print("最大出現次數的數字為:",str(intmax),"出現次數為",str(array.count(intmax)))
else:
    print("error")
    




        
      

    
        
    