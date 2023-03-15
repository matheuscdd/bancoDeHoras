from env import file_name
def calcHours():
    import pandas as pd
    from datetime import datetime as dt
    df = pd.read_excel(file_name)

    df["check-out"] = pd.to_datetime(df["check-out"], format="%H:%M:%S").dt.time
    df["check-in"] = pd.to_datetime(df["check-in"], format="%H:%M:%S").dt.time

    df["work_hours"] = df.apply(lambda x: dt.combine(dt.min, x["check-out"]) - dt.combine(dt.min, x["check-in"]), axis=1)

    df["work_hours"] = df["work_hours"].apply(lambda x: str(x)[7:15])

    df.to_excel(file_name, index=False)

