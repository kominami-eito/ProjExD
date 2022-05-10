import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc(): # 上下左右の動きの判定と動かし方
    global cx, cy, mx, my, key
    if key == "Up" and x[my-1][mx] == 0:
        my -= 1
    if key == "Down" and x[my+1][mx] == 0:
        my += 1
    if key == "Left" and x[my][mx-1] == 0:
        mx -= 1
    if key == "Right" and x[my][mx+1] == 0:
        mx += 1

    
    cx, cy = 100*mx+50, 100*my+50
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__": # 迷路の基本的な設定
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()

    x = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, x)

    tori = tk.PhotoImage(file = "fig/8.png")
    mx, my = 1,1
    cx, cy = 100*mx+50, 100*my+50
    canvas.create_image(cx, cy, image = tori, tag = "tori")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    root.after(100, main_proc)
    root.mainloop()