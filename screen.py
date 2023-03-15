from tkinter import *

win = Tk()
win.title("Banco de horas")
win.iconbitmap("heart.ico")

title = Label(win, text="Banco de horas")
title.grid(column=0, row=0, pady=20, padx=20)
#melhorar esse cara
button = Button(win, text="check-in", command=lambda: win.iconbitmap("clock.ico"))
button.grid(column=0, row=1, padx=10, pady=10)

win.mainloop()
