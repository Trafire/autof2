import win32gui
import win32con
from autof2.interface import mouse
from autof2.interface import clipboard
from autof2.interface.send_data import SendData

def enumHandler(hwnd, lParam):
    global f2_hwnd
    if win32gui.IsWindowVisible(hwnd):
        if 'Connect 2000 (© Uniware Computer Systems BV) (Session 1 : 192.168.180.1)' in win32gui.GetWindowText(hwnd):
            f2_hwnd =  hwnd
       

def get_hwnd():
    win32gui.EnumWindows(enumHandler, f2_hwnd) # stops when f2_hwnd is not None


def get_corners(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x0 = rect[0]
    y0 = rect[1]
    x1 = rect[2] #- x
    y1 = rect[3] #- y

    return x0,y0,x1,y1
    
def drag_window():
    win32gui.ShowWindow(f2_hwnd, win32con.SW_MAXIMIZE)
    try:
        win32gui.SetForegroundWindow(f2_hwnd)
    except:
        get_hwnd()
        win32gui.SetForegroundWindow(f2_hwnd)
    c = get_corners(f2_hwnd)
    mouse.click_and_drag(c[0] +25,c[1] + 50,c[2] - 25,c[3]-50) 

def get_window():
    send = SendData()
    drag_window()
    send.send('%c')
    data = None
    for i in range(3):
        try:
            data = clipboard.get_clipboard()
            break
        except:
            time.sleep(0.01)
    return data        


f2_hwnd = None
get_hwnd()
