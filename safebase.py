import pyperclip
import win32gui
import win32clipboard
import time
import re


cc_composed_pattern = re.compile(r'\D*(\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4})\D*')
cpf_pattern = re.compile(r'\b\d{3}[ .-]?\d{3}[ .-]?\d{3}[ -]?\d{2}\b')


target_apps = ["chatGPT", "notepad", "word", "iexplore", "firefox", "chrome", "edge", "opera", "safari"]

def block_paste():

    import ctypes
    
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0) 
    ctypes.windll.user32.keybd_event(0x56, 0, 0, 0) 
    ctypes.windll.user32.keybd_event(0x56, 0, 2, 0) 
    ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)

while True:
    active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if any(app.lower() in active_window.lower() for app in target_apps):
        clipboard_content = pyperclip.paste()
        if cc_hy_pattern.search(clipboard_content) or cc_ns_pattern.search(clipboard_content) or cc_composed_pattern.search(clipboard_content) or cpf_pattern.search(clipboard_content):
            block_paste()


    time.sleep(2.0)

