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

# import random

# num = list(range(1,101))
# #OR...
# # num = random.randint(1,100)
# secret_num = random.choice(num)
# guesses = 0

# if input("Pick diffaculty: ") == 'easy':
#     guesses = 10
# else:
#     guesses = 5

# def make_guess():
#     global guesses
#     new_guess = int(input("Guess number: "))
#     guesses -= 1

#     if guesses <= 0:
#         return print("GAME END... :(")

#     if new_guess > secret_num:
#         print("Too high!")
#     elif new_guess < secret_num:
#         print("Too low!")
#     elif new_guess == secret_num:
#         return print("CORRECT!!")
#     else:
#         print("NANI...?!")
#     make_guess()
    
# make_guess()

# print(guesses)

#=====================DAY13===================================#
#-------------DEBUGGING----------
# def my_function():
#     for i in range(1,21):
#         # print(i)
#         if i == 20:
#             print("TEST")
# my_function()

#-------------DEBUGGING----------
# from random import randint
# dice_imgs = ["D1",'D2','D3','D4','D5','D6']
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])


#-------------DEBUGGING----------
 #pythontutor.com/visualize
 #helps see your code run step by step

#=====================DAY14===================================#

#HIGHER LOWER GAME
# import random
# my_list = {
#     "bob":1, 
#     "tree":2, 
#     "bird":3
# }


# def game_end():
#     print("END...")

# def user_response():
#     user_said = input("HIGHER, LOWER, QUIET(h/l/q)?: ")
#     if user_said == "h":
#         return 'h'
#     elif user_said == 'l':
#         return 'l'
#     else:
#         game_end()
    
# def setup_game():
#     for key in my_list:
#         print(f"{key}=>{my_list[key]}")

# def run_game():
#     #set 
#     item_a = random.choice(list(my_list))
#     item_b = random.choice(list(my_list))

#     # print(my_list)
#     # print(f"{item_a}=>{my_list[item_a]}")
#     print(f"{item_a} vs. {item_b}")
#     user_input = user_response()
#     user_score = 0

#     if user_input == 'h' and my_list[item_a] > my_list[item_b]:
#         user_score += 1
#         print("WINNER")
#     elif user_input == 'l' and my_list[item_a] < my_list[item_b]:
#         user_score += 1
#         print("WINNER")
#     else:
#         print(user_score)
#         game_end()

# run_game()



# # PRINT EVERYTHNG
# print(my_list.items())
# # PRINT ALL VALUES
# print(my_list.values())
# # PRINT VALUE OF KEY
# print(my_list["bird"])
# # MAKE NEW
# my_list['cat'] = 10
# print(random.choice(list(my_list.keys())))

# print(my_list)

#=========================DAY15=========================================#

#INSTALL PYCHARM...

#----------------COFFEE MACHINE CHALLENGE--------------
# REQUIREMENTS
# 1. PRINT RESOURCES
# 2. Check of resources sufficient


# flavors = [
#     {
#     'name':'expresso', 
#     'price':1.50,
#     'ingredients':{'water':50,'coffee':18,'milk':0}
#     },
#     {
#     'name':'latte',
#     'price':2.50,
#     'ingredients':{'water':200,'coffee':24,'milk':150}
#     },
#     {
#     'name':'cappuccino',
#     'price':3.00,
#     'ingredients':{'water':250,'coffee':24,'milk':100}    
#     }
# ]
# # [Water, coffee, milk]
# machine_resorces = [300,100,200]
# #pennies, nickels, dimes, quarters
# coin_values = [0.01,0.05,0.10,0.25]
# chosen_coffee = {}
# ammount_owed = 0
# # print(flavors[0]['name'])
# # print(flavors[0]['price'])
# # print(flavors[0]['ingredients'])

