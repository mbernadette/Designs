import turtle

# Draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.pensize(5)
    turtle.color(0.27, 0.51, 0.71) # Steel Blue
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Write a string s at the specified location (x, y)
def writeText(s, x, y):
    turtle.pensize(1)
    turtle.color(0.28, 0.24, 0.55) # Dark Slate Blue
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(s, align="center", font=("Times", 15, "italic"))

# Draw a point at the specified location (x, y)
def drawPoint(x, y):
    turtle.pensize(2)
    turtle.color(0.58, 0.0, 0.83) # Dark Violet
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

# Draw a circle centered at (x, y) with the specified radius
def drawCircle(x = 0, y = 0, radius = 10, mycolor = (0.49, 0.99, 0.00)): # Lawn Green
    turtle.pencolor(mycolor[0], mycolor[1], mycolor[2])
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

# Draw a rectangle at (x, y) with the specified width and height
def drawRectangle(x = 0, y = 0, width = 10, height = 10):
    turtle.pensize(2)
    turtle.color(0.60, 0.98, 0.60) # Pale Green
    turtle.penup()
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown()
    turtle.circle(30, 90)
    turtle.forward(height)
    turtle.circle(30, 90)
    turtle.forward(width)
    turtle.circle(30, 90)
    turtle.forward(height)
    turtle.circle(30, 90)
    turtle.forward(width)

