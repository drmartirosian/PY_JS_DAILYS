#==============================DAY11====================================#
#Black jack complete!

#==============================DAY12====================================#
#-----------------SCOPES-NAMESPACES
# num = 1

# def increase_num():
#     num = 2
#     print(f"LOCAL VARIABLE:{num}")
# increase_num()

# print(f"GLOBAL VARIABLE:{num}")

#-------------NO BLOCK SCOPE IN PYTHON--------------------
# game_level = 3
# enemies = ["ZOMBIES","ALIENS","SKELETON"]
# new_enemy = "ALIEN"

# if game_level < 5:
#     new_enemy = enemies[0]

# def new_func():
#     # global new_enemy
#     new_enemy = "WEREWOLF"
#     # print(new_enemy)
# new_func()

# print(new_enemy)

#---------------CONSTANTS
# CAPITALIZE NAME OF VARIABLE






#-------------NUMBER GUESSING GAME--------------

import random

num = list(range(1,101))
#OR...
# num = random.randint(1,100)
secret_num = random.choice(num)
guesses = 0

if input("Pick diffaculty: ") == 'easy':
    guesses = 10
else:
    guesses = 5

def make_guess():
    global guesses
    new_guess = int(input("Guess number: "))
    guesses -= 1

    if guesses <= 0:
        return print("GAME END... :(")

    if new_guess > secret_num:
        print("Too high!")
    elif new_guess < secret_num:
        print("Too low!")
    elif new_guess == secret_num:
        return print("CORRECT!!")
    else:
        print("NANI...?!")
    make_guess()
    
make_guess()

# print(guesses)