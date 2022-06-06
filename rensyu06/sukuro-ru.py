import tkinter
from PIL import Image, ImageTk, ImageOps
import random

# アプリの設定
VIEW_WIDTH = 600
VIEW_HEIGHT = 400
GAME_WIDTH = 1500

BG_IMAGE_PATH = "bg_natural_sougen.jpeg"

class Character:

    def __init__(self):
        pass

class Player(Character):

    def __init__(self):
        pass

class Enemy(Character):

    def __init__(self):
        pass

class Goal(Character):

    def __init__(self):
        pass

class Screen:

    def __init__(self, master):
        self.master = master

        self.view_width = VIEW_WIDTH
        self.view_height = VIEW_HEIGHT
        self.game_width = GAME_WIDTH
        self.game_height = self.view_height

        self.createWidgets()
        self.drawBackground()

    def createWidgets(self):
        self.canvas = tkinter.Canvas(
            self.master,
            width=self.view_width,
            height=self.view_height,
            scrollregion= (
                0,0,self.game_width,self.game_height
            ),
            highlightthickness=0
        )
        self.canvas.grid(column=0, row=0)

        xbar = tkinter.Scrollbar(
            self.master,
            orient=tkinter.HORIZONTAL,
        )

        xbar.grid(
            row=1, column=0,
            sticky=tkinter.W + tkinter.E
        )

        xbar.config(
            command=self.canvas.xview
        )

        self.canvas.config(
            xscrollcommand=xbar.set
        )

    def drawBackground(self):
        image = Image.open(BG_IMAGE_PATH)

        size = (self.game_width, self.game_height)
        resized_image = image.resize(size)

        self.bg_image = ImageTk.PhotoImage(resized_image)

        self.canvas.create_image(
            0, 0,
            anchor=tkinter.NW,
            image=self.bg_image
        )

class Game:

    def __init__(self, master):
        self.master = master
        self.screen = Screen(self.master)

def main():
    app = tkinter.Tk()
    game = Game(app)
    app.mainloop()

if __name__ == "__main__":
    main()