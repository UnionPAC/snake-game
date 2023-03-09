from turtle import Turtle

# CONSTANTS
ALIGN = "center"
UPDATE_FONT = ("PT Mono", 16, "normal")
GAME_OVER_FONT = ("PT Mono", 26, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.setpos(x=0, y=270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGN, font=UPDATE_FONT)

    def game_over(self):
        self.setpos(x=0, y=20)
        self.write("GAME OVER", False, align=ALIGN, font=GAME_OVER_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
