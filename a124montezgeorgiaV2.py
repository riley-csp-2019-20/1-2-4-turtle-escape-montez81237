import turtle as trtl 
import random 

z = trtl.Turtle()
z.shape("turtle")
z.color("red")
m = trtl.Turtle()
m.speed(0)
m.pensize(5)
m.ht()
count = 250 
wall_width = 8
door_width = 22
z.goto(0,-10)
def z_up():
    z.setheading(90)
    z.forward(10)
def z_down():
    z.setheading(270)
    z.forward(10)
def z_left():
    z.setheading(180)
    z.forward(10)
def z_right():
    z.setheading(0)
    z.forward(10)
for i in range(25):

    if i < 20:
        door = random.randint(wall_width, count - door_width*2)
        barrier =  random.randint(wall_width, count - door_width*2)
        if door < barrier:
                
            m.forward(door)
            m.penup()
            m.forward(door_width)
            m.pendown() 
            m.forward(barrier - door - door_width)
            

            m.right(90)
            m.forward(wall_width*2)
            m.back(wall_width*2)
            m.left(90)
            
            m.forward(count - barrier)


        else:
            m.forward(barrier)

            m.right(90)
            m.forward(wall_width*2)
            m.backward(wall_width*2)
            m.left(90)

            m.forward(door - barrier)
            m.penup()
            m.forward(door_width)
            m.pendown()

            m.forward(count - door - door_width)
        
        

    m.right(90)
    count = count - wall_width







wn = trtl.Screen()
wn.onkeypress(z_up,"Up")
wn.onkeypress(z_down,"Down")
wn.onkeypress(z_left,"Left")
wn.onkeypress(z_right,"Right")
wn.listen()
wn.mainloop()
