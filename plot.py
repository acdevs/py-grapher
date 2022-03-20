import turtle as T
import math as m
t=T.Turtle()
r=T.Turtle()
t.hideturtle()
r.hideturtle()
t.speed(0)
r.speed(0)
t.pensize(1)
t.fd(500)
t.goto(0,0)
t.lt(90)
t.fd(500)
t.goto(0,0)
t.lt(180)
t.fd(500)
t.goto(0,0)
t.rt(90)
t.fd(500)
t.goto(0,0)
t.home()
t.speed(0)
t.pensize(1)
r.pensize(1)
##How many pixels as 1 unit of X-axis:
xU=50
##How many pixels as 1 unit of Y-axis:
yU=50
#Mark Axis...
wx=T.Turtle()
wx.penup()
wx.hideturtle()
wx.pensize(1)
wx.speed(0)
wy=wx.clone()
if xU<=10:
    fs=6
elif xU<=20:
    fs=8
else:
    fs=10
for i in range(xU,500,xU):
    wx.setpos(i,-15)
    n=f'{i//xU}'
    wx.write(n,font=('Arial',fs,'normal'))
    wx.setpos(i,0)
    wx.dot(3,'black')
    wx.setpos(-i,-15)
    n=f'{-i//xU}'
    wx.write(n,font=('Arial',fs,'normal'))
    wx.setpos(-i,0)
    wx.dot(3,'black')
for i in range(yU,500,yU):
    wy.setpos(-15,i)
    n=f'{i//yU}'
    wy.write(n,font=('Arial',fs,'normal'))
    wy.setpos(0,i)
    wy.dot(3,'black')
    wy.setpos(-20,-i)
    n=f'{-i//yU}'
    wy.write(n,font=('Arial',fs,'normal'))
    wy.setpos(0,-i)
    wy.dot(3,'black')

#MAIN FUNCTION IS HERE...
def f(x):
    x/=xU
    #Main Function...
    y=x-m.floor(x)
    y*=yU
    return y
##def g(x):
##    x/=xU
##    #Main Function...
##    y=m.tan(x)   
##    y*=yU
##    return y
#Mark the points...
##tg=t.clone()
##rg=r.clone()
for x in range(1,400,10):
    t.setpos( x,f( x))
    r.setpos(-x,f(-x))
##    tg.setpos( x,g( x))
##    tg.dot(3,'blue')
##    rg.setpos(-x,g(-x))
##    rg.dot(3,'blue')
