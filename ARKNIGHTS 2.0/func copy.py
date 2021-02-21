import load
import win32gui
import win32api
import win32con
import win32process
import win32event
import time
import ctypes
import globalvar
import pyautogui
import image
import datetime
import os


def paperless_estamp_program(path='D:\\明日方舟\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe'):
    ifexistexe=os.system('tasklist|findstr "programe.exe"')
    if ifexistexe==0:
        os.system('taskkill /f /im "programe.exe"')
        time.sleep(1)
    handle=win32process.CreateProcess(path, '', None , None , 0 ,win32process.CREATE_NEW_CONSOLE , None , None ,win32process.STARTUPINFO())
    win32event.WaitForSingleObject(handle[0],2)


def play_gamep():
    #titles = globalvar.get_value('titles')
    sites = globalvar.get_value('sites')
    #paperless_estamp_program()
    #win32api.ShellExecute(0, 'open', 'D:\\明日方舟\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe', '', '', 1)
    #load.recognize(5, sites['mnq'], 'mnq')
    #win32gui.EnumWindows(load.foo, 0)
    #lt = [t for t in titles if t]
    #lt.sort()

    '''for t in lt:
        if(t.find('MuMu模拟器')) >= 0:
            hwnd = win32gui.FindWindow(None, t)
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,1240,720,win32con.SWP_SHOWWINDOW)
            hwnd=win32gui.FindWindow(None, t)
            size = win32gui.GetWindowRect(hwnd)
            globalvar.set_value('size', size)'''
            
    load.click_button(5, sites['mrfz'], 'mrfz', 0.1)
    load.click_button(1, sites['start'], 'start', 0.1)
    load.click_button(1, sites['kshx'], 'kshx', 0.1)
    if load.judge(10, 0.5, sites['crossgg'], 'crossgg'):
        time.sleep(2)
        load.click_button(1, sites['crossgg'], 'crossgg', 2)
    time.sleep(5)
    load.click('blank', 0.5)
    load.click('blank', 0.5)
    if load.judge(5, 0.5, sites['crossqd'], 'crossqd'):
        load.click_button(1, sites['crossqd'], 'crossqd', 1)


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
            
    load.click_button(5, sites['mrfz'], 'mrfz', 0.1)
    load.click_button(1, sites['start'], 'start', 20)
    load.click('kshx', 0.1)
    if load.judge(10, 0.5, sites['crossgg'], 'crossgg'):
        time.sleep(2)
        load.click_button(1, sites['crossgg'], 'crossgg', 2)
    time.sleep(5)
    load.click('blank', 0.5)
    load.click('blank', 0.5)
    if load.judge(5, 0.5, sites['crossqd'], 'crossqd'):
        load.click_button(1, sites['crossqd'], 'crossqd', 1)



def play_redivep():
    #titles = globalvar.get_value('titles')
    #sites = globalvar.get_value('sites')
    #win32process.CreateProcess(1, 'open', 'D:\\明日方舟\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe', '', '', 1)
    '''load.recognize(5, sites['mnq'], 'mnq')
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

    time.sleep(100)'''
    load.click('redive', 30)
    load.click('start', 30)
    load.click('skip', 5)
    load.click('skip', 5)
    load.click('skip', 5)
    load.click('shutnotify', 5)
    load.click('myhomepage', 5)
    load.click('myhomepage', 5)


def play_redive():
    titles = globalvar.get_value('titles')
    sites = globalvar.get_value('sites')
    #win32process.CreateProcess(1, 'open', 'D:\\明日方舟\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe', '', '', 1)
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

    time.sleep(100)
    load.click('redive', 30)
    load.click('start', 30)
    load.click('skip', 5)
    load.click('skip', 5)
    load.click('skip', 5)
    load.click('shutnotify', 5)
    load.click('myhomepage', 5)
    load.click('myhomepage', 5)




