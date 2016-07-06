import ctypes
import time

def click_and_drag(x0,y0,x1,y1):
    '''(int,int,int,int) -> None
    '''
    SetCursorPos(x0, y0) 
    mouse_event(2, 0, 0, 0, 0) # click
    SetCursorPos(x1, y1)
    #time.sleep(1) # wait 2 ms for stability
    mouse_event(4, 0, 0, 0, 0) #unclick

def click(x,y):
     SetCursorPos(x, y)
     mouse_event(2, 0, 0, 0, 0) # click
     mouse_event(4, 0, 0, 0, 0) #unclick

def drag_window():
    win32gui.ShowWindow(window.f2_hwnd, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(window.f2_hwnd)
    c = window.get_corners(window.f2_hwnd)
    click_and_drag(c[0] +25,c[1] + 50,c[2] - 25,c[3]-50)     

SetCursorPos = ctypes.windll.user32.SetCursorPos
mouse_event = ctypes.windll.user32.mouse_event


