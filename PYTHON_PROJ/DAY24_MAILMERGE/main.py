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

# with open('./Input/Letters/starting_letter.docx') as letter:
#     contents = letter.read()
#     print(contents)









with open('./Input/Letters/starting_letter.docx','r') as letter:
    # ARAY OF NAMES
    names_array = open('./Input/Names/invited_names.txt','r').readlines()

    # GET ARAY OF EACH LINE OF LETTER
    let_array = letter.readlines()

    for name in names_array:
        # CHANGE INTRO
        idx = names_array.index(name)
        let_array[0] = let_array[0].replace("[name]", names_array[idx])

        # GENERATE LETTER
        with open('./Output/ReadyToSend/new_letter.txt',mode='w') as file:
            for line in let_array:
                file.write(line)





