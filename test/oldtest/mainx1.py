import os
import subprocess as Sprc
import datetime as Dtm
def get_time(chrono):

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
    "start_time": "",
    "end_time": "",
}
#TODO: change path
fetch_by_time_ps1 = "C:\\Users\\2003s\\PycharmProjects\\AutoRackCSVs\\fetch_by_time.ps1"
get_serial_ps1 = "C:\\Users\\2003s\\PycharmProjects\\AutoRackCSVs\\get_serial.ps1"

while True:
    print("Enter 1 to fetch files by modification time")
    print("Enter 2 to fetch files by creation time")
    print("Enter 3 to fetch files by access time")
    print("Enter 4 to get serial number of a file")
    print("Enter 5 to fetch file by serial number")
    fetch_choice = int(input()); print()

    if fetch_choice not in range(1, 6):
        print("Enter valid choice")
        continue
    elif(fetch_choice == 4):
        print("Enter the file name:")
        file_name = input().strip()

        command = ["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", get_serial_ps1, "-folder_path", csv_folder,
                   "-file_name", file_name]
        process = Sprc.Popen(command, stdout=Sprc.PIPE, stderr=Sprc.PIPE, text=True)
        op, err = process.communicate()
        ret_code = process.returncode

        if (ret_code == 0):
            if (op == "-1"):
                print("No such file found")
            print(f"Serial number of the file: {op}")
            pass
        else:
            print("Failed")
            print(err)
            input()
    elif(fetch_choice == 5):


        pass
    else:
        print("-----Fetch by time-----")
        t1 = get_time("start")
        if t1 == None:
            print("Invalid input entered")
            continue
        info["start_time"] = str(t1)
        t2 = get_time("end")
        if t2 == None:
            print("Invalid input entered")
            continue
        info["end_time"] = str(t2)

        start_time = info.get("start_time")
        end_time = info.get("end_time")
        command = ["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", fetch_by_time_ps1, "-folder_path", csv_folder,
                   "-fetch_choice", str(fetch_choice), "-start_time", start_time, "-end_time", end_time]
        process = Sprc.Popen(command, stdout=Sprc.PIPE, stderr=Sprc.PIPE, text=True)

        op, err = process.communicate()
        ret_code = process.returncode
        if (ret_code == 0):
            print(op)
            print("enter file name to open, type X to skip:")
            inp = input().strip()
            if (inp == "X" or inp == "x"):
                pass
            else:
                open_csv = input().strip()
                try:
                    #TODO: change path
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

'''
path = C:\\Users\\2003s\OneDrive\Desktop\Internship\csv_fold
2/8/2023 00:00:00
10/8/2023 00:00:00
'''