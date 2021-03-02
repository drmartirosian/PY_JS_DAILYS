#PYTHON100

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
# pet = (input("What is your pet? "))
# city = (input("What is your home street? "))
# print("Your 'online' name could be "+pet+" "+city+"!")

#=====================DAY-2=============================#

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
bill = round(float(input("What was the bill? ")),2)
percent = bill * (int(input("Percentage tip? 10, 12, or 15? ")) / 100)
num_people = int(input("How many people splitting bill? "))
final_bill = round(((bill + percent) / num_people), 2)
print(f"Each person should pay: ${final_bill}")
# --------------------------------------
