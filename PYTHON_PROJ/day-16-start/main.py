# import another_module
# print(another_module.another_variable)

#CLASS
    #=> object
        #=>attributes(speed:0,fuel:32)
        #=>methods(def move(): speed = 60) aka functions tied to that object
 



import turtle
test = turtle.Turtle()
#POLYGON
for i in range(6):
    test.forward(100) #move forward 100
    test.right(300) #turn at 300 angle
#SQUARE
# for i in range(4):
#     test.forward(100)
#     test.left(90)
#CIRCLE
# for i in range(13):
#     test.forward(10)
#     test.right(30)
turtle.done()