# def pay_machine():
#     global ammount_owed
#     print("Please insert coins: ")
#     #amount user pays in
#     temp_amount = coin_values[0]*int(input("pennies? ")) + coin_values[1]*int(input("nickels? ")) + coin_values[2]*int(input("dimes? ")) + coin_values[3]*int(input("quarters? "))
#     #subtract coins from amount owed for coffee        
#     ammount_owed = ammount_owed - temp_amount
#     if ammount_owed <= 0:
#         print('THANK YOU!')
#     else:
#         print("Not quiet enough!")
#         pay_machine()

# def pick_coffee():
#     global chosen_coffee, ammount_owed
#     # Get users desired coffee e.g. 'latte'
#     temp_coffee = input("What would you like? (expresso/latte/cappuccino): ")

#     #Get the ingredients for that coffee
#     for flavor in flavors:
#         #If user request exists in machine array
#         if temp_coffee == flavors[flavors.index(flavor)]['name']:
#             #set chosen coffee to coffee's ingredients
#             chosen_coffee = flavors[flavors.index(flavor)]
#             ammount_owed = flavors[flavors.index(flavor)]['price']

# def enough_resources():
#     global chosen_coffee, machine_resorces
#     cof_res = []
    
#     #put ingredient amounts for chosen coffee into array form [water,coffee,milk]
#     for ingred in chosen_coffee['ingredients']:
#         # print(f"{ingred} => {chosen_coffee['ingredients'][ingred]}")
#         cof_res.append(chosen_coffee['ingredients'][ingred])
#         # print(chosen_coffee['ingredients'][ingred])

#     # Compare to machine resources, true if enough to make
#     if machine_resorces[0] >= cof_res[0]:
#         if machine_resorces[1] >= cof_res[1]:
#             if machine_resorces[2] >= cof_res[2]:
#                 # print(machine_resorces)
#                 # print(cof_res)
#                 machine_resorces = [machine_resorces[0]-cof_res[0], machine_resorces[1]-cof_res[1], machine_resorces[2]-cof_res[2]]
#                 return True
#     else:
#         return False

# def run_machine():
#     pick_coffee()
#     if enough_resources() == True:
#         print("Enough to make coffee!")
#         print(f"MACHINE RESOURCES LEFT: {machine_resorces}")
#         print(f"coffee price: {ammount_owed}")
#     else:
#         print("Not enough ingredents for coffee... :(")
#     pay_machine()
    
# run_machine()

#==============================DAY16=====================================#
#-------------OOP and CLASSES / OBJECTS---------------------
#CLASSES => BLUEPRINTS THAT GENERATE OBJECTS
#OBJECTS => MADE BY CLASSES, 

#        object      class
# e.g. => car = CarBluePrint()

#==========================DAY17====================================#
#pass => skip, place holder...
#Classes named by Pascal Casing (e.g. "PascalCasing")
# class User:
#     #Constructor - part of Class, AKA initializes Class
#     #   Constructor(object_being_made, any_peramiters)
#     #                    (paramaters)
#     def __init__(self,user_id,username):
#         #initialize attributes...
#         # print("TEST") #Runs every time new object from this class...
#         #ID => attribute...
#         self.id = user_id
#         self.username = username

#ATTRIBUTES = CHARACTERISTICS OF OBJECTS MADE
#METHODS => THINGS CLASS CAN DO (FUNCTIONS)


#OLD CODE BEFORE CONSTRUCTOR...
# class User()
#     pass
# user_1 = User()
# user_1.id = '001'
# user_1.username = 'daniel'

# user_2 = User()
# user_2.id = '002'
# user_2.username = 'jack'

# print(user_1.username)

#SO...

# #CLASS
# class User:
#     #CONSTRUCTOR
#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.username = username
#         #No need for paramater, automaticallly sets to 0...
#         self.followers = 0
#         self.following = 0
#     #METHOD1
#     def add_followers(self):
#         self.followers += 1
#         self.following += 1

# user_1 = User('001','daniel')
# user_2 = User('002','jack')
# user_1.add_followers()
# user_1.add_followers()

# print(user_1.followers)
# print(user_2.followers)


 