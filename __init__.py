#!./venv/bin/python

from genericpath import exists
import os
import random
import shutil
import dircache
from datetime import date, datetime

def get_random_image(src):
    filename = random.choice(dircache.listdir(src))
    path = os.path.join(src, filename)
    
    # Initially a dictionary as we needed a thumbnail as well as an original Image. 
    Dict = {
        "Image" : path,
    }
    return Dict

def is_daytime():
    time = datetime.now()
    hour = time.hour
    return hour < 14

def get_significant_event():
    #Search for events (Birthdays, Holidays) and provide cool pictures for them! 
    return False

def strip_image_name(image):
    return False

# Find a way to effectively run this function on startup of the Laptop, or per-day.
if __name__ == "__main__":
    # Get the time of day, and determine whether or not the night varient should be used.
    daytime = is_daytime()
    
    if daytime:
        src = "./Images"
    else:
        src = "./ImagesNight"

    dst = "/Users/christopherhutchings/Library/Application Support/Microsoft/Teams/Backgrounds/Uploads"

    dailyImage = get_random_image(src)
    
    file_object = open('Logs.txt', 'a')
    file_object.write('\nCurrently grinding in ... ' + dailyImage["Image"])

    # Close the file
    file_object.close()

    # Check if we already have a Default Image. 
    path = exists(dst + "/Default.jpg")
    if path:
        print("File exists!")
        os.remove(dst + "/Default.jpg")

    # Copy over the new background files.
    shutil.copyfile(dailyImage["Image"], dst + "/Default.jpg")
    
    
