import pyxel

class BSO:
    def __init__(self):
        self.balls = 0
        self.strikes = 0
        self.outs = 0

    def add_ball(self):
        self.balls += 1
        if self.balls >= 4:
            self.balls = 0
            self.add_strike()

    def add_strike(self):
        self.strikes += 1
        if self.strikes >= 3:
            self.strikes = 0
            self.add_out()

    def add_out(self):
        self.outs += 1
        if self.outs >= 3:
            self.balls = 0
            self.strikes = 0
            self.outs = 0

    def draw(self, x, y):
        pyxel.text(x, y, "BALL   " + "X" * self.balls + "-" * (3 - self.balls), 7)
        pyxel.text(x, y + 10, "STRIKE " + "X" * self.strikes + "-" * (2 - self.strikes), 7)
        pyxel.text(x, y + 20, "OUT    " + "X" * self.outs + "-" * (2 - self.outs), 7)
