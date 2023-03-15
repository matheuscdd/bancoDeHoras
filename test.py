import pandas as pd
from datetime import datetime as dt, time, timedelta
import datetime
df = pd.read_excel("register.xlsx")

df["check-out"] = pd.to_datetime(df["check-out"], format="%H:%M:%S").dt.time
df["check-in"] = pd.to_datetime(df["check-in"], format="%H:%M:%S").dt.time

df["work_hours"] = df.apply(lambda x: dt.combine(dt.min, x["check-out"]) - dt.combine(dt.min, x["check-in"]), axis=1)

# result = str(df["work_hours"][0])[7:15]
df["work_hours"] = df["work_hours"].apply(lambda x: str(x)[7:15])
# df["work_hours"] = df["work_hours"].astype("datetime64")
# print(result)
df.to_excel("result.xlsx", index=False)
