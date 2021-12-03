import turtle

class Player:

    def __init__(self):
        self.pieces = []
        self.create_pieces()
        self.x = (self.pieces[0].xcor()+ self.pieces[1].xcor())/2

    def create_pieces(self):
        # creating the pieces that make up the player
        for x in range(-10,11,10):
            piece = turtle.Turtle()
            piece.penup()

            piece.color("white")
            piece.shape('square')
            piece.hideturtle()
            piece.goto(((0-x),-150))
            piece.showturtle()
            self.pieces.append(piece)
    def get_current_x(self):
        # to be used for deciding where to shoot
        self.x = (self.pieces[0].xcor()+ self.pieces[1].xcor())/2
        return self.x


    def move_left(self):
        for x in self.pieces:
            x.goto((x.xcor()-20,x.ycor()))

    def move_right(self):
        for x in self.pieces:
            x.goto((x.xcor()+20, x.ycor()))


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
        # if self.ycor() < 200:
        self.sety(self.ycor()+25)
        # else:
        #     self.hideturtle()

