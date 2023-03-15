from env import file_name

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


