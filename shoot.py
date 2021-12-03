import turtle

class Bullet(turtle.Turtle):

    def __init__(self,coords):
        super().__init__()
        self.coords = coords
        self.shoot()

    def shoot(self):

        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(self.coords)
        self.color("white")
        self.shape("circle")

    def move_forward(self):
        if self.ycor() < 200:
            self.sety(self.ycor()+25)
        else:
            self.hideturtle()


