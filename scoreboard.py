from turtle import Turtle

ALIGN = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def increse_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)