#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

import threading
from win10toast import ToastNotifier
import requests
from tqdm import tqdm
import yaml
from urllib.parse import urlparse
from retrying import retry
# 定义show_notification,使用此弹出系统消息
def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=5)
#程序启动时
def Form_1_onLoad(uiName):
    threading.Thread(target=show_notification, args=("Randomly", "欢迎使用！")).start() 
    pass
#关闭按钮
    pass
#关闭按钮
#Button '❌'s Event :Button-1
def Button_3_onButton1(event,uiName,widgetName):
    sys.exit()
    pass


