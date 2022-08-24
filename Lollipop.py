#lollipop drawing

from turtle import*
bgcolor('black')
setup(430,768)
speed(0)
shape("circle")
c=["red","orange","yellow","green","blue","indigo","violet"]
up()
seth(-90)
fd(380)
down()
color('white')
pensize(15)
seth(90)
fd(400)
up()
fd(160)
down()
seth(0)
for i in range(700):
 color(c[i%7])
 shapesize(0.2+(i/490))
 up()
 fd(3+(i/5))
 down()
 stamp()
 rt(51.991)


done()
