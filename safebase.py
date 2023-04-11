import pyperclip
import win32gui
import time
import re

cc_pattern = re.compile(r'\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b')
#cpf_pattern = re.compiler()


target_apps = ["chatGPT", "notepad", "word", "iexplore", "firefox", "chrome", "edge", "opera", "safari"]

def block_paste():

    import ctypes
    
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0) # press the control key
    ctypes.windll.user32.keybd_event(0x56, 0, 0, 0) # press the "V" key
    ctypes.windll.user32.keybd_event(0x56, 0, 2, 0) # release the "V" key
    ctypes.windll.user32.keybd_event(0x11, 0, 2, 0) # release the control key

while True:
    active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if any(app.lower() in active_window.lower() for app in target_apps):
        clipboard_content = pyperclip.paste()
        if cc_pattern.search(clipboard_content) or cpf_pattern.search(clipboard_content):
            block_paste()


    time.sleep(0.5)

