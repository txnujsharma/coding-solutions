check_day = input("if its wednesday today, type 1. if not, type 0 ")


if check_day == "0":
        age = input("enter your age: ")
        input_age = int(age)
        if input_age > 18:
                print("your ticket price is 18 dollars")
        else :
                print("Your ticket price is 8 dollars")
if check_day == "1":
        age = input("enter your age: ")
        input_age = int(age)
        if input_age > 18:
                print("your ticket price is 17.64 dollars")
        else :
                print("Your ticket price is 7.84 dollars")