#!./venv/bin/python
from genericpath import exists
import os
import sys
import random
import shutil
import dircache
from datetime import date, datetime

def get_random_image(src):
    filename = random.choice(dircache.listdir(src))
    path = os.path.join(src, filename)
    print(filename[0 : len(filename) - 4])
    # Initially a dictionary as we needed a thumbnail as well as an original Image. 
    Dict = {
        "Name" : filename[0:len(filename) - 4],
        "Image" : path,
    }
    return Dict

def is_daytime():
    time = datetime.now()
    hour = time.hour
    return hour < 16

def get_image_directory():
    # Search for events (Birthdays, Holidays) and provide cool pictures for them! 
    # Get the time of day, and determine whether or not the night varient should be used.
    daytime = is_daytime()

    if daytime:
        src = "./Images/Day"
    else:
        src = "./Images/Night"

    return src

def strip_image_name(image):
    return False

# Find a way to effectively run this function on startup of the Laptop, or per-day.
if __name__ == "__main__":
    lastTimeRan = "..."
    lastSceneRan = "..."

    # Identify the previous
    fp = open("./CurrentScene.txt")
    for i, line in enumerate(fp):
        if i == 0:
            lastTimeRan = line.replace("\n", "")
        elif i == 1:
            lastSceneRan = line
    print(lastTimeRan)

    sys.exit()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    src = get_image_directory()
    dst = os.path.expanduser('~') + "/Library/Application Support/Microsoft/Teams/Backgrounds/Uploads"

    dailyImage = get_random_image(src)
    
    # Logging
    file_object = open('Logs.txt', 'a')
    file_object.write('\n\nApp running | ' + current_time)
    file_object.write('\nCurrently grinding in ... ' + dailyImage["Name"] + " | "+ dailyImage["Image"])

    # Check if we already have a Default Image. 
    path = exists(dst + "/Default.jpg")
    if path:
        print("File exists ... Replacing with " + dailyImage["Image"])
        os.remove(dst + "/Default.jpg")
    else:
        os.system("osascript -e 'Tell application \"System Events\" to display dialog \" Error: No Default.Jpg selected in Teams...\n Refer to setup guide in ReadMe.md\"'")
        sys.exit()
    # Copy over the new background files.
    shutil.copyfile(dailyImage["Image"], dst + "/Default.jpg")
    
    # Close the file
    file_object.close()
    
    
