nums = [int(i) for i in input("輸入數字:").split(',')] 
nums.sort()                         
min = nums[0]                    
while min!=1:                    
    for i in range(1,len(nums)):    
        r = nums[i]%min          
        if r !=0:                   
            nums.insert(0, r)      
            break                 
    if min != nums[0]:         
        min = nums[0]          
    else:
        break                    
print("最大公因數=",min)