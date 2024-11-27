import random

def get_random_color_gd():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))