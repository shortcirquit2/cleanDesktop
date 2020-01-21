#! python3
"""
Written for Windows 10 and Python 3 by: shortcircuit2

Creates a folder on the desktop with the current date as
name and moves the files on the desktop into this new folder.

It excludes the file desktop.ini and hidden files.
"""
import os
import datetime

# get the path to the desktop
desktop_path = str(os.environ.get("USERPROFILE")) + '\\Desktop\\'

# get the current date and make a variable that holds the location of the new folder
date_object = datetime.datetime.today()
date_string = date_object.strftime("%Y-%m-%d")
new_folder = desktop_path + date_string

# makes a new folder with the current date as name
try:
    os.mkdir(new_folder)
except FileExistsError:
    pass

# move the files on the desktop into the new file. exclude hidden files and desktop.ini
for file in os.listdir(desktop_path):
    if '~' not in file and file != 'desktop.ini' and file != date_string:
        file_path = desktop_path + file
        new_file_path = new_folder + '\\' + file

        try:
            os.rename(file_path, new_file_path)
        except FileExistsError:
            print('The file {} does already exist in the folder and will not be moved'.format(file))
        except FileNotFoundError:
            print("Couldn't find the file: " + file)
