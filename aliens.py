import turtle
import time
ALIENPOS = [
    [(-120, 150), (-80, 150), (-40, 150), (0, 150), (40, 150),  (120, 150),(80,150)],
    [(-110, 170), (-70, 170), (-30, 170), (10, 170), (50, 170), (130, 170), (90, 170)],
    [(-130, 190), (-90, 190), (-50, 190), (-10, 190), (30, 190), (110, 190), (70, 190)]
            ]
ALIEN_NUM = 7

class Alien:
    def __init__(self):
        self.direction = True
        self.count = 7
        self.level = 3
        self.speed_level = 1
        self.alien_group = []
        self.create_aliens()

    def create_aliens(self):
        for y in range(0,self.level):
            for x in range(0,ALIEN_NUM):
                alien = turtle.Turtle()
                alien.penup()
                alien.goto(ALIENPOS[y][x])
                if y==0:
                    alien.color('red')
                elif y== 1:
                    alien.color("blue")
                elif y== 2:
                    alien.color("orange")
                alien.shape('square')
                alien.shapesize(stretch_wid=0.5,stretch_len=1)
                self.alien_group.append(alien)

    def start_moving(self):
        # Choosing direction (left or right)
        if self.direction:
            for aln in self.alien_group:
                # If the aliens are within the screen,
                if aln.xcor()< 180 and aln.xcor()>-180:
                    aln.forward(5 *self.speed_level)
                else:
                # if one of the alien touches the wall, direction changes and movement stops
                    self.direction = False
                    for aln in self.alien_group:
                        aln.sety(aln.ycor() - 10)
                        aln.backward(5*self.speed_level)
                    return print("change sides")
            time.sleep(0.05)


        # same thing but in the opposite direction
        if not self.direction:
            for aln in self.alien_group:
                if aln.xcor() < 180 and aln.xcor() > -180:
                    aln.backward(5*self.speed_level)
                else:
                    self.direction = True
                    for aln in self.alien_group:
                        aln.sety(aln.ycor() - 10)
                    # for y in self.alien_group:
                        aln.forward(5*self.speed_level)
                    self.speed_level +=0.1
                    return print("change sides")
            time.sleep(0.05)


class AlienBullet(turtle.Turtle):

    def __init__(self, coord):
        super().__init__()
        self.penup()
        self.goto(coord)
        self.seth(270)
        self.color("white")
        self.shape('circle')
        self.shapesize(stretch_wid=0.25, stretch_len=1)

    def bullet_move(self):
        self.forward(20)

