import turtle as t

#设置色彩模式RGB
t.colormode(255)

t.lt(90)

lv=14
l=120
s=45

t.width(lv)

#初始化RGB颜色
r=0
g=0
b=0
t.pencolor(r,g,b)

t.penup()
t.bk(l)
t.pendown()
t.fd(l)

def draw_tree(l,level):
    global r,g,b
    #save the current pen width
    w=t.width()

    #narrow the pen width
    t.width(w*3.0/4.0)
    #set color
    r=r+1
    g=g+2
    b=b+3
    t.pencolor(r%200,g%200,b%200)

    l=3.0/4.0*l

    t.lt(s)
    t.fd(l)

    if level<lv:
        draw_tree(l,level+1)
    t.bk(l)
    t.rt(2*s)
    t.fd(l)

    if level<lv:
        draw_tree(l,level+1)
    t.bk(l)
    t.lt(s)

    #restore the previous pen width
    t.width(w)

t.speed("fastest")
draw_tree(l,4)
t.done()



