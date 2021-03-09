#PYTHON100

#======================DAY1=========================#
# -----------------PRINT------------------------#
# print("Hello world!")

# -----------------QUOTES WITHIN QUOTES---------#
#print("print('What to print?')")

# -----------------LINE BREAK-------------------#
# print("TEST \n TEST")

# -----------------CONCAT-----------------------#
# print("Hello"+" World!")
# print("Hello"+" "+"World!")

# -----------------INPUT------------------------#
#input("WHAT IS YOUR NAME?")

# name = (input("What is yur name...? "))
# print(name)

# year = int(input("YEAR?"))
# print(year)

# -----------------INPUT, RESPONSE---------------#
# print msg incomplete, waits for input get rest of msg
# print("Hello, " + input("What is your name? ") + "!")

# -----------------LENGTH------------------------#
# print("NAME LENGTH:", len( input("NAME? ")))
# or...
# name = (input("What is your name? "))
# print(len(name))

# -----------------VARIABLES---------------------#
# name = "Jack" #original...
# name = "Bob" #changed to...
# name = input("WHAT IS YOUR NAME? ") #now is input value
# print(name)

# CHALLENGE: SWITCH VALUES...
# a = input("a:")
# b = input("b:")

# c = a
# a = b
# b = c
# or...
# a = [a, b]
# b = a[0]
# a = a[1]
# or...
# a = [input("a:"), input("b:")]
# b = a[0]
# a = a[1]

# print ("a:"+a+"\nb:"+b )

# -----------------NAMING---------------------#
# Snake case...
# no numbers at start of name...
# No caps...

# user_name = "name"

# --------------"ONLINE" NAME GENERATOR-----------------#
# print("Welcome to name generator!")
# pet = (input("What is your first pet's name? "))
# city = (input("What is your childhood street? "))
# print("Your 'online' name could be: " + city + " " + pet + "!")

#=====================DAY2=============================#

# -----------------DATA TYPES---------------------#

# Data Types

# STRINGS - "LETTERS/WORDS"
# print("HELLO"[2])
# print("HELLO "+"WORLD!")

# INTEGERS - NUMBERS
# print(100_000+100)

# FLOAT - NUMBERS WITH DECIMAL PLACES
# E.G. 3.14678 is a floating num

# BOOLEAN - TRUE OR FALSE

#-------------exorcise 1------------------

# # Can't print...?
# num_char = len(input("Give me number? "))
# # data type?
# print(type(num_char)) 
# # make string (stringify)
# new_num_char = str(num_char)
# # now works!
# print("Length of number was: "+new_num_char+"!")
# ---------------
# a = 1 #starting data int
# a = str(a) #makes string
# a = int(a) #makes integer
# a = bool(a) #makes boolean
# print(type(a)) #check type
# print(a)
# ---------------
# print(70+float(100.332)) # 170.332
# print(70+float("100.332")) # 170.332
# print(str(1)+str(2)) # 12
# print( int("1") + int("2")) # 3
#------------exorcise-2------

# user_num = input("2 digit num...")
# # print(user_num)
# nums = [int(user_num[0]), int(user_num[1])]
# # print(type(nums[0]))
# print( str(nums[0]) + "+" + str(nums[1]) + "=" + str(nums[0] + nums[1]))
# -----------------------------

# PEMDAS OPERATORS
# ()
# ** #exponent 2^2
# * and /
# + and -

# e.g.
# 1 + 1
# 2 - 1
# 3 * 3 
# 3 / 3
# 3 // 3 #chop off, no decimals
# 2**2 
# /=,*=,-=,+= #change variable + perform operation
# print(3 * 3 + 3 / 3 - 3) # 7
# print(3 * (3 + 3) / 3 - 3) # 3

# --------exorcise-BMI---
# person = [input("Weight(kg)? "), input("height(m)? ")]
# person = [int(person[0]), float(person[1])]
# print(type(person[0]), type(person[1])) #strings
# print("BMI: " + str((person[0]) / (person[1])**2) )

# ----------rounding nums---------------
# print(int(8/3))
# print(round(8/3)) #num, decimal places
# print(round(8/3, 1)) #num, decimal places
# print(8 // 3) #chop off after decmal places...

