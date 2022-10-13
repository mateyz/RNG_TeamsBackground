import os
import random
from re import L
import dircache
from datetime import date, datetime

def get_random_image(src):
    filename = random.choice(dircache.listdir(src))
    path = os.path.join(src, filename)
    return path

def is_daytime():
    time = datetime.now()
    hour = time.hour
    return hour < 15
    

# Find a way to effectively run this function on startup of the Laptop, or per-day.
if __name__ == "__main__":
    src = "./Images"
    dst = "/Users/christopherhutchings/Library/Application Support/Microsoft/Teams/Backgrounds/Uploads"
    dailyImage = get_random_image(src)

    print("Currently grinding in ... ", dailyImage)

    # Get the time of day, and determine whether or not the night varient should be used.
    daytime = is_daytime()