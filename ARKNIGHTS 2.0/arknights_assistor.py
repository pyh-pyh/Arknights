import win32process
import time


class Assistor:
    '''Assistor for Arknights'''
    def __init__(self):
    
    
    def play_game():
    titles = globalvar.get_value('titles')
    sites = globalvar.get_value('sites')
    #paperless_estamp_program()
    #win32api.ShellExecute(0, 'open', 'D:\\明日方舟\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe', '', '', 1)
    load.recognize(5, sites['mnq'], 'mnq')
    win32gui.EnumWindows(load.foo, 0)
    lt = [t for t in titles if t]
    lt.sort()

    for t in lt:
        if(t.find('MuMu模拟器')) >= 0:
            hwnd = win32gui.FindWindow(None, t)
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,1240,720,win32con.SWP_SHOWWINDOW)
            hwnd=win32gui.FindWindow(None, t)
            size = win32gui.GetWindowRect(hwnd)
            globalvar.set_value('size', size)