# result = 4/2
# # or...
# num = 4
# num += 2
# print(num)

#----------F-STRING( f"example text here..." )-----------
# score = 0
# height = 1.8
# is_winning = True
# #f-string
# print(f"Score: {score}, height: {height}, Winning?: {is_winning}")

# ---------challenge-time left-----------
# user_age = int(input("Your age? "))
# # print(type(user_age))

# years = round(90 - user_age)
# months = round(years * 12)
# weeks = round(months * 4.4)
# days = round(weeks * 30)

# print(f"-------Time left-------\nDays:{(days)}\nWeeks:{weeks}\nMonths:{months}\nYears:{years}")

# -----------TIP CALCULATOR---------------
# bill = round(float(input("What was the bill? ")),2)
# percent = bill * (int(input("Percentage tip? 10, 12, or 15? ")) / 100)
# num_people = int(input("How many people splitting bill? "))
# final_bill = round(((bill + percent) / num_people), 2)
# print(f"Each person should pay: ${final_bill}")
# --------------------------------------

# ======================DAY3===========================#

#------------IF ELSE ----------------#
# >
# <
# >=
# <=
# ==
# !=

# water_level = 50
# test_level = 80

# if water_level < test_level:
#     print("LESS")
# else:
#     print("MORE")

#------------------------------------
# height = int(input("What is your height?"))

# if height >= 120:
#     print("CAN RIDE")
# else:
#     print("Can't ride...")
#-----------ODD EVEN TEST--------------
# Modular ==> (%)

# num = int(input("Give number..."))

# if (num % 2) == 0:
#     print("EVEN")
# else:
#     print("ODD") 

#-------line if else---------
# print("EVEN") if num % 2 == 0 else print("ODD")

#-------or if else----------

# num = input("Give number...")
# num_len = len(num)
# x = 0

# if num_len <= 1:
#     x = int(num[0])
# else:
#     x = int(num[num_len-1])

# # print(x)

# if x == 0 or x == 2 or x == 4 or x == 6 or x == 8:
#     print("EVEN")
# else:
#     print("ODD")

#---------leap year test---------------

# year = 2100


# # Leap if year divisable by 4...
# if year % 4 == 0:
#     #except even divisable by 100
#     if year % 100 == 0:
#         # unless also divisable by 400
#         if year % 400 == 0:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("YES")
# else:
#     print("NO")

#---------if elif else-------
# if conditions:
#     ...
# elif conditions2:
#     ...
# else:
#     ...
#--------Ticket challenge--------
# photo = True
# cost = 0
# height = int(input("Height in cm? "))

# if height > 120:
#     print("Tall enough to ride!")
#     age = int(input("Age? "))
#     if age >= 18:
#         print("Age 18 or older? Ticket $12.")
#         cost += 12
#     elif age <= 12:
#         print("Age 12 or under? Ticket $5.")
#         cost += 5
#     else:
#         print("Between 12 and 18? Tickets $7.")
#         cost += 7
#     photo = str(input("Photo (Y/N)? "))

#     if photo == 'Y':
#         cost += 3
#     else:
#         cost += 0

#     print(f"Total cost for ride: ${cost}!")
# else:
#     print("Cant ride... :(")

# --------Pizza Challenge----------

# print("Welcome to Python Pizza!")
# size = input("What size pizza (S, M, L)? ")
# add_pepperoni = input("Want pepperoni (Y/N)? ")
# extra_cheese = input("Extra cheese (Y/N)? ")
# cost = 0

# if size == "S":
#     cost += 15
# elif size == "M":
#     cost += 20
# else:
#     cost += 25

# if size == "S" and add_pepperoni == "Y":
#     cost += 2 
# elif size == "M" and add_pepperoni == "Y":
#     cost += 3
# else:
#     cost += 0

# if extra_cheese == "Y":
#     cost += 1 

# print(f"Te price of your pizza is: ${cost}!")

#-----------and, or, not---------------

# -------Challenge LOVE CALCULATOR------
# names_combined = input("What is their name? \n") + input("What is their name? \n")

# true_arr = ['t','r','u','e']
# love_arr = ['l','o','v','e']

