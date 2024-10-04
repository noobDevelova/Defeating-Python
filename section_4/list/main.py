import random

friends = ["Randi", "Nepil", "Jupri", "Audi", "Deja"]

roulette = random.randint(0, len(friends) - 1)
friends[-1] = 'Pahed'
print(friends)