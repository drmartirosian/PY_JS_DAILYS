import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = [0]
computer_hand = [0]



def continue_game():
    if check_for_21() == False:
        if input("Continue (y/n)? ") == 'y':
            deal_cards()
            print(f"USER=>{user_hand} vs {computer_hand[0]}<= COMPUTER")
            continue_game()
        else:
            declare_winner()
    else:
        return declare_winner()





def deal_cards():
    #Deal user cards...
    user_hand.insert(len(user_hand),int(random.choice(cards)))
    user_hand[0] += user_hand[len(user_hand)-1]
    if computer_hand[0] < 19:
        #Deal to computer...
        computer_hand.insert(len(computer_hand),int(random.choice(cards)))
        computer_hand[0] += computer_hand[len(computer_hand)-1]
   
def check_for_21():
    if user_hand[0] >= 21 or computer_hand[0] >= 21:
        return True
    else:
        return False

def check_for_aces():
    if 11 in user_hand and user_hand[0] > 21:
        user_hand[int(user_hand.index(11))] = 1
    elif 11 in computer_hand and computer_hand[0] > 21:
        computer_hand[int(computer_hand.index(11))] = 1

def declare_winner():
    # print(f"GAME OVER!!! USER=>{user_hand} vs {computer_hand}<=COMPUTER")
    if user_hand[0] > 21 and computer_hand[0] > 21:
        print("LOSER DRAW!")
    elif user_hand[0] > 21:
        print("COMPUTER WINS!")
    elif computer_hand[0] > 21:
        print("USER WINS!")
    elif user_hand[0] > computer_hand[0]:
        print("WINNER, WINNER, CHICKEN DINNER!")
    elif computer_hand[0] > user_hand[0]:
        print("COMPUTER WIN!")
    elif user_hand[0] == computer_hand[0]:
        print("DRAW!")
    else:
        print("NANI...?!?")

print(continue_game())