# true_count = 0
# love_count = 0
# final_number = 0

# for i in true_arr:
#     true_count += names_combined.lower().count(i)
# for i in love_arr:
#     love_count += names_combined.lower().count(i)

# final_number = int(str(true_count)+str(love_count))

# if final_number < 10 or final_number > 90:
#     print(f"BAM!! {final_number}%!")
# elif final_number >= 40 and final_number <= 50:
#     print(f"Woo! {final_number}%!")
# else:
#     print(f"Your score is {final_number}%...")

# ------choose adventure challenge
# print('''
# Welcome!
#       __...--~~~~~-._   _.-~~~~~--...__
#     //               `V'               \\ 
#    //                 |                 \\ 
#   //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
#  //__.....----~~~~._\ | /_.~~~~----.....__\\
# ====================\\|//====================
#                     `---`

# ''')
# q1 = input("Left or right (R/L)? \n").lower()
# if q1 == "r":
#     q2 = input("Swim or wait (S/W)? \n").lower()
#     if q2 == "w":
#         q3 = input("Which door (R, B, Y)? \n").lower()
#         if q3 == "y":
#             print("Winner!")
#         else:
#             print("Game over...")
#     else:
#         print("Game over...")
# else:
#     print("Game over...")
#============================DAY4============================#

#------------Random-------------

# import random
# rand_int = random.randint(1,10)
# rand_float = random.random()
# rand_dec_int = rand_float*rand_int

# print(rand_dec_int)

#------------Importing-------------
##File to import (my_module)
# import my_module
##Thing in imported file to print
# print(my_module.pi)

#-------------COIN-TOSS------------------

# import random

# coin = random.randint(1,2)

# if coin == 1:
#     print("HEADS")
# else:
#     print("TAILS")

#--------------LIST/ARRAY-----------------
# example_list = ['A','B','C','D']

# # print(example_list[0]) #Alamaba
# # print(example_list[-2]) #Samoa

# #Replace specific value at position...
# example_list[-2] = "E" 

# #Add to end of list...
# example_list.append("F")

# #Add bunch of items...
# example_list.extend(["X","Y","Z"])

# #Insert between specific position...
# example_list.insert(2,"J")

# #Remove 1st item of this value... Error if none
# try:
#     example_list.remove("A") #if found...
# except ValueError:
#     pass  # do nothing!
#     print("Not in list!")


# print(example_list)

#--------Name Picker Challenge-------
# people = input("Give list of names seperated by a comma: \n").split(", ")
# #people = ["Bob","Sally","Cody"]

# import random
# ran_num = random.randint(0, len(people)-1)
# print(people[ran_num])

#or...
# import random
# print(random.choice(people))

#-------------nested list------------------
# fruits = ["Strawberrys"]
# vegitables = ["Kale"]
# nest_list = [fruits,vegitables]

#---------Treasure map challenge----------
# row1 = [" ", " ", " "]
# row2 = [" ", " ", " "]
# row3 = [" ", " ", " "]

# map = [row1,row2,row3]

# print(f'   1    2    3\n1{row1}\n2{row2}\n3{row3}\n')

# user_input = input("Where do you want to put the treasure...? \n")

#---code below...
# y = int(user_input[1])-1 #PICKS COLUMN
# x = int(user_input[0])-1 #PICKS SLOT
# map[y][x] = "X" #Replace at this row&item
# print(f'{row1}\n{row2}\n{row3}\n')

##OR...
# if y == 1:
#     row1[x] = 'X'
# elif y ==2:
#     row2[x] = 'X'
# elif y == 3:
#     row3[x] = 'X'
# else:
#     print("invalid nums...")

# print(f'{row1}\n{row2}\n{row3}\n')



#---------ROCK PAPER SCISSORS CHALLENGE--------------
# import random
# #input is your choice, random is bot's choice...
# choices = input("Pick 0 for rock, 1 for paper, 2 for scissors: ")+str(random.randint(0,2))
# outcomes = [['02','10','21'], ['01','12','20',]]
# ascii_hand = [
# """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """,
# """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """,
# """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
# ]

