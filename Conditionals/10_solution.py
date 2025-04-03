pet = input("is your pet a dog or cat! ")
age = int(input("what is the age of your per! "))

if pet == "dog" and age <= 2:
    print("puppy food")

elif pet == "dog" and age > 2:
    print("senior dog food")

elif pet == "cat" and age <= 2:
    print("kitten food")

elif pet == "cat" and age > 2:
    print("senior cat food")
