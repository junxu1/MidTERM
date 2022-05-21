a =int(input("輸入度數"))

if a<=120:
    print("Summer month",a*2.1)
    print("Non-summer month",a*2.1)
elif 121<=a<=330:
    print("Summer month",120*2.1+(a-120)*3.02)
    print("Non-summer month",120*2.1+(a-120)*2.68)
elif 331<=a<=500:
    print("Summer month",120*2.1+210*3.02+(a-330)*4.39)
    print("Non-summer month",120*2.1+210*2.68+(a-330)*3.61)
elif 501<=a<=700:
    print("Summer month",120*2.1+210*3.02+170*4.39+(a-500)*4.97)
    print("Non-summer month",120*2.1+210*2.68+170*3.61+(a-500)*4.01)
else:
    print("Summer month",120*2.1+210*3.02+170*4.39+200*4.97+(a-700)*5.63)
    print("Non-summer month",120*2.1+210*2.68+170*3.61+200*4.01+(a-700)*4.5)