# if choices in outcomes[0]:
#     print(f'''
#     WON!:{choices}
#     YOU:
#     {ascii_hand[int(choices[0])]}
#                  VS.
#     {ascii_hand[int(choices[1])]}
#     BOT:
#     ''')
# elif choices in outcomes[1]:
#         print(f'''
#     LOST!:{choices}
#     YOU:
#     {ascii_hand[int(choices[0])]}
#                  VS.
#     {ascii_hand[int(choices[1])]}
#     BOT:
#     ''')
# else:
#     print(f"DRAW....\n {choices}")

#============================DAY4============================#

#-------------LOOPS------------------
#FOR LOOP
# for item in list:
#   do something

# fruits = ["Apple", "Orange", "Pear"]

# for fruit in fruits:
#     print(fruit)


#-------------Average height----------
# heights = [180,124,165,173,189,169,146]
# heights_sum = 0
# heights_length = len(heights)

# for height in heights:
#     heights_sum += height

# average_height = round((heights_sum)/heights_length)

# print(average_height)

#--------MAX AND MIN--------------
#FINDS HIGHEST/LOWEST VALUE IN ARRAY
# scores = [180,124,165,173,189,169,146]
# current_score = scores[0]
# for score in scores:
#     if score < current_score:
#         current_score = score
# print(current_score)

#OR...
# print(max(scores))
# print(min(scores))

#-------FOR LOOP WITH RANGE--------
#          range(start,end,"step")
# Step will skip by that number to next
# always make end +1 to keep range where you want
# for num in range(1,11,3):
#     print(num) #1,4,7,10

#-----Add even nums challenge---
# answer = 0
# for num in range(2,101,2):
#     answer += num
# print(answer)

#-----------FIZZ BUZZ challenge
# for num in range(1,11):
#     if num % 2 == 0 and num % 5 == 0:
#         print(f"FIZZBUZZ")
#     elif num % 2 == 0:
#         print(f"FIZZ")
#     elif num % 5 == 0:
#         print(f"BUZZ")
#     else:
#         print(f"NA")

#-------------PASSWORD CHALLENGE------------------
# import random
# #[final password,num,letters,symbols,temp-cache]
# choices = [
#     '',
#     int(input("# of numbers?")),
#     int(input("# of letters?")),
#     int(input("# of symbols?")),
#     []]
# #DATABASE
# database = [
#     list('qwertyuioplkjhgfdsazxcvbnm'),
#     list('!@#$%^&*?'),
#     list('0123456789')]

# #NUMBERS
# for choice in range(0, choices[1]):
#     choices[4].append(random.choice(database[2]))
# #LETTERS
# for choice in range(0, choices[2]):
#     choices[4].append(random.choice(database[0]))
# #SYMBOLS
# for choice in range(0, choices[3]):
#     choices[4].append(random.choice(database[1]))
# #SHUFFLE CACHE ARRAY, THEN ADD TO PASSWORD STR
# random.shuffle(choices[4])
# for x in choices[4]:
#     choices[0] += x
# #FINAL PASSWORD
# print(choices[0])

#==================DAY6=============================
#-------------FUNCTIONS-WHILE LOOPS------------------

# #Function, def => DEFINE
# def my_function(word):
#     print(word)

# #Call function
# for fun in range(3):
#     my_function("Hello world!")

#-------------FOR & WHILE LOOPS------------------
# list_of_items = [item1,item2,item3]
# for item in list_of_items:
#     print(item)

# for something in range(a,b):
#     print(num)

# while something_is_true:
#     do something repeatedly

# test = False
# while test != True:
#     test = True
# print("test!!")

#Or...
# while not something:
#     do this...

#====================DAY7======================#
#-------------HANGMAN------------------
# import random
# secret_word = list('test')
# guesses = []
# current_guess = ''
# chances_left = 6
# points_to_win = 0
# hangman_pics = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']
# current_hangman = 0
# current_blanks = []
# for item in secret_word: 
#     current_blanks.append('_')

