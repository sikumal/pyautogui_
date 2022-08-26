import time
import random
import pyautogui as pg

time.sleep(4)

pesan = ["hallo", "P", "asslamu'alaikum", "cek"]

for s in range(100):
    pg.typewrite(random.choice(pesan))
    pg.press("enter")
    time.sleep(0.1)
