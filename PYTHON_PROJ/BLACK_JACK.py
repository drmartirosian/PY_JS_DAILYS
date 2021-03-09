#ASK FOR CARDS
#RANDOM CARDS FROM 52
#CAN"T GO OVER 21 - BUST!
#JACK, KING, QUEEN = 1-
#ACE = 1 or 11
# DEALER SHOWS 1 card, rest of hand hidden
#Can see own hand
#HIT, STAY
#DRAWS
#DEALER HAND < 17, must take another card
# 1. do you want to play? y/n
# ace = 11 untl over 21, then 1
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = [0]
computer_hand = [0]

def continue_game():
    #Continue dealing cards
    if input("Continue (y/n)? ") == 'y':
        #Make sure no hand over 21
        if over_21() == True:
            return declare_winner()
        #Deal to user
        user_hand.insert(len(user_hand),int(random.choice(cards)))
        user_hand[0] += user_hand[len(user_hand)-1]
        #Deal to computer
        computer_hand.insert(len(computer_hand),int(random.choice(cards)))
        computer_hand[0] += computer_hand[len(computer_hand)-1]

        if over_21() == True:
            return declare_winner()

        print(f"{user_hand[0]} vs {computer_hand[0]}")
        continue_game()
    #Decline more cards
    else:
        return declare_winner()

def over_21():
    if user_hand[0] >= 21 or computer_hand[0] >= 21:
        return True
    else:
        return False

# def change_ace_to_one():
#     if 11 in user_hand and user_hand[0] > 21:
#         print("convert 11 to 1")
#     over_21()

def declare_winner():
    print(f"GAME OVER!!! USER=>{user_hand} vs {computer_hand}<=COMPUTER")


print(continue_game())