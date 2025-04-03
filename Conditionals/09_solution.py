year = int(input("enter the year! "))
if year % 100 == 0  and year % 400 != 0:
    print("It is a leap year")

elif year % 4 == 0  and year % 100 != 0:
    print("It is a leap year")

elif year % 400 == 0 :
    print("It is not a leap year")

else:
    print("it ia not a leap year")