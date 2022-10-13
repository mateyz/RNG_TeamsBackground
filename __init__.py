from genericpath import exists
import os
import random
import shutil
import dircache
from datetime import date, datetime

def get_random_image(src):
    filename = random.choice(dircache.listdir(src))
    path = os.path.join(src, filename)
    thumbPath = os.path.join(src + "../ImagesThumbnail", filename)
    Dict = {
        "Image" : path,
        "Thumbnail" : thumbPath
    }

    return Dict

def is_daytime():
    time = datetime.now()
    hour = time.hour
    return hour < 15
    

def strip_image_name(image):
    return False

# Find a way to effectively run this function on startup of the Laptop, or per-day.
if __name__ == "__main__":
    src = "./Images"
    dst = "/Users/christopherhutchings/Library/Application Support/Microsoft/Teams/Backgrounds/Uploads"
    dailyImage = get_random_image(src)
    print("Currently grinding in ... ", dailyImage["Image"])

    # Get the time of day, and determine whether or not the night varient should be used.
    daytime = is_daytime()

    # Check if we already have a Default Image. 
    path = exists(dst + "/Default.jpg")
    if path:
        print("File exists!")
        os.remove(dst + "/Default.jpg")
    #    os.remove(dst + "/Default_thumb.jpg")

    # Copy over the new background files.
    shutil.copyfile(dailyImage["Image"], dst + "/Default.jpg")
    
    
    # shutil.copyfile(dailyImage["Thumbnail"], dst)
    