# #make function for making guesses
# def make_guess():
#     global secret_word, guesses, current_guess, chances_left,points_to_win, current_hangman, current_blanks
#     print(f"{hangman_pics[0]} \n {current_blanks}")
#     while chances_left > 0:
#         current_guess = input("Guess a letter: ")
#         if check_repeat() == True:
#             print(f"Already guessed this! PAST GUESSES: {guesses}")
#         elif check_repeat() == False:
#             guesses.append(current_guess)
#             if check_match() == True:
#                 answer_right()
#             elif check_match() == False:
#                 answer_wrong()
#         if points_to_win >= len(secret_word):
#             game_end()
#     game_end()
# #Make sure no repeat guesses
# def check_repeat():
#     global secret_word, guesses, current_guess, chances_left,points_to_win    
#     if current_guess in guesses:
#             return True
#     elif current_guess not in guesses:
#         return False
# #Check if new guess matches secret word
# def check_match():
#     global secret_word, guesses, current_guess, chances_left,points_to_win    
#     if current_guess in secret_word:
#         return True
#     elif current_guess not in secret_word:
#         return False
# #If right answer...
# def answer_right():
#     global secret_word, guesses, current_guess, chances_left,points_to_win, current_hangman, current_blanks
#     for i in secret_word:
#         if current_guess == i:
#             current_blanks[secret_word.index(i)] = i
#             points_to_win += 1
#     print(f"RIGHT!")
# #if wrong answer...
# def answer_wrong():
#     global secret_word, guesses, current_guess, chances_left,points_to_win    
#     chances_left -= 1
#     print(f"{hangman_pics[-6+chances_left]} \n")
#     print("WRONG!")
# #How game ends
# def game_end():
#     global secret_word, guesses, current_guess, chances_left,points_to_win   
#     if points_to_win == len(secret_word):
#         print("WINNER!")
#     elif chances_left <= 0:
#         print("LOST!")
# #Call make guess function
# make_guess()

#==============================DAY8=====================================#
#-------------function arguments (inputs)------------------
# Paramater = argument
# something = 'Daniel'
# def greet(z):
#     print(f"Hey,{z}1")
#     print(f"Hey,{z}2")
#     print(f"Hey,{z}3")
# greet(something)

# def greet_with(name,location):
#     print(f"Hello, {name}! \nWhat's it like in {location}?")
# greet_with("Daniel", "USA")

# def example_func(a,b,c):
#     print(f"{a}{b}{c}")
# example_func(c=3,b=2,a=1)

#-------------paint wall challenge------------------
#math to round up to ceiling
# import math
# def paint_wall(a,b):
#     cans = ((a*b)/5)
#     print(math.ceil(cans))
# paint_wall(7,13)

#-------------prime number checker------------------
#Prime # = any number that can't be broken down further by division...
# def prime_num(num):
#     is_prime = True

#     for n in range(2,num):
#         if num % n == 0:
#             is_prime = False

#     if is_prime == True:
#         print("PRIME")
#     else:
#         print("NOT PRIME")
# prime_num(3)
# prime_num(4)
# prime_num(5)


#-------------CEASAR CIPHER CHALLENGE------------------
# alphabet = list('abcdefghijklmnopqrstuvwxyz')
# message = [list(input("Give a message: ")),[],'']
# shift = int(input("Give a number: "))

# def message_index():
#     for m in message[0]:
#         for a in alphabet:
#             if m == a:
#                 message[1].append(alphabet.index(a))

# def scrambler():
#     alphabet.append(alphabet.pop(0))

# def ceaser_cipher():
#     global message, shift, alphabet
#     message_index()
#     while shift >= 1:
#         scrambler()
#         shift -= 1
#     for idx in message[1]:
#         message[2] += alphabet[idx]
#     print(f"Your scrambled message is now: {message[2]}")

# ceaser_cipher()

#================================DAY9==================================================#
#-------------Dictionaries------------------
#{KEY:VALUE, KEY:VALUE,KEY:VALUE}
# dictionary = {
#     "a":"1", 
#     "b":"2", 
#     "c":"3"
# }

# print(dictionary)
# print(dictionary.items())
# print(dictionary.values())
# print(dictionary["b"])
# print(dictionary[3])
# dictionary[4] = "d"
# dictionary = {}
# print(dictionary)

#To get keys...
# for key in dictionary:
#     print(f"{key}=>{dictionary[key]}")

