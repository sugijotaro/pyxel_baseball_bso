from bso import BSO
import pyxel

class App:
    def __init__(self):
        self.bso = BSO()
        pyxel.init(160, 120)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_B):
            self.bso.add_ball()
        if pyxel.btnp(pyxel.KEY_S):
            self.bso.add_strike()
        if pyxel.btnp(pyxel.KEY_O):
            self.bso.add_out()

    def draw(self):
        pyxel.cls(0)
        self.bso.draw(10, 10)

App()
