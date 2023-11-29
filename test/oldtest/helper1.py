import os
import subprocess as Sprc
import datetime as Dtm

def get_time(chrono):
    print("-----Fetch by time-----")
    print(f"Enter {chrono} time in the format `dd/mm/yyyy hh/mm/ss` (24- hour clock)")
    t= input().strip()
    try:
        return Dtm.datetime.strptime(t, "%d/%m/%Y %H:%M:%S")
    except ValueError as e:
        print("Invalid input entered");
    except Exception as e:
        print(e);
csv_folder = "C:\\Users\\2003s\\OneDrive\\Desktop\\Internship\\csv_fold"

info = {
    "start_time": "2/8/2023 00:00:00",
    "end_time": "10/8/2023 00:00:00",
}
ps1 = "C:\\Users\\2003s\\PycharmProjects\\AutoRackCSVs\\main.ps1"
fetch_choice = 1
start_time = info.get("start_time")
end_time = info.get("end_time")
command = ["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps1, "-csv_folder", csv_folder, "-fetch_choice",
           str(fetch_choice), "-start_time", start_time, "-end_time", end_time]
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
        i += 1
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
