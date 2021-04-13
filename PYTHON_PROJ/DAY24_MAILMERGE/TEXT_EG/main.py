# file = open ('data.txt') #open file for use
# contents = file.read() #read out contents of txt file
# print(contents)
# file.close() #close to stop using up CPU resources 

#OR...
# with open ('data.txt',mode='a') as file: #mode=(r)ead,(w)rite,(a)ppend
#     # contents = file.read() #read out contents of txt file
#     # print(contents)
#     file.write('\nThe cake is a lie!')

# #GENERAT ENEW TXT FILES
# with open('new_file.txt',mode='w') as file:
#     file.write("\nThe cake is a lie.")

#PARTICULAR ADDRESS LOCATION
with open('../test.txt') as file:
    contents = file.read()
    print(contents)

