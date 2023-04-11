import pyperclip
import win32gui
import win32clipboard
import time
import re

#Desired regex
cc_composed_pattern = re.compile(r'\D*(\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4})\D*')
cpf_pattern = re.compile(r'\b\d{3}[ .-]?\d{3}[ .-]?\d{3}[ -]?\d{2}\b')

#Desired apps
target_apps = ["chatGPT", "notepad.exe", "winword.exe", "iexplore.exe", "firefox.exe", "chrome.exe", "msedge.exe", "opera.exe", "safari.exe"]

#Erase clipboard at CC or CPF number copy detection
#Active window condition still not working! For now it will erase the clipboard for all apps, based on the patterns detected only. 
def block_paste():
    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()

while True:
    active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if any(app.lower() in active_window.lower() for app in target_apps):
        clipboard_content = pyperclip.paste()
        if cc_composed_pattern.search(clipboard_content) or cpf_pattern.search(clipboard_content):
            block_paste()

#No loop No look
    time.sleep(1.0)

