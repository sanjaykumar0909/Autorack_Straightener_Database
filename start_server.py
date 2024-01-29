import subprocess
import threading

django_run_cmd = [
    r"venv\scripts\activate.bat",
    "py manage.py runserver"
]

react_run_cmd = [
    "npm start"
]

def django_run():
    res = subprocess.Popen(django_run_cmd, shell=True, cwd=r'path/to/django/project', stdout=subprocess.PIPE, text=True)
    out, err = res.communicate()
    print("Django Output:", out)

def react_run():
    res = subprocess.Popen(react_run_cmd, shell=True, cwd=r'path/to/react/project', stdout=subprocess.PIPE, text=True)
    out, err = res.communicate()
    print("React Output:", out)

t1 = threading.Thread(target=django_run)
t2 = threading.Thread(target=react_run)

t1.start()
t2.start()

t1.join()  # Wait for the threads to finish
t2.join()

