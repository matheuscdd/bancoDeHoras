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


def ensureSheetExists():
    from os.path import isfile
    import pandas as pd
    exists = isfile(file_name)
    if not exists:
        temp = {"data": ["2023-03-27"], "check-in": ["00:00:00"], "check-out":	["00:00:00"], "work_hours": ["00:00:09"], "week": [13]}
        df = pd.DataFrame(temp)
        df = df.drop(index=df.index)
        df.to_excel(file_name, index=False)

