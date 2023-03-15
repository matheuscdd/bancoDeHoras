from env import file_name
from math import isnan


def isWork():
    import pandas as pd
    df = pd.read_excel(file_name)
    if not len(df["check-out"]) or not len(df["check-in"]):
        return False
    try:
        result = df["check-out"][len(df["check-out"]) - 1]
        return isnan(result)
    except:
        result = len(df["check-out"]) == len(df["check-in"])
        return not result
