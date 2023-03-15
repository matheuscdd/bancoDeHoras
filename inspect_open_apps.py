from env import file_name, app_name

def isSheetOpen():
    import psutil
    for process in psutil.process_iter():
        try:
            if 'excel.exe' in process.name().lower():
                for file in process.open_files():
                    if file_name in file.path.lower():
                        return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def isAppAlreadyOpen():
    import psutil
    counter = 0
    for process in psutil.process_iter():
        if app_name in process.name().lower():
            counter += 1
    return False if counter <= 2 else True

