import os
import random
import dircache

def get_random_image(src):
    print("Retreiving file from ... ", src)
    filename = random.choice(dircache.listdir(src))
    path = os.path.join(src, filename)
    print("Selected ... ", path)


# Find a way to effectively run this function on startup of the Laptop, or per-day.
get_random_image("./Images")