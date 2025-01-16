import time
import numpy as np
import pyautogui as pg
import matplotlib.pyplot as plt

time.sleep(5)
sc = pg.screenshot()
print('done!')

plt.imshow(sc)
plt.grid(True) # shows the range at which the game window is displayed (or region of interest)

sc = np.array(sc)
sc_crop = sc[300:400, 2600:3200] # change these values
plt.imshow(sc_crop)

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
sc_crop_grey = rgb2gray(sc_crop)
plt.imshow(sc_crop_grey, cmap='gray')

def get_sc():
    sc = pg.screenshot()
    sc = np.array(sc)
    sc_crop = sc[300:400, 2600:3200]
    sc_crop_grey = rgb2gray(sc_crop)
    return sc_crop_grey

sc_sample = get_sc()




