import os

def check_for_output(folder_path):
    try:
        # List all files in the directory
        files = os.listdir(folder_path)

        for file in files:
            if file == "output.txt":
                return True
            elif(file != "DO NOT MODIFY, DELETE THIS FOLDER"):
                os.remove(os.path.join(folder_path, file))
        return False
    except FileNotFoundError:
        print("Folder not found.")
        return False
