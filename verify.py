from env import file_name
def isWork():
    import pandas as pd
    df = pd.read_excel(file_name)
    result = len(df["check-in"]) == len(df["check-out"])

    a = len(df["check-out"])
    print(df["check-out"])

    print(result)
    return not result

isWork()