from env import file_name, need_week_hours
import pandas as pd
from datetime import datetime as dt, date, timedelta
def calcHours():
    df = pd.read_excel(file_name)

    df["check-out"] = pd.to_datetime(df["check-out"], format="%H:%M:%S").dt.time
    df["check-in"] = pd.to_datetime(df["check-in"], format="%H:%M:%S").dt.time

    df["work_hours"] = df.apply(lambda x: dt.combine(dt.min, x["check-out"]) - dt.combine(dt.min, x["check-in"]), axis=1)
    df["week"] = df["data"].dt.isocalendar().week
    df["work_hours"] = df["work_hours"].apply(lambda x: str(x)[7:15])

    df.to_excel(file_name, index=False)


def calcWeekHours(all_weeks: bool = False):
    df = pd.read_excel(file_name)
    df["week"] = df["data"].dt.isocalendar().week
    df["work_hours"] = pd.to_timedelta(df["work_hours"])
    week_hours = df.groupby("week")["work_hours"].sum()
    this_week = date.today().isocalendar().week
    if all_weeks:
        return week_hours
    try:
        find = week_hours[this_week]
        return find
    except:
        return "0 days 00:00:00"


def calcDayHours():
    df = pd.read_excel(file_name)
    df["work_hours"] = pd.to_timedelta(df["work_hours"])
    days_hours = df.groupby("data")["work_hours"].sum()
    this_day = date.today().strftime("%Y-%m-%d")
    try:
        find = days_hours[this_day]
        return str(find)[7:15]
    except:
        return "00:00:00"


calcHours()
def differenceHoursWeek():
    week_hours = calcWeekHours(all_weeks=True)
    week_count = len(week_hours)
    tot_hours = week_hours.sum()

    # print(result)
    needed_hours = timedelta(hours=need_week_hours) * week_count
    print(needed_hours)


differenceHoursWeek()

def convertHours(timedate):
    hours = int(timedate.total_seconds() // 3600)
    minutes = str(timedate - timedelta(hours=hours))[10:15]
    result = f"{hours}:{minutes}"
    print(result)
    return result