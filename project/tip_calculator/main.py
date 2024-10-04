print("#" * 30)
print("Tip Calculator")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill? "))

summary = round((bill * (tip + 1) / people), 2)
print(f'Each person should pay ${summary:0.2f}')

print("#" * 30) 
