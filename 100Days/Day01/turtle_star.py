import turtle as t

t.speed(1)#画笔速度0-10

def drawStar(x,y):

    t.pu()#t.up()画笔抬起
    t.goto(x,y)
    t.pd()#画笔落下
    #set heading:0
    t.seth(0)#设置朝向
    for i in range(5):
        t.fd(40)
        t.rt(144)

for x in range(0,250,50):
    drawStar(x,0)

t.done()

# import turtle as t
# t.pencolor('black')
# t.fillcolor('red')
#
# t.begin_fill()
# for i in range(5):
#     t.fd(200)
#     t.rt(144)
# t.end_fill()
# t.done()

# import turtle as t
#
# t.fillcolor('red')
# t.hideturtle()
# t.begin_fill()
# while True:
#     t.fd(200)
#     t.rt(144)
#     if abs(t.pos())<1:
#         break
# t.end_fill()
# t.done()

'''
turtle.speed(speed-None)
参数：0-10整型或速度字符串
fastest：0
fast：10
normal：6
slow：3
slowest：1

turtle.penup()
turtle.pu()
turtle.up()
画笔抬起

turtle.pendown()
turtle.pd()
turtle.down()
画笔落下

turtle.goto(x,y=None)
turtle.setpos(x,y=None)
turtle.setposition(x,y=None)
位置
参数：
x-一个数值或数值对/向量
y-一个数值或None

turtle.setheading(to_angle)
turtle.seth(to_angle)
朝向
参数：
to_angle-一个数值，整型或浮点型
0-东
90-北
180-西
270-南

turtle.forward(distance)
turtle.fd(distance)
前进
参数：
distance-一个数值，整型或浮点型

turtle.right(angle)
turtle.rt(angle)
右转

turtle.left()
turtle.lt()
左转
'''
