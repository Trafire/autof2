import win32clipboard
import time

def set_clipbaord(data):
    win32clipboard.OpenClipboard()
    time.sleep(0.1)
    win32clipboard.SetClipboardText(data)
    win32clipboard.CloseClipboard()

def get_clipboard():
    data = None
    for i in range(10000):
        try:
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            break
        except:
            time.sleep(0.01)
    return data