#-------------grading challenge------------------
# student_scores = {
#     "Harry":80,
#     "Ron":14,
#     "Hermiony":92,
#     "Draco":93,
#     "Headwig":100
# }

# def get_student_grades():
#     for student in student_scores:
#         student_scores[student]
#         if student_scores[student] >= 90:
#             print(f"{student} scored an A!!!")
#         elif student_scores[student] >= 80:
#             print(f"{student} scored an B!")
#         elif student_scores[student] >= 70:
#             print(f"{student} scored an C.")
#         elif student_scores[student] >= 60:
#             print(f"{student} scored an D...?")
#         else:
#             print(f"{student} scored an F...")

# get_student_grades()


#-------------nesting------------------
# test = {
#     'key1':['1','2','3'],
#     'key2':{'a':'X','b':'Y','c':'Z'}
# }

#-------------country dictionaries challenge------------------
# travel_log = [
#     {
#         'country':'America',
#         'visits':50,
#         'cities':['Los Angeles','Houson','El Paso']
#     }
# ]

# def add_log(country,visits,cities):
#     global travel_log
#     new_country = {}
#     new_country['country'] = country
#     new_country['visits'] = visits
#     new_country['cities'] = cities
#     travel_log.append(new_country)
#     for key in travel_log:
#         print(key)

# add_log('Australia',1,['Canberra','Sydney'])

#-------------BLIND AUCTION CHALLENGE------------------
# users = []
# winner = ''

# def get_info():
#     global users
#     winner = 0
#     winner_name = ''
#     username = input("Username? ")
#     bid = int(input("Bid? "))

#     new_user = {}
#     new_user['username'] = username
#     new_user['bid'] = bid
#     users.append(new_user)

#     other_users = input("Are there other players (y/n)? ")

#     if other_users == 'y':
#         get_info()
#     elif other_users == 'n':
#         for user in users:
#             if user['bid'] > winner:
#                 winner = user['bid']
#                 winner_name = user['username']
#         print(winner_name)

# get_info()

#============================DAY10=========================================#
#-------------Name Cap Corrector------------------

# def format_name(full_name):
#     full_name = full_name.split(' ')
#     new_name = ''
#     for name in full_name:
#         cache = name[0].upper()
#         for letter in range(1,len(name)):
#             cache += name[letter].lower()
#         new_name += cache+" "
#     return new_name
# print(format_name("JOHN MCLANE"))
# print(format_name("boB jELlY"))
# print(format_name("bob boBert"))

#OR...

# f_name = "anGela"
# print(f_name.title())

#-------------CALCULATOR------------------
#FIRST NUMBER
#OPERATOR
#SECOND NUMBER
#CONTINUE (Y/N)? => REPEAT OPERATOR,2ND NUM
#START OVER

# def calculator():
#     num1 = int(input("What's the first number? "))
#     repeat = True
#     while repeat == True:
#         operator = input("Pick the operator (+,-,*,/)? ")
#         num2 = int(input("What is the 2nd number? "))
#         if operator == "+":
#             num1 = num1 + num2
#             continue_calc = input("Continue (y/n)? ")
#         if continue_calc == 'y':
#             repeat = True
#         elif continue_calc == 'n':
#             repeat = False
#     return num1

# calculator()


# import operator
# ops = {
# '+' : operator.add,
# '-' : operator.sub,
# '*' : operator.mul,
# '/' : operator.truediv, 
# }
# # print(ops["+"](1,1)) #TEST

# def calculator():
#     num1 = int(input("Pick a number: "))
#     repeat_calc = True

#     while repeat_calc == True:
#         #Gather info
#         current_op = str(input("Pick operator(+,-,/,*): "))
#         num2 = int(input("Pick 2nd number: "))
#         #Run calculation
#         num1 = round(ops[current_op](num1,num2))
#         print(num1)
#         #Continue?
#         if input("Keep calculating(y/n)? ") == 'y':
#             repeat_calc = True
#         else:
#             repeat_calc = False
     

# calculator()

#-------------BLANK------------------
#-------------BLANK------------------
#-------------BLANK------------------
#-------------BLANK------------------
#-------------BLANK------------------: