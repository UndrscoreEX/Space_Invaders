import turtle

import scoreboard
from player import Player, Bullet
from aliens import Alien, AlienBullet
from scoreboard import Score_Board, Title, Prompt, Success, Highscore
import time
import random

rand = [x for x in range(1,21)]

game = True
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')
wn.screensize(canvwidth=300, canvheight=400)
wn.setup(width=400,height=500)
wn.tracer(0)

def start_game():
    # wn.resetscreen()
    wn.clearscreen()
    prep()
    prompt.clear()

    # aliens_pos = []
    global on_screen_bullets
    on_screen_bullets = []
    alien_bullet_count = []
    aliens_pos = aliens.alien_group

    game = True

    while game:
        print(len(aliens_pos))
        turtle.update()
        time.sleep(0.05)
        if len(aliens_pos) <1:
            game = False
            success()
            break

        # Shooting from the aliens:
        if random.choice(rand) == 1 and len(alien_bullet_count)<4:

            chosen = random.choice(aliens_pos)
            a_bullet = AlienBullet(chosen.pos())
            alien_bullet_count.append(a_bullet)

        # removing spent bullets:
        for bullet in on_screen_bullets:
            if bullet.ycor() > 220:
                bullet.hideturtle()
                on_screen_bullets.pop(on_screen_bullets.index(bullet))
                score.decrease_point()

            bullet.move_forward()

        # alien bullets
        for ab in alien_bullet_count:
            if ab.ycor()< -180:
                ab.hideturtle()
                alien_bullet_count.pop(alien_bullet_count.index(ab))
            if ab.distance(player.pieces[0])< 20 or ab.distance(player.pieces[1])< 20 :
                gameover()
                game = False
                break
            ab.bullet_move()
        for ap in aliens_pos:
            if ap.ycor()< -150:
                gameover()
                game = False
                break
            for bullet in on_screen_bullets:
                if ap.distance(bullet)< 20:
                    print("hit")
                    ap.hideturtle()
                    bullet.hideturtle()
                    aliens_pos.pop(aliens_pos.index(ap))
                    on_screen_bullets.pop(on_screen_bullets.index(bullet))
                    aliens.speed_level +=0.1
                    score.increase_point()
        wn.onkey(key='Left', fun=player.move_left)
        wn.onkey(key='Right', fun=player.move_right)
        wn.onkey(key='space', fun=shoot)
        aliens.start_moving()


def shoot():
    if len(on_screen_bullets)<4:
        coords = (player.get_current_x(),-150)
        print(coords)
        blt = Bullet(coords=coords)
        on_screen_bullets.append(blt)


def gameover():
    # print("score is :::: ",score.score)
    highscore.update_highscore(score.score)
    global game
    game = False
    wn.resetscreen()
    goScreen = turtle.Turtle()
    goScreen.penup()
    goScreen.hideturtle()
    goScreen.color("white")
    goScreen.goto(-90,0)
    goScreen.write("GAME OVER",font=("Verdana",20, "normal"), move=False)
    goScreen.goto(-50,-20)
    goScreen.write("press [t] to restart")

def prep():
    turtle.resetscreen()
    global score
    score = Score_Board()
    global player
    player = Player()
    global highscore
    highscore = Highscore()
    global title
    global aliens
    title = Title()
    aliens = Alien()
    turtle.update()

def success():
    wn.resetscreen()
    succ = Success()



wn.listen()
wn.onkey(key="t",fun=start_game)
# wn.onkey(key="space" ,fun=prep)

prep()
global prompt
prompt = Prompt()
turtle.done()