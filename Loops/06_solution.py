given_number = 5
product = 1
factorial = 1
for i in range(1, given_number + 1):
    product = factorial* product
    factorial+= 1
print("factorial: ",product)