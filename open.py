import random
import time
import pyautogui as ui
from Body.speak import speak
from Data.Command.data import open_dld

def opend(text):
    opendlg = random.choice(open_dld)
    speak(f"{opendlg} {text}")
    time.sleep(0.5)
    ui.hotkey("win")
    time.sleep(0.2)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")

def open(text):
    if " website" in text:
        text = text.replace(" website","")
        text = text.replace(text,text+".com")
        opend(text)
    elif " app" in text:
        text = text.replace(" app", "")
        opend(text)

    else :
        opend(text)



