import turtle
from tinydb import TinyDB, Query


class Score_Board(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(-85,200)
        self.hideturtle()
        self.write(f"Score: {self.score}")

    def increase_point(self):
        self.clear()
        self.score += 50
        self.write(f"Score: {self.score}")

    def decrease_point(self):
        self.clear()
        self.score -= 25
        self.write(f"Score: {self.score}")

class Title(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-90,220)
        self.hideturtle()
        self.color("white")
        self.write("SPACE INVADERS",font=("Verdana",15, "normal"))

class Prompt(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-80, 0)
        self.write("Press [t] to begin",font=("Verdana",15, "normal"))


class Success(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-60, 20)
        self.write("You Win",font=("Verdana",15, "normal"),move=False)
        self.goto(-80, -50)
        self.write("Press [t] to play again", font=("Verdana",10, "normal"),move=False)

class Highscore(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(25,200)
        self.hideturtle()
        self.score = 0
        self.db = TinyDB("highscore.json")
        try:
            self.score = (self.db.search(Query().type == "HS"))[0]["score"]
            self.write(f"Highscore: {self.score}")
            print("found db score")

        except:
            print("no current highscore, creating new one")
            self.db.insert({'type':"HS","score":100})
            self.write(f"Highscore: {self.score}")

    def update_highscore(self, score):
        print(score, self.score)
        if score > self.score:
            print('updating')
            self.db.update({'score':score}, Query().type == "HS")
        # self.db.insert({"type":"HS","score": score})
        # self.clear()
        # self.write(f"Highscore: {self.score}")








