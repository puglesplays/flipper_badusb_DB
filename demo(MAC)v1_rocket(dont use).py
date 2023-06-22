import time
import pyautogui
from pyflipper.pyflipper import PyFlipper

def open_file():
    file_path = ""

    if True:  
        file_path = "/Users/austinthompson/Desktop/Algebra1-6-End-of-Unit-Assessment-assessment.pdf/"
        pyautogui.press('enter')

    time.sleep(0.5)
    pyautogui.write(file_path)
    pyautogui.press('enter')

while True:  
    time.sleep(1)

open_file()
