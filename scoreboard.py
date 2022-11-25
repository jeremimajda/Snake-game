import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.current_score = -1
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.current_score += 1
        self.write(f"Score: {self.current_score} High score:{self.high_score}",
                   False, "center", ("Courier", 20, "normal"))

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", False, "center", ("Courier", 20, "normal"))

    def reset(self):
        if self.current_score > self.high_score:
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.current_score))
            with open("high_score.txt", mode="r") as file:
                self.high_score = int(file.read())
        self.current_score = -1
        self.refresh_score()




