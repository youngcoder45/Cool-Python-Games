import turtle
import winsound
import os
import math
import random
import tkinter as tk
from tkinter import messagebox as msg
from turtle import TurtleScreen, RawTurtle
import time
# Creating GUI
win = tk.Tk()
win.geometry("800x750")
win.resizable(width=False, height=False)
win.title("-----Space Invader-----")
win["bg"] = "#180833"


def start():
    canvas = tk.Canvas(win, width=750, height=650)
    canvas.place(x=20, y=10)
    wn = TurtleScreen(canvas)
    wn.bgcolor("blue")
    # Register the Shapes
    wn.register_shape("E:\\Aditya_Verma\\Python_Programming\\Games\\newbg.gif")
    # wn.register_shape("C:\\Users\\varma\\Desktop\\Games\\spaceship.gif")
    # wn.register_shape("C:\\Users\\varma\\Desktop\\Games\\alien.gif")
    #wn.register_shape("C:\\Users\\varma\\Desktop\\Games\\GameOver.gif")
    wn.bgpic("E:\\Aditya_Verma\\Python_Programming\\Games\\newbg.gif")
    score = 0
    score_pen = RawTurtle(wn)
    score_pen.speed(0)
    score_pen.color("yellow")
    score_pen.penup()
    score_pen.setposition(-370, 290)
    scorestring = "score:%s" % score
    score_pen.write(scorestring, False, align="left",
                    font=("Arial", 14, "normal"))
    score_pen.hideturtle()
    # Create the Player Turtle
    player = RawTurtle(wn)
    # player.shape("C:\\Users\\varma\\Desktop\\Games\\spaceship.gif")
    player.shape("turtle")
    player.shapesize(3.0,3.0)
    player.color("red")
    player.penup()
    player.speed(0)
    player.setposition(0,-250)
    player.setheading(90)
    playerspeed=25
    #create enemies
    number_of_enemies=10
    enemies=[]
    #add enemies to the list
    for i in range(number_of_enemies):
        enemies.append(RawTurtle(wn))
    for enemy in enemies:
        enemy.shape("classic")
        enemy.setheading(270)
        enemy.shapesize(3.0,3.0)
        enemy.color("green")
        enemy.penup()
        enemy.speed(0)
        x=random.randint(-200,200)
        y=random.randint(100,250)
        enemy.setposition(x,y)
        enemyspeed=5
    #Create player's Bullet
    bullet=RawTurtle(wn)
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed()
    bullet.setheading(90)
    bullet.shapesize(1.0,1.0)
    bullet.hideturtle()
    bulletspeed=150
    #Move player to Left And Right
    def move_left():
        x=player.xcor()
        x-=playerspeed
        if x<-280:
            x=-280
            player.setx(x)
    def move_right():
        x=player.xcor()
        x+=playerspeed
        if x>280:
            x=280
            player.setx(x)
    #bullet state fix
    global bulletstate
    bulletstate="ready"
    def fire_bullet():
        global bulletstate
        if bulletstate == "ready":
            bulletstate="fire"
            #winsound.playsound("Adrees", winsound.SND_ASYNC)
            # Make Bullet TO players Top
            x=player.xcor()
            y=player.ycor()+10
            bullet.setposition(x,y)
            bullet.showturtle()
    def isCollison_enemy_bullet(t1,t2):
        distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance<35:
            return True
        else:
            return False
    def isCollison_enemy_player(t1,t2):
        distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance<100:
            return True
        else:
            return False
    #Create Keyboard
    wn.listen()
    wn.onkey(move_right,"Right")
    wn.onkey(move_left,"Left")
    wn.onkey(fire_bullet,"space")
    #Main Game LOOP
    Game_Over=False
    missed_enemies=0
    while True:
        for enemy in enemies:
            x=enemy.xcor()
            x+=enemyspeed
            enemy.setx(x)
            if enemy.xcor()>270:
                for e in enemies:
                    y=e.ycor()
                    y-=40
                    e.sety(y)
                    if e.ycor()<-285 and Game_Over==False:
                        e.hideturtle()
                        missed_enemies+=1
                        if missed_enemies==5:
                            Game_Over=True
                        x=random.randint(-200,200)
                        y=random.randint(100,250)
                        e.setposition(x,y)
                        e.showturtle()
                enemyspeed *=-1
            if enemy.xcor()<-270:
                for e in enemies:
                    y=e.ycor()
                    y-=40
                    e.sety(y)
                    if e.ycor()<-285 and Game_Over==False:
                        e.hideturtle()
                        missed_enemies+=1
                        if missed_enemies==5:
                            Game_Over=True
                        x=random.randint(-200,200)
                        y=random.randint(100,250)
                        e.setposition(x,y)
                        e.showturtle()
                enemyspeed*=-1
            if isCollison_enemy_bullet(bullet,enemy):
                time.sleep(0.05)
                #winsound.playsound("Adrees", winsound.SND_ASYNC)
                bullet.hideturtle()
                bulletstate="ready"
                bullet.setposition(0,-400)
                #reset the Enemy
                x=random.randint(-200,200)
                y=random.randint(100,250)
                enemy.setposition(x,y)
                enemyspeed+=0.5
                score+=10
                scorestring="score:%s"%score
                score_pen.clear()
                score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
            if isCollison_enemy_player(player,enemy):
                #winsound.playsound("Adrees", winsound.SND_ASYNC)
                Game_Over=True
                if Game_Over==True:
                    player.hideturtle()
                    enemy.hideturtle()
                for e in enemies:
                    e.hideturtle()
                wn.bgcolor("red")
               #wn.bgpic("E:\\Aditya\\Python_Programming\\Games\\GameOver.gif")
                break
        if bulletstate=="fire":
            y=bullet.ycor()
            y+=bulletspeed
            bullet.sety(y)
            if bullet.ycor()>275:
                bullet.hideturtle()
                bulletstate="ready"

#delay=input("Press enter to finish")
start_game = tk.Button(win, text="Start", width=20, height=1,
                    font=("Agency FB", 20),bg="#180833", bd=4,
                    fg="white", activebackground="yellow", command=start)
start_game.place(x=300, y=680)
win.mainloop()
