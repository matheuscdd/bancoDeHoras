from tkinter import *
from calc_hours import calcHours
from inspect_sheet_open import isSheetOpen
from types_project import Condition
from env import file_name
from checks import openSheet
from verify import isWork
from PIL import Image

imgH = Image.open("happy.png")



conditionWork = Condition(
    title="Trabalhando...",
    icon="yes.ico",
    btn="Check-out",
    img="sad.png",
    work=True
)

conditionNotWork = Condition(
    title="Pausa",
    icon="not.ico",
    btn="Check-in",
    img="happy.png",
    work=False
)

condition = conditionWork.copy() if isWork() else conditionNotWork.copy()

win = Tk()
win.resizable(False, False)
win.iconbitmap(condition["icon"])
win.title(condition["title"])



def working():
    global condition
    openSheet("check-in")
    condition = conditionWork.copy()
    updateInfo()


def pause():
    global condition
    openSheet("check-out")
    condition = conditionNotWork.copy()
    updateInfo()
    calcHours()


def updateInfo():
    globals()
    win.title(condition["title"])
    win.iconbitmap(condition["icon"])
    button["text"] = condition["btn"]
    img = Label(win, image=PhotoImage(file=condition["img"]))
    img.image = render
    img.grid(column=0, row=5)
    win.update_idletasks()




def status():
    if messageErrorSheetOpen():
        return
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


img = Label(win, image=PhotoImage(file=condition["img"]))
img.image = render
img.grid(column=0, row=5)


def messageErrorSheetOpen():
    # preciso executar antes de fazer as verificações os check-ins
    from tkinter.messagebox import showerror
    if isSheetOpen():
        showerror(
            title="O arquivo está aberto",
            message=f"Feche o arquivo {file_name} para continuar"
        )
        button["command"] = messageErrorSheetOpen
        button["text"] = "Tentar novamente"
        return True
    else:
        button["command"] = status
        button["text"] = condition["btn"]
        return False


win.mainloop()
