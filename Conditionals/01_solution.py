age = input("provide me and age: ")
age_in_int = int(age)
if age_in_int < 13:
     print("child")

if age_in_int >= 13 and age_in_int <= 19 :
     print("teenager")

if age_in_int >= 20 and age_in_int <= 59 :
     print("adult")

if age_in_int >= 60:
     print("senior")


