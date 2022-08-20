import cv2
import numpy as np
import pyautogui
# this is where the detection will be handled will deliver 4 char str into main 
class ChessVision:
    def __init__(self):
        pass

    def get_screenshot(self):
        while True:
            screenshot = pyautogui.screenshot()
            screenshot = np.array(screenshot)
            screenshot = screenshot[:, :, :, ::-1].copy()
            cv2.imshow('ChessVisor', screenshot)
            if cv2.waitKey(1) ==ord('q'):
                break
        cv2.destroyAllWindows()
        print('done')


CV = ChessVision()
CV.get_screenshot()