from tkinter import *
from calc_hours import calcHours, calcDayHours, convertHours, differenceHoursWeek
from inspect_open_apps import isSheetOpen, isAppAlreadyOpen
from types_project import Condition
from env import file_name, need_week_hours
from checks import openSheet
from verify import isWork, ensureSheetExists
from tkinter.messagebox import showerror


if isAppAlreadyOpen():
    showerror(
        title="Fatal Error",
        message="O programa já está aberto"
    )
else:
    ensureSheetExists()
    conditionWork = Condition(
        title="Trabalhando...",
        icon="./assets/yes.ico",
        btn="Check-out",
        img="./assets/sad.png",
        work=True
    )

    conditionNotWork = Condition(
        title="Pausa",
        icon="./assets/not.ico",
        btn="Check-in",
        img="./assets/happy.png",
        work=False
    )

    condition = conditionWork.copy() if isWork() else conditionNotWork.copy()

    app = Tk()
    app.resizable(False, False)
    app.iconbitmap(condition["icon"])
    app.title(condition["title"])


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
        report()


    def updateInfo():
        global img, render
        app.title(condition["title"])
        app.iconbitmap(condition["icon"])
        button["text"] = condition["btn"]
        render = PhotoImage(file=condition["img"])
        img = Label(app, image=render, padx=20, pady=20)
        img.image = render
        img.grid(column=0, row=5)
        app.update_idletasks()


    def status():
        if messageErrorSheetOpen():
            return
        condition["work"] = not condition["work"]
        working() if condition["work"] else pause()


    button = Button(app, text=condition["btn"], command=status)
    button.grid(column=0, row=2, padx=10, pady=20)

    text = Text(app, height=4, width=30, font=("Calibri", 10), padx=10, pady=10)
    text.grid(column=0, row=1)
    text.config(state=DISABLED)


    def insertText(txt: str, color: str = "black"):
        text.config(state=NORMAL)
        text.insert(INSERT, txt+"\n")
        lines = len(text.get("1.0", END).splitlines())
        text.tag_configure(color, foreground=color)
        text.tag_add(color, f"{lines - 1}.0", END)
        text.config(state=DISABLED)


    def clean_text():
        text.config(state=NORMAL)
        text.delete("1.0", END)
        text.config(state=DISABLED)

    def report():
        from datetime import timedelta
        clean_text()
        insertText(
            f"Hoje trabalhei: {calcDayHours()}", "#3872A2"
        )
        try:
            result = differenceHoursWeek()
            insertText(
                f"Balanço semanal: {result}", "#43C553" if result[0] in "+" else "#D44C3D"
            )
        except:
            insertText(
                f"Balanço semanal: {convertHours(timedelta(hours=need_week_hours), True)}"
            )


    report()



    title = Label(app, text="Banco de horas", font="Calibri 14")
    title.grid(column=0, row=0, pady=20, padx=20)

    render = PhotoImage(file=condition["img"])
    img = Label(app, image=render, pady=40, padx=20)
    img.image = render
    img.grid(column=0, row=5)

    fragment = Label(app, text="")
    fragment.grid(column=0, row=6)

    def messageErrorSheetOpen():
        if isSheetOpen():
            condition["img"] = "./assets/lost.png"
            updateInfo()
            showerror(
                title="Planilha já em uso",
                message=f"Feche o arquivo {file_name} para continuar"
            )
            button["command"] = messageErrorSheetOpen
            button["text"] = "Tentar novamente"
            return True
        else:
            condition["img"] = "./assets/sad.png" if condition["work"] else "./assets/happy.png"
            updateInfo()
            button["command"] = status
            return False


    app.mainloop()
