import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, txt)

def button_equal(event):
    get = entry.get()
    res = eval(get)
    entry.delete(0,tk.END)
    entry.insert(tk.END,res)

def button_clear(event):
    entry.delete(0,tk.END)

root = tk.Tk()
root.title("tk")
root.geometry("300x450")

x =1
y =0
for i in range(9, -1, -1):
    button = tk.Button(root,text=i,font=("Times New Roman", 30))
    button.bind("<1>",button_click)
    button.grid(row = x, column = y, padx = 10, pady = 10)
    y += 1
    if y == 3:
        x += 1
        y = 0

button = tk.Button(root,text="+",font=("Times New Roman", 30))
button.bind("<1>",button_click)
button.grid(row = 4, column = 1)

button = tk.Button(root,text="=",font=("Times New Roman", 30))
button.bind("<1>",button_equal)
button.grid(row = 4, column = 2)

button = tk.Button(root,text="C",font=("Times New Roman", 30))
button.bind("<1>",button_clear)
button.grid(row = 4, column = 3)

entry = tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
entry.grid(row = 0, column = 0,columnspan = 3)

root.mainloop()