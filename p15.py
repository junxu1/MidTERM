a =str(input("輸入一組四位數字為:"))



print("輸出加密後的數字為",str((int(a[2])+7)%10)+str((int(a[3])+7)%10)+str((int(a[0])+7)%10)+str((int(a[1])+7)%10))