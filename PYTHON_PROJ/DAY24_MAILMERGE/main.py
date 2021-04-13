# TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# #Hint1 READLINES(): This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# f = open("demofile.txt", "r")
# print(f.readlines())

# #Hint2 REPLACE(): This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# txt = "I like bananas"
# x = txt.replace("bananas", "apples") #replacea with b
# print(x)

# #Hint3 STRIP(): THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# txt = "     banana     "
# x = txt.strip() #removes spaces beind/infront of
# print("of all fruits", x, "is my favorite")


PLACEHOLDER = '[name]'
# LIST OF NAMES
with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

#ARRAY BROKEN INTO LIST
with open('./Input/Letters/starting_letter.docx') as letter_file:
    letter_contents = letter_file.read()
    #Loop thru names
    for name in names:
        #removes \n after each name
        stripped_name = name.strip() 
        # Swap [name] out with each name in list
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
        #Write new letters with new_letter for their contents
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.docx',mode='w') as completed_letter:
            completed_letter.write(new_letter)