#Turtle Race
import turtle
import tkinter as tk
from tkinter import messagebox as msg
from turtle import TurtleScreen,RawTurtle
import random
#Creating Gui
win=tk.Tk()
win.geometry("800x600")
win.resizable(width=False,height=False)
win.title("--Turtle Race--")
win["bg"]="green"

canvas=tk.Canvas(win,width=650,height=455)
canvas.place(x=100,y=10)
title=tk.Label(canvas,text="Turtle Race",width=20,height=1,font=("Agency FB",40))
title.place(x=100,y=10)
chance=""
def start():
    s1=TurtleScreen(canvas)
    s1.bgcolor("white")
    player_one=RawTurtle(s1)
    player_one.color("red")
    player_one.shape("turtle")
    player_one.shapesize(1.0,1.0)
    player_one.penup()
    player_one.goto(-200,100)

    player_two=player_one.clone()
    player_two.color("black")
    player_two.penup()
    player_two.goto(-200,-100)

    player_one.goto(300,60)
    player_one.pendown()
    player_one.circle(40)
    player_one.penup()
    player_one.goto(-200,100)
    
    player_two.goto(300,-120)
    player_two.pendown()
    player_two.circle(40)
    player_two.penup()
    player_two.goto(-200,-100)

    die=[1,2,3,4,5,6]
    def play():
        for i in range(20):
            global chance
            if chance != "A":
                chance="A"
                if player_one.pos()>=(270,50):
                    print("PLAYER ONE WINS!")
                    win.destroy()
                    win2=tk.Tk()
                    win2.title("Congratulations!")
                    win2.geometry("450x100")
                    win2["bg"]="yellow"
                    tk.Label(win2,text="Player One Wins!",activeforeground="white",font=("Agency FB",40))
                    break
                else:
                    die_outcome=random.choice(die)
                    player_one.fd(20*die_outcome)
                    print("Player one Position==>",player_one.pos())
            else:
                #msg.showwarning("Alert!","Its Not your CHANCE!")
                break
    
    def play2():
        for i in range(20):
            global chance
            if chance != "B":
                chance="B"
                if player_two.pos()>=(270,-50):
                    print("PLAYER TWO WINS!")
                    win.destroy()
                    win2=tk.Tk()
                    win2.title("Congratulations!")
                    win2.geometry("450x100")
                    win2["bg"]="yellow"
                    tk.Label(win2,text="Player Two Wins!",activeforeground="white",font=("Agency FB",40))
                    break
                else:
                    die_outcome=random.choice(die)
                    player_two.fd(20*die_outcome)
                    print("Player two Position==>",player_two.pos())
            else:
                #msg.showwarning("Alert!","Its Not your CHANCE!")
                break
    player1=tk.Button(canvas,text="player1",bg="green",fg="white",
                      activeforeground="yellow",
                      font=("Agency FB",18),
                      relief="ridge",width=8,height=1,command=play)
    player1.place(x=113,y=420)

    player2=tk.Button(canvas,text="player2",bg="green",fg="white",
                      activeforeground="yellow",
                      font=("Agency FB",18),
                      relief="ridge",width=8,height=1,command=play2)
    player2.place(x=250,y=420)

start_button=tk.Button(canvas,text="Start",bg="green",fg="white",
                      activeforeground="yellow",
                      font=("Agency FB",18),command="start",
                      relief="ridge",width=8,height=1)
start_button.place(x=200,y=20)

stop_button=tk.Button(canvas,text="Stop",bg="green",fg="white",
                      activeforeground="yellow",
                      font=("Agency FB",18),command=win.destroy,
                      relief="ridge",width=8,height=1)
stop_button.place(x=200,y=20)

    












    
