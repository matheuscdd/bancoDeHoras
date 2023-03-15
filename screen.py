from tkinter import *
from calc_hours import calcHours
from inspect_open_apps import isSheetOpen, isAppAlreadyOpen
from types_project import Condition
from env import file_name
from checks import openSheet
from verify import isWork
from tkinter.messagebox import showerror

if isAppAlreadyOpen():
    showerror(
        title="Fatal Error",
        message="O programa já está aberto"
    )
else:
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
    win.wm_attributes("-topmost", 1) # Depois preciso tirar essa parte
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
        global img, render
        win.title(condition["title"])
        win.iconbitmap(condition["icon"])
        button["text"] = condition["btn"]
        render = PhotoImage(file=condition["img"])
        img = Label(win, image=render)
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

    render = PhotoImage(file=condition["img"])
    img = Label(win, image=render)
    img.image = render
    img.grid(column=0, row=5)


    def messageErrorSheetOpen():
        # preciso executar antes de fazer as verificações os check-ins
        if isSheetOpen():
            showerror(
                title="Planilha já em uso",
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
