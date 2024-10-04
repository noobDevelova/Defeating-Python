print("#" * 20)
print("Hello there, welcome to Dufan's Rollercoaster")
print("Register form below there\n")

height = int(input("Fill your height: "))
cost = 0

if height >= 120:
    age = int(input("Fill your age: "))

    if age >= 18:
        cost = 12
    elif age >= 12 or age < 18:
        cost = 7
    else:
        cost = 5
    
    photos = input("Want photos? Y/N ")

    if photos == 'Y':
        cost += 3
    
    print(f'The Total Bill is ${cost}')
else:
    print("Sorry, You Cant Ride.")

print("#" * 20)
