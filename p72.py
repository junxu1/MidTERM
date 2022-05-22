from re import S


n=int(input("請輸入n:"))
k=int(input("請輸入k:"))
if n>k and k>1:
    s=(n//k)+n
    sum=((s-n)//k)+s
    print("Peter可以抽",sum,"支紙菸")

