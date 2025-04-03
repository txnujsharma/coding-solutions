word = input("enter your password ")
count = len(word)

if count <= 6:
    print("weak password")
elif 6 < count <=10 :
    print("medium password")
elif count > 10:
    print("strong password")
