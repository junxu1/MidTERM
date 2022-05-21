x =int(input("輸入x座標"))
y = int(input("輸入y座標"))
if x>0 and y>0:
    print("該點位於第一象限","離原點距離為根號",x*x+y*y)
elif x==0 and y==0:
    print("該點位於原點")
elif x==0 and y<0:
    print("該點位於下半面Y軸上","離原點距離為根號",y*y) 
elif x==0 and y>0:
    print("該點位於上半面Y軸上","離原點距離為根號",y*y) 
elif x<0 and y==0:
     print("該點位於左半面X軸上","離原點距離為根號",x*x)
else:
     print("該點位於右半面X軸上","離原點距離為根號",x*x)  