def jijian():
    sites = globalvar.get_value('sites')
    
    # 检测主界面基建按钮有无提醒
    if not load.judge(2, 0.2, sites['jijianbutton'], 'jijianbutton'):

        # 主界面点基建
        load.click('jijian', 8)

        '''# 点制造站分配制造任务
        load.click('production', 1)
        load.click('production', 1)
        load.click('xingdongjieshu', 1)
        load.click('maxproduce', 1)
        load.click('zhixinggenggai', 1)
        load.click('production1', 1)
        load.click('maxproduce', 1)
        load.click('zhixinggenggai', 1)
        load.click('production2', 1)
        load.click('maxproduce', 1)
        load.click('zhixinggenggai', 1)
        load.click('production3', 1)
        load.click('maxproduce', 1)
        load.click('zhixinggenggai', 1)
        load.click('return', 1)
        load.click('return', 1)'''

        # 判断有无提醒
        if load.judge(2, 0.2, sites['notify'], 'notify'):
            load.click_button(1, sites['notify'], 'notify', 2)
            load.click('harvest', 1)
            load.click('harvest', 1)
            load.click('harvest', 1)
            load.click('blank', 1)
        
        elif load.judge(2, 0.2, sites['notifyonly'], 'notifyonly'):
            load.click_button(1, sites['notifyonly'], 'notifyonly', 2)
            load.click('harvest', 1)
            load.click('harvest', 1)
            load.click('harvest', 1)
            load.click('blank', 1)

        return_home()


def return_home():
    load.click('returnhome', 1)
    load.click('shouye', 1)
    time.sleep(5)


