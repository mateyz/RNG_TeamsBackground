import os
import random
import dircache

def get_random_image(src):
    filename = random.choice(dircache.listdir(src))
    path = os.path.join(src, filename)
    return path

# Find a way to effectively run this function on startup of the Laptop, or per-day.
if __name__ == "__main__":
    src = "./Images"
    dst = "/Users/christopherhutchings/Library/Application Support/Microsoft/Teams/Backgrounds/Uploads"
    dailyImage = get_random_image(src)

    print("Selected ... ", dailyImage)