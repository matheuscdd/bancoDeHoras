from tkinter import *
from inspect_sheet_open import isSheetOpen

from env import file_name

condition: dict = dict(
    title="Banco de horas",
    btn="Carregando...",
    icon="clock.ico",
    work=False
)

win = Tk()
win.resizable(False, False)
win.iconbitmap(condition["icon"])

def working():
    global condition
    condition = dict(
        title="Trabalhando...",
        icon="yes.ico",
        btn="Check-out",
        work=True
    )
    updateInfo()


def pause():
    global condition
    condition = dict(
        title="Pausa",
        icon="not.ico",
        btn="Check-in",
        work=False
    )
    updateInfo()

def updateInfo():
    button["text"] = condition["btn"]
    win.title(condition["title"])
    win.iconbitmap(condition["icon"])


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

def messageErrorSheetOpen():
    # preciso executar antes de fazer as verificações os check-ins
    # Estou pensando em alterar o botão aqui
    from tkinter.messagebox import showerror
    if isSheetOpen():
        showerror(
            title=f"Erro: O arquivo está aberto",
            message=f"Feche o arquivo {file_name} para continuar"
        )
        button["command"] = messageErrorSheetOpen
        button["text"] = "Tentar novamente"
    else:
        button["command"] = status
        button["text"] = condition["btn"]

messageErrorSheetOpen()

win.mainloop()
