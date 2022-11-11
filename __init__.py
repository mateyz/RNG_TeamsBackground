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

def get_specific_image(src, filename):
    path = os.path.join(src, filename)
    Dict = {
        "Name" : filename[0:len(filename) - 4],
        "Image" : path,
    }
    return Dict

def is_daytime():
    time = datetime.now()
    hour = time.hour
    return hour < 11

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
    lastSceneRan = "..."

    # Identify the previous image theme
    fp = open("./CurrentScene.txt")
    for i, line in enumerate(fp):
        lastSceneRan = line.replace("\n", "")
        
    print(lastSceneRan)
    src = get_image_directory()

    if(is_daytime()):
        print("Generate a new image for the day")
        newBackground = get_random_image(src)
    else:
        print("Generating night varient for current (" + lastSceneRan + ") background")
        if os.path.exists(src + "/" + lastSceneRan + ".jpg"):
            newBackground = get_specific_image(src, lastSceneRan + ".jpg")
        else:
            print("Night varient not found ... Providing a random nighttime image")
            newBackground = get_random_image(src)

    # Save the previous image name to our file for later.
    print(newBackground)
    persistentFile = open("./CurrentScene.txt", "w")
    persistentFile.write(newBackground["Name"])
    persistentFile.close()

    # Force replacing the Default.jpg image
    dst = os.path.expanduser('~') + "/Library/Application Support/Microsoft/Teams/Backgrounds/Uploads"

    # Check if we already have a Default Image. 
    path = exists(dst + "/Default.jpg")
    if path:
        print("File exists ... Replacing with " + newBackground["Image"])
        os.remove(dst + "/Default.jpg")
    else:
        os.system("osascript -e 'Tell application \"System Events\" to display dialog \" Error: No Default.Jpg selected in Teams...\n Refer to setup guide in ReadMe.md\"'")
        sys.exit()
    # Copy over the new background files.
    shutil.copyfile(newBackground["Image"], dst + "/Default.jpg")
    
    # Logging
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    file_object = open('Logs.txt', 'a')
    file_object.write('\n\nApp running | ' + current_time)
    file_object.write('\nCurrently grinding in ... ' + newBackground["Name"] + " | "+ newBackground["Image"])
    file_object.close()

    # Exit the current program
    sys.exit()
    
    
