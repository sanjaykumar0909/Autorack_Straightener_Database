import os
import subprocess as Sprc
import datetime as Dtm


def get_time():
    print("-----Fetch by time-----")
    print("Enter start time in the format `dd/mm/yyyy dd/mm/yyyy` (24- hour clock)")
    t = input().strip()
    try:
        return Dtm.datetime.strptime(t, "%d/%m/%Y %H:%M:%S")
    except ValueError as e:
        print("Invalid input entered")
    except Exception as e:
        print(e)


print("enter path containing the bend files:")
csv_folder = input()
finished = False
info = {
    "fetch_by_creation": {
        "start_time": "",
        "end_time": "",
    },
    "fetch_by_access": {
        "start_time": "",
        "end_time": "",
    },
    "fetch_by_modification": {
        "start_time": "",
        "end_time": "",
    },
}
while not finished:
    print("enter 1 to fetch file by creation time")
    print("enter 2 to fetch file by access time")
    print("enter 3 to fetch file by modification")
    fetch_choice = int(input());
    print()

    if (fetch_choice == 1):
        t1 = get_time()
        info.get("fetch_by_creation")["start_time"] = str(t1)
        t2 = get_time()
        info.get("fetch_by_creation")["end_time"] = str(t2)
    elif (fetch_choice == 2):
        t1 = get_time()
        info.get("fetch_by_access")["start_time"] = str(t1)
        t2 = get_time()
        info.get("fetch_by_access")["end_time"] = str(t2)
    elif (fetch_choice == 3):
        t1 = get_time()
        info.get("fetch_by_modification")["start_time"] = str(t1)
        t2 = get_time()
        info.get("fetch_by_modification")["end_time"] = str(t2)
    else:
        print("Enter valid choice")


    ps1 = "C:\\Users\\2003s\\PycharmProjects\\AutoRackCSVs\\main.ps1"

    start_time = info.get("fetch_by")

    end_time = info.get("")
    command = ["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps1, "-csv_folder", csv_folder, "-start_time",
               start_time, "-end_time", end_time]
    process = Sprc.Popen(command, stdout=Sprc.PIPE, stderr=Sprc.PIPE, text=True)

    op, err = process.communicate()
    ret_code = process.returncode
    if (ret_code == 0):
        print("Successfully fetched")
        print(f'the files are:')
        i = 0
        files = op.split(" ")
        while i < len(files):
            print(f'{i + 1}. {files[i]}')
        print("enter file name to open, type X to skip:")
        inp = input().strip()
        if (inp == "X" or inp == "x"):
            pass
        else:
            open_csv = input().strip()
            try:
                excel = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                Sprc.Popen([excel, os.path.join(csv_folder, open_csv)])
            except FileNotFoundError as fnf:
                print(fnf)
                input()
            except Exception as e:
                print(e)
                input()
    else:
        print("Failed")
        print(err)
        input()
    print("enter 'y' to continue and 'x' to exit the application")
    if (input().strip() == 'x'): quit(0)

