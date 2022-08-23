import cv2
import numpy as np
import pyautogui
# this is where the detection will be handled will deliver 4 char str into main 
class ChessVision:
    def __init__(self):
        self.windowRegion = 400,355,1170,1180

        pass

    def get_screenshot(self):
        while True:
            screenshot = pyautogui.screenshot(region = self.windowRegion)
            screenshot = np.array(screenshot)
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
            cv2.imshow('ChessVisor', screenshot)