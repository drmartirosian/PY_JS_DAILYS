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

#-------------BLANK------------------
#-------------BLANK------------------
#-------------BLANK------------------
#-------------BLANK------------------
#-------------BLANK------------------
#-------------BLANK------------------