# Draw an outline of a flower using 5 circles
def drawFlower(xCenter = 0, yCenter = 0, xRightUp = 0, yRightUp = 0,
    xRightDown = 0, yRightDown = 0, xLeftUp = 0, yLeftUp = 0,
    xLeftDown = 0, yLeftDown = 0, radius = 10):
    turtle.pensize(3)
    turtle.color(1.0, 0.41, 0.70) # Hot Pink
    turtle.penup()
    turtle.goto(xCenter, yCenter - radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(xRightUp, yRightUp - radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(xRightDown, yRightDown - radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(xLeftUp, yLeftUp - radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(xLeftDown, yLeftDown - radius)
    turtle.pendown()
    turtle.circle(radius)

# Fill in the flower
def fillFlower(xRightUp = 0, yRightUp = 0, xRightDown = 0, yRightDown = 0,
    xLeftUp = 0, yLeftUp = 0, xLeftDown = 0, yLeftDown = 0,
    xCenter = 0, yCenter = 0, radius = 10):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(xRightUp, yRightUp - radius)
    turtle.pendown()
    turtle.pencolor(0.86, 0.44, 0.58) # Pale Violet Red
    turtle.fillcolor(0.69, 0.77, 0.87) # Light Steel Blue
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(xRightDown, yRightDown - radius)
    turtle.pendown()
    turtle.pencolor(0.86, 0.44, 0.58) # Pale Violet Red
    turtle.fillcolor(0.69, 0.77, 0.87) # Light Steel Blue
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(xLeftUp, yLeftUp - radius)
    turtle.pendown()
    turtle.pencolor(0.86, 0.44, 0.58) # Pale Violet Red
    turtle.fillcolor(0.69, 0.77, 0.87) # Light Steel Blue
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(xLeftDown, yLeftDown - radius)
    turtle.pendown()
    turtle.pencolor(0.86, 0.44, 0.58) # Pale Violet Red
    turtle.fillcolor(0.69, 0.77, 0.87) # Light Steel Blue
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(xCenter, yCenter - radius)
    turtle.pendown()
    turtle.pencolor(0.28, 0.24, 0.55) # Dark Slate Blue
    turtle.fillcolor(0.86, 0.44, 0.58) # Pale Violet Red
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def drawLeaf(x = 0, y = 0):
    turtle.pensize(5)
    turtle.pencolor(0.20, 0.80, 0.20) # Lime Green
    turtle.fillcolor(0.50, 1.0, 0.83) # Aquamarine
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30, steps = 3)
    turtle.end_fill()

# Turtle setup
turtle.setup(1300, 700)
turtle.speed(0)
turtle.bgcolor(0.0, 0.0, 0.0) # Black

# Turtle drawing calling above functions
drawCircle(-100, 150, 20, mycolor = (0.86, 0.44, 0.58)) # Pale Violet Red
drawCircle(-50, 100, 20, mycolor = (0.86, 0.44, 0.58))
drawCircle(-150, 100, 20, mycolor = (0.86, 0.44, 0.58))
drawCircle(-100, 50, 20, mycolor = (0.86, 0.44, 0.58))

drawFlower(-100, 100, -80, 120, -80, 80, -120, 120, -120, 80, 20)

drawLine(-100, 170, -100, 220)
drawLine(-30, 100, 20, 100)
drawLine(-170, 100, -220, 100)
drawLine(-100, 30, -100, -20)

turtle.setheading(225)
drawRectangle(-75, 50, 10, 30)
turtle.setheading(315)
drawRectangle(-70, 115, 10, 30)
turtle.setheading(135)
drawRectangle(-140, 55, 10, 30)
turtle.setheading(45)
drawRectangle(-135, 120, 10, 30)

turtle.setheading(180)
drawRectangle(-111, 245, 10, 30)
turtle.setheading(360)
drawRectangle(-99, -75, 10, 30)
turtle.setheading(90)
drawRectangle(-175, 89, 10, 30)
turtle.setheading(90)
drawRectangle(55, 91, 10, 30)

turtle.setheading(360)
drawLeaf(-100, 220)
turtle.setheading(270)
drawLeaf(20, 100)
turtle.setheading(90)
drawLeaf(-220, 100)
turtle.setheading(180)
drawLeaf(-100, -20)

drawPoint(-50, 60)
drawPoint(-50, 150)
drawPoint(-150, 60)
drawPoint(-150, 150)

drawPoint(-100, 220)
drawPoint(15, 105)
drawPoint(-215, 105)
drawPoint(-100, -10)

fillFlower(20, 265, 20, 225, -20, 265, -20, 225, 0, 245, 20)
fillFlower(-180, 265, -180, 225, -220, 265, -220, 225, -200, 245, 20)
fillFlower(20, 60, 20, 20, -20, 60, -20, 20, 0, 40, 20)
fillFlower(-180, 60, -180, 20, -220, 60, -220, 20, -200, 40, 20)

drawFlower(-100, 320, -80, 340, -80, 300, -120, 340, -120, 300, 20)
drawFlower(-100, -40, -80, -20, -80, -60, -120, -20, -120, -60, 20)
drawFlower(80, 140, 100, 160, 100, 120, 60, 160, 60, 120, 20)
drawFlower(-280, 140, -260, 160, -260, 120, -300, 160, -300, 120, 20)

drawLine(35, 240, 70, 275)
drawLine(-235, 240, -270, 275)
drawLine(35, -37, 70, -72)
drawLine(-235, -37, -270, -72)

drawPoint(70, 280)
drawPoint(-270, 280)
drawPoint(75, -72)
drawPoint(-275, -72)

turtle.setheading(315)
drawLeaf(75, 280)
turtle.setheading(45)
drawLeaf(-275, 280)
turtle.setheading(225)
drawLeaf(81, -82)
turtle.setheading(135)
drawLeaf(-281, -82)

drawCircle(126, 350, 20)
drawCircle(-297, 350, 20)
drawCircle(132, -85, 20)
drawCircle(-303, -85, 20)

drawCircle(152, 133, 20)
fillFlower(280, 153, 280, 113, 240, 153, 240, 113, 260, 133, 20)

drawCircle(-322, 133, 20)
fillFlower(-400, 153, -400, 113, -360, 153, -360, 113, -380, 133, 20)

drawFlower(150, 20, 170, 40, 170, 0, 130, 40, 130, 0, 20)
fillFlower(420, -30, 420, -70, 380, -30, 380, -70, 400, -50, 20)
drawFlower(530, -100, 550, -120, 550, -80, 510, -80, 510, -120, 20)
drawFlower(220, -180, 220, -220, 180, -180, 180, -220, 200, -200, 20)
fillFlower(470, -230, 470, -270, 430, -230, 430, -270, 450, -250, 20)

drawPoint(200, 40)
drawPoint(450, -100)
drawPoint(150, -150)
drawPoint(350, -250)
drawPoint(300, 20)
drawPoint(400, -200)
drawPoint(500, -300)
drawPoint(550, -350)
drawPoint(580, -250)

writeText("love...", 320, 90)
writeText("knots...", 215, -25)
writeText("love...", 465, -90)
writeText("knots...", 590, -145)
writeText("knots...", 265, -240)
writeText("love...", 510, -290)

turtle.hideturtle()
turtle.done()