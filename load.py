import win32gui
import win32api
import win32con
import time
import ctypes
import globalvar
import pyautogui


def get_color(x, y):
    gdi32 = ctypes.windll.gdi32
    user32 = ctypes.windll.user32
    hdc = user32.GetDC(None)
    pixel = gdi32.GetPixel(hdc, x, y)
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return [r, g, b]


def load_global():
    pointval = {}
    pointval['mnq'] = [[21, 105, 144], [0, 167, 255], [111, 191, 226], [255, 242, 229], [208, 225, 229], [218, 230, 231], [255, 242, 232], [54, 170, 224], [153, 206, 229], [255, 245, 235], [216, 229, 233], [229, 235, 236], [237, 238, 235], [54, 172, 226], [190, 219, 232], [243, 238, 234], [215, 228, 233], [255, 251, 233], [134, 205, 236], [0, 157, 249]]
    pointval['mrfz'] = [[124, 87, 78], [160, 125, 110], [232, 211, 186], [237, 217, 192], [225, 207, 184], [218, 212, 193], [229, 215, 196], [246, 229, 206], [248, 231, 206], [249, 233, 208], [249, 233, 209], [249, 232, 208], [248, 230, 205], [248, 229, 204], [244, 223, 199], [244, 222, 198], [248, 229, 205], [249, 232, 207], [241, 226, 205], [191, 193, 183]]
    pointval['start'] = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [43, 37, 0], [193, 163, 2], [255, 216, 2], [253, 214, 2], [247, 209, 2], [213, 180, 2], [157, 133, 1], [95, 81, 1], [34, 29, 0], [2, 2, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    pointval['kshx'] = [[123, 123, 123], [111, 111, 111], [108, 108, 108], [109, 109, 109], [109, 109, 109], [124, 124, 124], [152, 152, 152], [130, 130, 130], [99, 99, 99], [87, 87, 87], [118, 118, 118], [190, 190, 190], [163, 163, 163], [94, 94, 94], [180, 180, 180], [232, 232, 232], [115, 115, 115], [131, 131, 131], [190, 190, 190], [146, 146, 146]]
    pointval['crossgg'] = [[168, 168, 168], [194, 194, 194], [195, 195, 195], [195, 195, 195], [189, 189, 189], [160, 160, 160], [111, 111, 111], [84, 84, 84], [95, 95, 95], [133, 133, 133], [181, 181, 181], [196, 196, 196], [196, 196, 196], [196, 196, 196], [190, 190, 190], [160, 160, 160], [109, 109, 109], [85, 85, 85], [90, 90, 90], [91, 91, 91]]
    pointval['crossqd'] = [[96, 96, 96], [135, 135, 135], [177, 177, 177], [195, 195, 195], [196, 196, 196], [193, 193, 193], [191, 191, 191], [153, 153, 153], [102, 102, 102], [78, 78, 78], [92, 92, 92], [89, 89, 89], [132, 132, 132], [182, 182, 182], [195, 195, 195], [196, 196, 196], [195, 195, 195], [192, 192, 192], [162, 162, 162], [104, 104, 104]]
    pointval['notify'] = [[47, 168, 223], [47, 168, 223], [47, 168, 223], [47, 168, 223], [47, 168, 223], [47, 168, 223], [47, 168, 223], [47, 168, 223], [47, 168, 223], [47, 168, 223], [47, 168, 223], [47, 168, 223], [47, 168, 222], [48, 168, 222], [50, 168, 222], [103, 191, 230], [222, 241, 249], [253, 254, 254], [255, 255, 255], [255, 255, 255]]
    pointval['notifyonly'] = [[43, 164, 219], [43, 164, 219], [43, 164, 219], [43, 164, 219], [43, 164, 219], [43, 164, 219], [43, 164, 219], [43, 164, 219], [43, 164, 219], [43, 164, 219], [43, 164, 219], [43, 164, 218], [43, 164, 217], [44, 164, 217], [52, 165, 219], [113, 194, 233], [233, 247, 252], [255, 255, 255], [255, 255, 255], [255, 255, 255]]
    pointval['hgy'] = [[19, 107, 146], [18, 110, 147], [21, 112, 149], [20, 111, 148], [18, 107, 146], [23, 110, 151], [22, 111, 152], [15, 106, 147], [18, 106, 144], [19, 107, 143], [26, 113, 150], [33, 121, 158], [28, 116, 155], [23, 110, 151], [23, 107, 148], [21, 104, 145], [22, 108, 146], [28, 113, 149], [70, 140, 171], [100, 159, 187]]
    pointval['shouyejiance'] = [[219, 221, 221], [219, 222, 221], [219, 222, 221], [218, 221, 220], [217, 219, 219], [216, 219, 219], [217, 220, 220], [225, 227, 227], [237, 240, 240], [250, 253, 254], [251, 253, 254], [250, 254, 254], [232, 234, 234], [226, 228, 229], [220, 224, 226], [229, 230, 230], [228, 229, 229], [228, 229, 229], [228, 229, 229], [228, 229, 229]]
    pointval['dailizhihui'] = [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [253, 253, 253], [242, 242, 242], [228, 228, 228], [214, 214, 214], [206, 206, 207], [198, 198, 198], [194, 194, 195], [189, 189, 189], [183, 183, 184], [179, 179, 179], [174, 174, 175], [171, 171, 171], [167, 167, 168], [168, 168, 168]]
    pointval['jijianbutton'] = [[211, 213, 215], [211, 213, 215], [211, 213, 215], [214, 216, 218], [229, 231, 233], [234, 236, 237], [234, 236, 237], [234, 236, 238], [234, 236, 238], [234, 236, 238], [234, 236, 237], [234, 236, 237], [234, 236, 237], [234, 236, 237], [234, 236, 237], [234, 236, 237], [234, 235, 237], [233, 235, 236], [236, 236, 236], [236, 236, 236]]
    pointval['kaishixingdong'] = [[80, 79, 79], [80, 79, 78], [80, 79, 78], [80, 79, 78], [80, 79, 78], [80, 79, 78], [80, 79, 78], [79, 78, 78], [79, 78, 78], [79, 78, 77], [79, 78, 77], [78, 78, 77], [78, 77, 77], [78, 77, 77], [78, 77, 77], [78, 77, 76], [78, 77, 76], [78, 77, 76], [78, 76, 75], [78, 76, 75]]
    pointval['actionstart'] = [[144, 85, 65], [205, 161, 148], [140, 98, 85], [102, 60, 47], [166, 117, 106], [199, 163, 152], [124, 65, 50], [107, 41, 25], [180, 128, 115], [205, 157, 142], [122, 60, 44], [87, 34, 18], [147, 103, 87], [192, 150, 136], [125, 84, 71], [110, 69, 60], [215, 174, 165], [175, 131, 123], [112, 69, 57], [142, 102, 86]]
    pointval['xingdongjieshu'] = [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]
    globalvar.set_value('pointval', pointval)
    
    titles = set()
    globalvar.set_value('titles', titles)
    
    size = []
    win32gui.EnumWindows(foo, 0)
    lt = [t for t in titles if t]
    lt.sort()
    for t in lt:
        if(t.find('MuMu模拟器')) >= 0:
            hwnd = win32gui.FindWindow(None, t)
            size = win32gui.GetWindowRect(hwnd)
            globalvar.set_value('size', size)
    
    sites = {}
    # 模拟器界面
    sites['mnq'] = (260, 110)
    sites['mrfz'] = (190, 180)
    sites['redive'] = (400, 180)
    sites['start'] = (620, 690)
    sites['kshx'] = (620, 530)

    # 公告和签到
    sites['crossgg'] = (1200, 95)
    sites['crossqd'] = (1165, 115)
    sites['shutnotify'] = (620, 660)

    # 公主连结冒险
    sites['adventure'] = (600, 700)
    sites['dixiacheng'] = (1150, 200)
    sites['duanya'] = (770, 350)
    sites['confirmOK'] = (760, 520)
    sites['myteam'] = (1120, 150)
    sites['huchucibianzu'] = (1020, 260)
    sites['battlebegin'] = (1080, 620)
    sites['challenge'] = (1100, 630)
    sites['nextstep'] = (1000, 700)
    sites['1F'] = (820, 480)
    sites['2F'] = (475, 350)
    sites['3F'] = (800, 350)
    sites['4F'] = (550, 350)
    sites['5F'] = (240, 350)
    sites['6F'] = (620, 350)
    sites['7F'] = (950, 350)
    sites['8F'] = (590, 350)
    sites['9F'] = (320, 350)
    sites['10F'] = (800, 350)
    sites['skip'] = (1200, 70)
    sites['myhomepage'] = (120, 725)
    sites['niudan'] = (950, 700)
    sites['putongniudan'] = (1180, 130)
    sites['chouqu'] = (930, 500)
    sites['OKbutton'] = (620, 600)
    sites['hanghui'] = (890, 600)
    sites['chengyuan'] = (300, 490)
    sites['dianzan'] = (1070, 290)
    sites['dianzanOK'] = (620, 510)
    sites['zhandoujjc'] = (750, 560)
    sites['gongzhujjc'] = (1070, 560)
    sites['jjcblank'] = (80, 160)
    sites['jjcpick'] = (850, 250)
    sites['jjccollect'] = (380, 480)
    sites['gonghuizhijia'] = (800, 700)
    sites['quanbushouqu'] = (1160, 590)
    sites['tasks'] = (1080, 600)
    sites['gifts'] = (1180, 600)
    sites['collectgifts'] = (1080, 650)
    sites['giftsOK'] = (760, 660)
    sites['tansuo'] = (950, 200)
    sites['jyzgk'] = (750, 340)
    sites['tansuolv5'] = (930, 230)
    sites['managk'] = (1050, 340)
    sites['timeplus'] = (1135, 465)
    sites['saodang'] = (980, 465)
    sites['saodangwancheng'] = (620, 650)
    sites['goumaimana'] = (242, 116)
    sites['goumai10'] = (760, 650)
    sites['goumaicancel'] = (200, 650)
    sites['sjdc'] = (950, 400)
    sites['sjdc1'] = (900, 370)
    sites['sjdc2'] = (900, 225)

    
    # 基建
    sites['jijian'] = (1000, 650)
    sites['jijianbutton'] = (1095, 610)
    sites['notify'] = (1150, 170)
    sites['notifyonly'] = (1150, 125)
    sites['harvest'] = (240, 710)
    sites['production'] = (165, 430)
    sites['maxproduce'] = (935, 235)
    sites['zhixinggenggai'] = (920, 615)
    sites['production1'] = (110, 240)
    sites['production2'] = (110, 400)
    sites['production3'] = (110, 480)
    

    # 进驻总览界面
    sites['jzzl'] = (120, 150)
    #================================#
    sites['dormi1'] = (650, 200)
    sites['dormi2'] = (650, 155)
    sites['dormi3'] = (650, 255)
    sites['dormi4'] = (650, 620)
    #================================#
    sites['electric1'] = (650, 425)
    sites['electric2'] = (650, 160)
    sites['electric3'] = (650, 465)
    #================================#
    sites['produce1'] = (650, 250)
    sites['produce2'] = (650, 570)
    sites['produce3'] = (650, 410)
    sites['produce4'] = (650, 315)
    #================================#
    sites['trade1'] = (650, 670)
    sites['trade2'] = (650, 160)
    sites['meeting'] = (650, 390)
    sites['center'] = (650, 230)
    sites['office'] = (650, 470)
    sites['manufacture'] = (650, 220)
    
    # 换干员界面
    sites['dormipos1'] = (450, 250)
    sites['dormipos2'] = (450, 500)
    sites['dormipos3'] = (600, 250)
    sites['dormipos4'] = (600, 500)
    sites['dormipos5'] = (750, 250)
    sites['dormipos6'] = (750, 500)
    sites['dormipos7'] = (900, 250)
    sites['dormipos8'] = (900, 500)
    sites['dormipos9'] = (1050, 250)
    sites['dormipos10'] = (1050, 500)
    sites['confirm'] = (1150, 690)
    sites['hgy'] = (900, 700)

    # 主页
    sites['return'] = (90, 70)
    sites['returnhome'] = (260, 70)
    sites['shouye'] = (90, 200)
    sites['shouyejiance'] = (815, 375)

    # 作战
    sites['zuozhan'] = (940, 190)
    #================================#
    sites['chapter1'] = (800, 400)
    sites['chapter2'] = (1200, 400)
    sites['chapter3'] = (600, 400)
    sites['chapter4'] = (1000, 400)
    sites['chapter7'] = (450, 400)
    sites['chapter8'] = (950, 400)
    sites['1-7'] = (1000, 250)
    sites['2-10'] = (620, 460)
    sites['2-5'] = (1100, 450)
    sites['3-2'] = (900, 360)
    sites['3-3'] = (1150, 350)
    sites['4-2'] = (800, 470)
    sites['4-10'] = (600, 370)
    sites['7-10'] = (1220, 290)
    sites['7-15'] = (700, 390)
    sites['7-16'] = (900, 280)
    sites['R8-9'] = (250, 265)
    sites['R8-10'] = (470, 265)
    sites['R8-11'] = (680, 265)
    sites['M8-7'] = (250, 490)
    sites['M8-8'] = (680, 490)
    #================================#
    sites['wuzichoubei'] = (225, 675)
    sites['wuzichoubei1'] = (180, 350)
    sites['wuzichoubei2'] = (450, 350)
    sites['wuzichoubei3'] = (700, 350)
    sites['wuzichoubei4'] = (950, 350)
    sites['wuzichoubei5'] = (1200, 350)
    sites['wuzichoubeibutton'] = (920, 210)
    #================================#
    sites['xinpiansousuo'] = (375, 675)
    sites['xinpiansousuo1'] = (230, 350)
    sites['xinpiansousuo2'] = (490, 350)
    sites['xinpiansousuo3'] = (750, 350)
    sites['xinpiansousuo4'] = (1000, 350)
    sites['xinpiansousuo-1'] = (395, 450)
    sites['xinpiansousuo-2'] = (830, 280)
    #================================#
    sites['jiaomiezuozhan'] = (525, 675)
    sites['longmenwaihuan'] = (725, 520)
    sites['kaximier'] = (650, 400)
    sites['daqishilingjiaowai'] = (500, 400)
    sites['beiyuanbinfengfeicheng'] = (260, 400)
    sites['jiaomiejieshu1'] = (900, 400)
    sites['jiaomiejieshu2'] = (250, 370)
    sites['dailizhihui'] = (1030, 610)
    sites['kaishixingdong'] = (1110, 675)
    sites['actionstart'] = (1060, 600)
    sites['xingdongjieshu'] = (340, 650)
    #================================#
    sites['huodong'] = (1150, 180)
    sites['huodong2'] = (1150, 250)
    sites['daqiuzhangzhilu'] = (1100, 370)
    sites['zhenzhongwangshi'] = (750, 550)
    sites['kechenganpai'] = (180, 480)
    sites['yishigaota'] = (1200, 390)
    sites['zhuwutai'] = (1000, 370)
    sites['jianianhua'] = (1000, 450)
    sites['shiguangchanghe'] = (180, 480)
    sites['dishuihuzhoubian'] = (950, 410)
    sites['dajjc'] = (1000, 450)
    sites['yyjh'] = (1080, 200)
    sites['SV-7'] = (1090, 240)
    sites['DM-4'] = (560, 350)
    sites['DM-7'] = (895, 400)
    sites['DM-8'] = (1000, 250)
    sites['TW-6'] = (300, 485)
    sites['TW-7'] = (550, 390)
    sites['TW-8'] = (850, 390)
    sites['OF-7'] = (600, 360)
    sites['OF-8'] = (850, 470)
    sites['OF-F4'] = (980, 340)
    sites['RI-8'] = (1030, 430)
    sites['RI-7'] = (780, 320)
    sites['RI-6'] = (370, 500)
    sites['FA-8'] = (1120, 270)
    sites['FA-7'] = (1000, 400)
    sites['FA-6'] = (900, 510)
    sites['GT-6'] = (930, 290)
    sites['GT-5'] = (820, 400)
    sites['MN-8'] = (930, 330)
    sites['MN-7'] = (420, 210)
    sites['MN-6'] = (230, 320)
    sites['MN-5'] = (45, 385)
    sites['MB-6'] = (815, 420)
    sites['MB-7'] = (815, 545)
    sites['MB-8'] = (1100, 545)



    # 其他
    sites['blank'] = (1220, 710)
    sites['blank2'] = (1220, 150)
    sites['blank3'] = (1220, 400)
    sites['blank4'] = (100, 600)
    sites['blank5'] = (100, 400)
  

    globalvar.set_value('sites', sites)


def foo(hwnd, mouse):
	titles = globalvar.get_value('titles')
	if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
		titles.add(win32gui.GetWindowText(hwnd))
		globalvar.set_value('titles', titles)


def confirm_color(x1, x2, y):
    color = []
    for x in range(x1, x2):
        color.append(get_color(x, y))
    return color


def recognize(refreshrate, site, name):
    pointval = globalvar.get_value('pointval')
    while True:
        time.sleep(refreshrate)
        if confirm_color(site[0] - 10, site[0] + 10, site[1]) == pointval[name]:
            break


def click_button(refreshrate, site, name, sleep):
    size = globalvar.get_value('size')
    recognize(refreshrate, site, name)
    win32api.SetCursorPos([size[0] + site[0], size[1] + site[1]])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(sleep)


def judge(wait, refreshrate, site, name):
    pointval = globalvar.get_value('pointval')
    t = 0
    while t <= wait:
        if confirm_color(site[0] - 10, site[0] + 10, site[1]) == pointval[name]:
            time.sleep(1)
            return True
        else:
            time.sleep(refreshrate)
            t += refreshrate
    return False


def click(name, sleep):
    size = globalvar.get_value('size')
    sites = globalvar.get_value('sites')
    win32api.SetCursorPos([size[0] + sites[name][0], size[1] + sites[name][1]])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(sleep)


def roll(direction, sleep):
    if direction == 'down':
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1)
        time.sleep(sleep)
    elif direction == 'up':
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1)
        time.sleep(sleep)
    

def drag(name, direction, route, speed, sleep):
    size = globalvar.get_value('size')
    sites = globalvar.get_value('sites')
    win32api.SetCursorPos([size[0] + sites[name][0], size[1] + sites[name][1]])
    if direction == 'up':
        dx = 0
        dy = -1
    if direction == 'down':
        dx = 0
        dy = 1
    if direction == 'left':
        dx = -1
        dy = 0
    if direction == 'right':
        dx = 1
        dy = 0
    pyautogui.dragRel(dx * route, dy * route, speed)
    time.sleep(sleep)
    

def daili():
    sites = globalvar.get_value('sites')
    color = get_color(sites['dailizhihui'][0], sites['dailizhihui'][1])
    if color[0] + color[1] + color[2] < 300:
        return False
    else:
        return True


def jiaomiejieshu():
    sites = globalvar.get_value('sites')
    color = [0, 0]
    color[0] = get_color(sites['jiaomiejieshu1'][0], sites['jiaomiejieshu1'][1])
    color[1] = get_color(sites['jiaomiejieshu2'][0], sites['jiaomiejieshu2'][1])
    if color[0] == [14, 12, 10] and color[1] == [0, 152, 220]:
        return True
    else:
        return False

