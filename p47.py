a = int(input("輸入筆數"))
if  a <=4:
    dict1={"金":4,"銀":5,"銅":9,"優":7}
    list1=zip(dict1.keys(),dict1.values())
    for key,values in list1:
        print("%s牌得到%d面"%(key,values))
   
