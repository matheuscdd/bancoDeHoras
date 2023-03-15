from datetime import datetime, date
from calc_hours import calcHours


def openSheet(choice):
    from openpyxl import load_workbook
    sheet = load_workbook("register.xlsx")
    tab = sheet.active
    hour = datetime.now().strftime("%H:%M:%S")
    num = len(tab["A"]) + 1
    if choice == "checkIn":
        checkIn(tab, num, hour)
    else:
        checkOut(tab, num, hour)
    sheet.save("register.xlsx")
    sheet.close()

def registerDay(tab, num):
    today = date.today()
    currDay = f'A{num}'
    tab[currDay] = today
    tab[currDay].number_format = "dd/mm/yyyy"


def checkIn(tab, num, hour):
    registerDay(tab, num)
    currCheckIn = f'B{num}'
    tab[currCheckIn] = hour
    tab[currCheckIn].number_format = "hh:mm:ss"


def checkOut(tab, num, hour):
    currCheckOut = f'C{num - 1}'
    tab[currCheckOut] = hour
    tab[currCheckOut].number_format = "hh:mm:ss"


# arrumar um jeito de fazer a soma do total de horas sem dar conflito
# openSheet("checkOut")


