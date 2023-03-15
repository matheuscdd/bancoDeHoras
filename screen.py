from tkinter import *

win = Tk()
win.resizable(False, False)

condition = dict(
    title="Banco de horas",
    btn="Carregando...",
    icon="clock.ico",
    work=False
)

win.iconbitmap(condition["icon"])

def working():
    win.title("Trabalhando...")
    win.iconbitmap("yes.ico")
    button["text"] = "Check-out"


def pause():
    win.title("Pausa")
    win.iconbitmap("not.ico")
    button["text"] = "Check-in"



def status():
    condition["work"] = not condition["work"]
    working() if condition["work"] else pause()


title = Label(win, text=condition["title"])
title.grid(column=0, row=0, pady=20, padx=20)
button = Button(win, text=condition["btn"], command=status)
button.grid(column=0, row=2, padx=10, pady=10)

text = Text(win, height=4, width=30, font="Calibri 10", padx=10, pady=10)
text.insert(INSERT, "oLÁ \n")
text.insert(END, "Acabou")
text.grid(column=0, row=1)


title = Label(win, text="Banco de horas")
title.grid(column=0, row=0, pady=20, padx=20)


win.mainloop()
