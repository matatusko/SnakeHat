import random
from time import time, sleep
from sense_hat import SenseHat

RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
MAGENTA = [255, 0, 255]
CYAN = [0, 255, 255]

sense = SenseHat()
sense.clear()