def jzgy():
    sites = globalvar.get_value('sites')

    # 主界面点基建
    load.click('jijian', 5)

    # 清理通知
    load.click('notifyonly', 2)
    load.click('harvest', 1)
    load.click('harvest', 1)
    load.click('harvest', 2)
    load.click('blank', 2)

    # 进驻干员
    load.click('jzzl', 2)
    load.click('blank', 2)
    
    # 滚鼠标
    load.drag('blank', 'up', 390, 2, 2)
    load.drag('blank', 'up', 390, 2, 2)
    
    # 第一个宿舍
    load.click('dormi1', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('dormipos7', 0.2)
    load.click('dormipos8', 0.2)
    load.click('dormipos9', 0.2)
    load.click('dormipos10', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)
    
    # 滚鼠标
    load.drag('blank', 'up', 390, 2, 2)
    load.drag('blank', 'up', 390, 2, 2)
    
    # 第二个宿舍
    load.click('dormi2', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('dormipos7', 0.2)
    load.click('dormipos8', 0.2)
    load.click('dormipos9', 0.2)
    load.click('dormipos10', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)
    
    # 滚鼠标
    load.drag('blank', 'up', 400, 2, 2)
    load.drag('blank', 'up', 400, 2, 2)
    
    # 第三个宿舍
    load.click('dormi3', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('dormipos7', 0.2)
    load.click('dormipos8', 0.2)
    load.click('dormipos9', 0.2)
    load.click('dormipos10', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 第四个宿舍
    load.click('dormi4', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('dormipos7', 0.2)
    load.click('dormipos8', 0.2)
    load.click('dormipos9', 0.2)
    load.click('dormipos10', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 滚鼠标
    load.drag('blank2', 'down', 310, 2, 2)

    # 倒数第一个发电站
    load.click('electric1', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 倒数第一个制造站
    load.click('produce1', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 滚鼠标
    load.drag('blank2', 'down', 485, 2, 2)

    # 倒数第一个贸易站
    load.click('trade1', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 办公室
    load.click('office', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)
    
    # 倒数第二个发电站
    load.click('electric2', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)
    
    # 滚鼠标
    load.drag('blank2', 'down', 520, 2, 2)

    # 倒数第二个制造站
    load.click('produce2', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 倒数第三个制造站
    load.click('produce3', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 加工站
    load.click('manufacture', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 滚鼠标
    load.drag('blank2', 'down', 510, 2, 2)

    # 倒数第三个发电站
    load.click('electric3', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 倒数第四个制造站
    load.click('produce4', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 倒数第二个贸易站
    load.click('trade2', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 滚鼠标
    load.drag('blank2', 'down', 500, 2, 2)

    # 会客室
    load.click('meeting', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    # 中枢
    load.click('center', 2)
    load.click('dormipos1', 0.2)
    load.click('dormipos2', 0.2)
    load.click('dormipos3', 0.2)
    load.click('dormipos4', 0.2)
    load.click('dormipos5', 0.2)
    load.click('dormipos6', 0.2)
    load.click('dormipos7', 0.2)
    load.click('dormipos8', 0.2)
    load.click('dormipos9', 0.2)
    load.click('dormipos10', 0.2)
    load.click('confirm', 1)
    if load.judge(1, 0.2, sites['hgy'], 'hgy'):
        load.click_button(1, sites['hgy'], 'hgy', 1)
    load.click('blank', 2)

    return_home()


def exterminate_dqsl(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('jiaomiezuozhan', 2)
    load.click('kaximier', 2)
    load.click('daqishilingjiaowai', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            if not load.daili():
                load.click('dailizhihui', 2)
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            while True:
                time.sleep(10)
                if load.jiaomiejieshu():
                    time.sleep(5)
                    break
            load.click('blank3', 10)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(2)
            load.click('xingdongjieshu', 2)
            time.sleep(2)
            mission += 1
    return_home()


def exterminate_bybf(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('jiaomiezuozhan', 2)
    load.click('kaximier', 2)
    load.click('beiyuanbinfengfeicheng', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            if not load.daili():
                load.click('dailizhihui', 2)
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            while True:
                time.sleep(10)
                if load.jiaomiejieshu():
                    time.sleep(5)
                    break
            load.click('blank3', 10)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(2)
            load.click('xingdongjieshu', 2)
            time.sleep(2)
            mission += 1
    return_home()


def exterminate_lmsq(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('jiaomiezuozhan', 2)
    load.click('kaximier', 2)
    load.click('daqishilingjiaowai', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            while True:
                time.sleep(10)
                if load.jiaomiejieshu():
                    time.sleep(5)
                    break
            load.click('blank3', 10)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(2)
            load.click('xingdongjieshu', 2)
            time.sleep(2)
            mission += 1
    return_home()




# 活动
def DM_4(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 2)
    load.click('zhenzhongwangshi', 2)
    load.click('DM-4',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.click_button(5, sites['xingdongjieshu'], 'xingdongjieshu', 2)
            if not load.judge(2, 1, sites['kaishixingdong'], 'kaishixingdong'):
                load.click('xingdongjieshu', 2)
            load.recognize(0.5, sites['kaishixingdong'], 'kaishixingdong')
            mission += 1
def DM_7(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 2)
    load.click('zhenzhongwangshi', 2)
    load.click('DM-7',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.click_button(5, sites['xingdongjieshu'], 'xingdongjieshu', 2)
            if not load.judge(2, 1, sites['kaishixingdong'], 'kaishixingdong'):
                load.click('xingdongjieshu', 2)
            load.recognize(0.5, sites['kaishixingdong'], 'kaishixingdong')
            mission += 1
def DM_8(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 2)
    load.click('zhenzhongwangshi', 2)
    load.click('DM-8',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.click_button(5, sites['xingdongjieshu'], 'xingdongjieshu', 2)
            if not load.judge(2, 1, sites['kaishixingdong'], 'kaishixingdong'):
                load.click('xingdongjieshu', 2)
            load.recognize(0.5, sites['kaishixingdong'], 'kaishixingdong')
            mission += 1
def SV_7_18(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 2)
    load.click('kechenganpai', 2)
    load.click('SV-7', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def TW_6_15(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 3)
    load.click('yishigaota', 2)
    load.drag('blank5', 'right', 1000, 2, 2)
    load.drag('blank5', 'right', 1000, 2, 2)
    load.drag('blank2', 'left', 500, 2, 2)
    load.click('TW-6', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def TW_7_18(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 3)
    load.click('yishigaota', 2)
    load.drag('blank5', 'right', 1000, 2, 2)
    load.drag('blank5', 'right', 1000, 2, 2)
    load.drag('blank2', 'left', 500, 2, 2)
    load.click('TW-7', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def TW_8_18(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 3)
    load.click('yishigaota', 2)
    load.drag('blank5', 'right', 1000, 2, 2)
    load.drag('blank5', 'right', 1000, 2, 2)
    load.drag('blank2', 'left', 500, 2, 2)
    load.click('TW-8', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def OF_7_30(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 3)
    load.click('zhuwutai', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank5', 'right', 500, 2, 2)
    load.click('OF-7', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def OF_8_30(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 3)
    load.click('zhuwutai', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank5', 'right', 500, 2, 2)
    load.click('OF-8', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def OF_F4(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 3)
    load.click('jianianhua', 2)
    load.click('OF-F4', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def RI_8_18(times):
    sites = globalvar.get_value('sites')
    load.click('huodong2', 3)
    load.click('daqiuzhangzhilu', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank5', 'right', 500, 2, 2)
    load.click('RI-8', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def RI_7_18(times):
    sites = globalvar.get_value('sites')
    load.click('huodong2', 3)
    load.click('daqiuzhangzhilu', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank5', 'right', 500, 2, 2)
    load.click('RI-7', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def RI_6_15(times):
    sites = globalvar.get_value('sites')
    load.click('huodong2', 3)
    load.click('daqiuzhangzhilu', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank5', 'right', 500, 2, 2)
    load.click('RI-6', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def FA_8_18(times):
    sites = globalvar.get_value('sites')
    load.click('huodong2', 3)
    load.click('shiguangchanghe', 2)
    load.click('FA-8', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def FA_7_15(times):
    sites = globalvar.get_value('sites')
    load.click('huodong2', 3)
    load.click('shiguangchanghe', 2)
    load.click('FA-7', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def FA_6_12(times):
    sites = globalvar.get_value('sites')
    load.click('huodong2', 3)
    load.click('shiguangchanghe', 2)
    load.click('FA-6', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def GT_6_15(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 3)
    load.click('dishuihuzhoubian', 2)
    load.click('GT-6', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def GT_5_15(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 3)
    load.click('dishuihuzhoubian', 2)
    load.click('GT-5', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def MN_8_18(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 4)
    load.click('dajjc', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank5', 'right', 500, 2, 2)
    load.click('MN-8', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def MN_7_18(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 4)
    load.click('dajjc', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank5', 'right', 500, 2, 2)
    load.click('MN-7', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def MN_6_15(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 4)
    load.click('dajjc', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank5', 'right', 500, 2, 2)
    load.click('MN-6', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()
def MN_5_15(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 4)
    load.click('dajjc', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank5', 'right', 500, 2, 2)
    load.click('MN-5', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def MB_6_15(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 4)
    load.click('yyjh', 2)
    load.click('MB-6', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def MB_7_18(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 4)
    load.click('yyjh', 2)
    load.click('MB-7', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def MB_8_18(times):
    sites = globalvar.get_value('sites')
    load.click('huodong', 4)
    load.click('yyjh', 2)
    load.click('MB-8', 2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


# 副本
def shieldheal(times, which):
    weekday = datetime.datetime.now().isoweekday()
    if weekday in [2, 3, 6]:
        print('Cannot operate shield and heal chip!')
    elif weekday == 1 or weekday == 4 or weekday == 5 or weekday == 7:
        if which == 1:
            xpss_1_1(times)
        if which == 2:
            xpss_1_2(times)
    


def supportpioneer(times, which):
    weekday = datetime.datetime.now().isoweekday()
    if weekday in [1, 2, 5]:
        print('Cannot operate support and pioneer chip!')
    elif weekday == 3:
        if which == 1:
            xpss_1_1(times)
        if which == 2:
            xpss_1_2(times)
    elif weekday == 4 or weekday == 6 or weekday == 7:
        if which == 1:
            xpss_2_1(times)
        if which == 2:
            xpss_2_2(times)


def wizardsnipper(times, which):
    weekday = datetime.datetime.now().isoweekday()
    if weekday in [3, 4, 7]:
        print('Cannot operate wizard and snipper chip!')
    elif weekday == 1 or weekday == 5:
        if which == 1:
            xpss_2_1(times)
        if which == 2:
            xpss_2_2(times)
    elif weekday == 2 or weekday == 6:
        if which == 1:
            xpss_1_1(times)
        if which == 2:
            xpss_1_2(times)


def guardtroop(times, which):
    weekday = datetime.datetime.now().isoweekday()
    if weekday in [1, 4, 5]:
        print('Cannot operate guard and troop chip!')
    elif weekday == 2 or weekday == 3:
        if which == 1:
            xpss_2_1(times)
        if which == 2:
            xpss_2_2(times)
    elif weekday == 6 or weekday == 7:
        if which == 1:
            xpss_3_1(times)
        if which == 2:
            xpss_3_2(times)


def redticket(times):
    weekday = datetime.datetime.now().isoweekday()
    if weekday in [2, 3, 5]:
        print('Cannot operate red ticket!')
    elif weekday == 1 or weekday == 4 or weekday == 6 or weekday == 7:
        wzcb_2(times)


def money(times):
    weekday = datetime.datetime.now().isoweekday()
    if weekday in [1, 3, 5]:
        print('Cannot operate money!')
    elif weekday == 2 or weekday == 4:
        wzcb_3(times)
    elif weekday == 6 or weekday == 7:
        wzcb_4(times)


def skill(times):
    weekday = datetime.datetime.now().isoweekday()
    if weekday in [1, 4, 6]:
        print('Cannot operate skill!')
    elif weekday == 2 or weekday == 3 or weekday == 5:
        wzcb_2(times)
    elif weekday == 7:
        wzcb_3(times)


def carbon(times):
    weekday = datetime.datetime.now().isoweekday()
    if weekday in [2, 4, 7]:
        print('Cannot operate carbon!')
    elif weekday == 1 or weekday == 3 or weekday == 5 or weekday == 6:
        wzcb_3(times)


def experience(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('wuzichoubei', 2)
    load.click('wuzichoubei1',2)
    load.click('wuzichoubeibutton',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def wzcb_2(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('wuzichoubei', 2)
    load.click('wuzichoubei2',2)
    load.click('wuzichoubeibutton',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def wzcb_3(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('wuzichoubei', 2)
    load.click('wuzichoubei3',2)
    load.click('wuzichoubeibutton',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def wzcb_4(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('wuzichoubei', 2)
    load.click('wuzichoubei4',2)
    load.click('wuzichoubeibutton',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def wzcb_5(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('wuzichoubei', 2)
    load.click('wuzichoubei5',2)
    load.click('wuzichoubeibutton',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def xpss_1_1(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('xinpiansousuo', 2)
    load.click('xinpiansousuo1',2)
    load.click('xinpiansousuo-1',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def xpss_2_1(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('xinpiansousuo', 2)
    load.click('xinpiansousuo2',2)
    load.click('xinpiansousuo-1',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def xpss_3_1(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('xinpiansousuo', 2)
    load.click('xinpiansousuo3',2)
    load.click('xinpiansousuo-1',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def xpss_4_1(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('xinpiansousuo', 2)
    load.click('xinpiansousuo4',2)
    load.click('xinpiansousuo-1',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def xpss_1_2(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('xinpiansousuo', 2)
    load.click('xinpiansousuo1',2)
    load.click('xinpiansousuo-2',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def xpss_2_2(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('xinpiansousuo', 2)
    load.click('xinpiansousuo2',2)
    load.click('xinpiansousuo-2',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def xpss_3_2(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('xinpiansousuo', 2)
    load.click('xinpiansousuo3',2)
    load.click('xinpiansousuo-2',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def xpss_4_2(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.click('xinpiansousuo', 2)
    load.click('xinpiansousuo4',2)
    load.click('xinpiansousuo-2',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def rock1_7_6best(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.click('chapter1', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('1-7',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def RMA2_10_15(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.click('chapter2', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('2-10',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def RMA7_10_18best(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('chapter7', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.click('7-10',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def Mn3_2_15(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('chapter3', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.click('3-2',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def Mn7_16_18best(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('chapter7', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.click('7-16',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def sugar4_2_18(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('chapter4', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.click('4-2',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def sugar2_5_12best(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.click('chapter2', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.click('2-5',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def device4_10_21(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('chapter4', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('4-10',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def device7_15_18best(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('chapter7', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.click('7-15',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def brick3_3_15best(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('chapter3', 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.drag('blank4', 'right', 1000, 2, 2)
    load.click('3-3',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def crystalR8_11_21best(times):
    sites = globalvar.get_value('sites')
    load.click('zuozhan', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.click('chapter8', 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank2', 'left', 1000, 2, 2)
    load.drag('blank4', 'right', 600, 2, 2)
    load.click('R8-11',2)
    if not load.daili():
        load.click('dailizhihui', 2)
    if load.daili():
        mission = 0
        while mission < times:
            load.click('kaishixingdong', 4)
            load.click('actionstart', 2)
            load.recognize(5, sites['xingdongjieshu'], 'xingdongjieshu')
            time.sleep(5)
            load.click('xingdongjieshu', 2)
            time.sleep(5)
            mission += 1
    return_home()


def underbattle(floor):
    load.click(str(floor) + 'F', 2)
    load.click('challenge', 2)
    if floor == 1:
        load.click('myteam', 2)
        load.click('huchucibianzu', 2)
    load.click('battlebegin', 2)
    while True:
        if (load.get_color(1000, 700) == [74, 139, 255] and load.get_color(1150, 700) == [74, 135, 255]) or \
           (load.get_color(1000, 700) == [74, 139, 255] and load.get_color(1150, 700) == [74, 138, 255]):
            load.click('nextstep', 8)
            load.click('nextstep', 8)
            break
        else:
            time.sleep(2)


def dixiacheng():
    load.click('adventure', 2)
    load.click('dixiacheng', 2)
    load.click('duanya', 2)
    load.click('confirmOK', 10)
    for i in range(10):
        underbattle(i+1)
    load.click('myhomepage', 5)


def niudan():
    load.click('niudan', 5)
    load.click('putongniudan', 5)
    load.click('chouqu', 2)
    load.click('confirmOK', 10)
    load.click('OKbutton', 2)
    load.click('myhomepage', 5)


def dianzan():
    load.click('hanghui', 3)
    load.click('chengyuan', 3)
    load.click('dianzan', 3)
    load.click('dianzanOK', 3)
    load.click('myhomepage', 5)


def jingjichang():
    load.click('adventure', 2)
    load.click('zhandoujjc', 2)
    load.click('jjcblank', 2)
    load.click('jjccollect', 2)
    load.click('battlebegin', 2)
    load.click('jjcpick', 2)
    load.click('battlebegin', 2)
    while True:
        if (load.get_color(1000, 700) == [74, 139, 255] and load.get_color(1150, 700) == [74, 135, 255]) \
            or (load.get_color(1000, 700) == [82, 98, 144] and load.get_color(1150, 700) == [79, 96, 144]) \
            or (load.get_color(1000, 700) == [74, 139, 255] and load.get_color(1150, 700) == [74, 138, 255]) \
            or (load.get_color(1000, 700) == [81, 99, 140] and load.get_color(1150, 700) == [79, 98, 139]) \
            or (load.get_color(1000, 700) == [79, 95, 137] and load.get_color(1150, 700) == [79, 95, 136]) \
            or (load.get_color(1000, 700) == [82, 94, 141] and load.get_color(1150, 700) == [79, 94, 141]):
            load.click('nextstep', 8)
            break
        else:
            time.sleep(2)
    load.click('myhomepage', 5)
    load.click('adventure', 2)
    load.click('gongzhujjc', 2)
    load.click('jjcblank', 2)
    load.click('jjccollect', 2)
    load.click('battlebegin', 2)
    load.click('jjcpick', 2)
    load.click('battlebegin', 2)
    load.click('battlebegin', 2)
    load.click('battlebegin', 2)
    while True:
        if load.get_color(1000, 700) == [113, 109, 137] and load.get_color(1150, 700) == [100, 108, 136] \
            or (load.get_color(1000, 700) == [107, 112, 136] and load.get_color(1150, 700) == [107, 112, 135]) \
            or (load.get_color(1000, 700) == [108, 113, 137] and load.get_color(1150, 700) == [108, 112, 137]) \
            or (load.get_color(1000, 700) == [113, 110, 138] and load.get_color(1150, 700) == [100, 109, 138]):
            load.click('nextstep', 8)
            break
        else:
            time.sleep(2)
    load.click('myhomepage', 5)


def gonghuizhijia():
    load.click('gonghuizhijia', 3)
    load.click('quanbushouqu', 3)
    load.click('battlebegin', 2)
    load.click('myhomepage', 5)


def collectrewards():
    load.click('tasks', 3)
    load.click('battlebegin', 2)
    load.click('battlebegin', 2)
    load.click('myhomepage', 5)
    load.click('gifts', 3)
    load.click('collectgifts', 2)
    load.click('giftsOK', 2)
    load.click('collectgifts', 2)
    load.click('myhomepage', 5)


def tansuo():
    load.click('adventure', 2)
    load.click('tansuo', 2)
    load.click('jyzgk', 2)
    load.click('tansuolv5', 2)
    load.click('timeplus', 2)
    load.click('saodang', 2)
    load.click('confirmOK', 8)
    load.click('saodangwancheng', 2)
    load.click('managk', 2)
    load.click('tansuolv5', 2)
    load.click('timeplus', 2)
    load.click('saodang', 2)
    load.click('confirmOK', 8)
    load.click('saodangwancheng', 2)
    load.click('myhomepage', 5)


def sjdc():
    load.click('adventure', 2)
    load.click('sjdc', 2)
    load.click('sjdc1', 2)
    load.click('timeplus', 2)
    load.click('timeplus', 2)
    load.click('timeplus', 2)
    load.click('timeplus', 2)
    load.click('saodang', 2)
    load.click('confirmOK', 10)
    load.click('saodangwancheng', 2)
    load.click('myhomepage', 5)
    load.click('myhomepage', 5)
    load.click('adventure', 2)
    load.click('sjdc', 2)
    load.click('sjdc2', 2)
    load.click('timeplus', 2)
    load.click('timeplus', 2)
    load.click('timeplus', 2)
    load.click('timeplus', 2)
    load.click('saodang', 2)
    load.click('confirmOK', 8)
    load.click('saodangwancheng', 2)
    load.click('myhomepage', 5)
    load.click('myhomepage', 5)


def goumaimana():
    load.click('goumaimana', 2)
    load.click('goumai10', 2)
    load.click('confirmOK', 2)
    load.click('goumaicancel', 2)
    