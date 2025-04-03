distance = int(input("enter distance you wanna travel "))

if distance < 3:
    print("Walk")

elif distance >= 3 and distance < 15:
    print("bike")

else:
    
    print("car")