import win32gui
import win32api
import win32con
import time
import ctypes
import globalvar
import func
import load
import PIL
import math
import operator
import functools
import pytesseract



def grab_image(bound):
    image = PIL.ImageGrab.grab(bound)
    return image


def compare_image(sample, pic):
    image1 = PIL.Image.open(sample)
    image2 = grab_image(pic)
    #把图像对象转换为直方图数据，存在list h1、h2 中
    h1 = image1.histogram()
    h2 = image2.histogram()
    result = math.sqrt(functools.reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
    return result


def judge(name):
    imagebound = globalvar.get_value('imagebound')
    sample = 'D:/明日方舟/脚本/pic/' + name + '.png'
    pic = imagebound[name]
    print(compare_image(sample, pic))


def recognize(name):
    imagebound = globalvar.get_value('imagebound')
    pic = imagebound[name]
    image = grab_image(pic)
    pytesseract.pytesseract.tesseract_cmd = 'D:/Tesseract/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(image, lang='chi_sim')
    return text


def text_judge(name, text):
    if recognize(name).strip() == text:
        return True
    if recognize(name).strip != text:
        return False


def load_image():
    imagebound = {}
    imagebound['编队'] = (665, 328, 886, 430)
    imagebound['倍速'] = (1030, 60, 1096, 118)
    imagebound['行动结束'] = (20, 590, 400, 690)
    imagebound['代理指挥'] = (1010, 590, 1205, 630)
    imagebound['芯片搜索二'] = (415, 495, 565, 535)
    globalvar.set_value('imagebound', imagebound)