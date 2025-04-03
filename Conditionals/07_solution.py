size = input("enter size of your cup. small, medium, large ")
espresso = input("you you want extra shot of espresso yes or no ")

if espresso == "yes" and size == "small":
    print("Small Cup of coffee with extra shot of espresso")

elif espresso == "yes" and size == "medium":
    print("medium Cup of coffee with extra shot of espresso")

elif espresso == "yes" and size == "large":
    print("large Cup of coffee with extra shot of espresso")

elif espresso == "no" and size == "small":
    print("Small Cup of coffee without shot of espresso")

elif espresso == "no" and size == "medium":
    print("medium Cup of coffee without shot of espresso")

elif espresso == "no" and size == "large":
    print("large Cup of coffee without shot of espresso")