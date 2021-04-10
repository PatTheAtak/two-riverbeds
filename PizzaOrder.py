# Check the README to understand how logic of the program.
#
#

print("Welcome to PatTheAtak Pizza Deliveries!")
size = input("What size of pizza do you want(S, M, or L)?  ")
add_pepperoni = input("Do you want pepperoni(Y or N)?  ")
extra_cheese = input("Do you want extra cheese(Y or N )? ")

price = 0

if add_pepperoni == "Y":
    if size =="S":
        price = 15
        price += 2

    elif size == "M":
        price = 20
        price += 3

    elif size == "L":
        price = 25
        price += 3
else:
    if size == "S":
        price = 15
    elif size == "M":
        price = 20
    elif size == "L":
        price = 25


if extra_cheese == "Y":
    price = price + 1

print(f'Your final bill is: ${price}')





