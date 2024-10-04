print(r""""
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
      """)

print("Welcome to Treasure Island.")
print("You're at a cross road. Where do you want to go?")
turn = input("  Type \"left\" or \"right\"  \n")

if turn == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input("  Type \"wait\" to wait for a boat. Type \"swim\" to swim across.  \n")
    
    if action == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        doors = input("  One red, one yellow and, one blue. Which colour do you choose?  \n")
        
        if doors == "yellow":
            print("You Win!")
        elif doors == 'red':
            print("Burned by fire.")
            print("Game Over.")
        elif doors == 'blue':
            print("Eaten by beasts.")
            print("Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by a trout.")
        print("Game Over.")
else:
    print("Fall into a hole.")
    print("Game Over.")


