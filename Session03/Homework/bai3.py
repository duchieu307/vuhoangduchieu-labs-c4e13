from turtle import *

def draw_square(lenght, color):
    pencolor(color)
    for i in range(4):
        forward(lenght)
        left(90)


dai = int(input("Enter Lenght "))
mau = input("Enter pen color ")

draw_square(dai, mau)




mainloop()
