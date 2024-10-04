print("Welcome to Pizza Deliveries")

print("Small Pizza (S): $15")
print("Medium Pizza (M): $20")
print("Large Pizza (L): $25")
size = input("What size pizza do you want? S, M, or L: ")


print("Add Pepperoni for small pizza: +$2")
print("Add Pepperoni for medium or large pizza: +$3")
peperoni = input("Do you want peperoni on your pizza? Y or N: ")

print("Add extra cheese for your pizza: +$1")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total = 0

if size == 'S':
    total += 15
elif size == 'M':
    total += 20
else:
    total += 25

if peperoni == 'Y':
    if size == 'S':
        total += 2
    else:
        total += 3

if extra_cheese == 'Y':
    total += 1

print(f"Your final bill is ${total}")



