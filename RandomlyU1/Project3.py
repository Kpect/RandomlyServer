#coding=utf-8
#import libs 
import yaml
import requests
import sys
import Project3_cmd
import Project3_sty
import Fun
import EXUIControl
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import os
import tkinter
import tkinter as tk
from tkinter import END
from ttkthemes import ThemedTk
from   tkinter import *
import tkinter.ttk
import tkinter.font

# 定义show_notification,使用此弹出系统消息
def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=5)


# 定义读取服务器方法
def readserver():
    server_list = {}
    with open("room.yml", 'r', encoding='utf-8') as file:
        server_list = yaml.safe_load(file)
    return server_list


# 定义获取服务器列表方法
def getrooms():
    server_list_url = "https://zlbox.jiangyin14.top/room.yml"
    response = requests.get(server_list_url)
    server_list = {}
    if response.status_code == 200:
        server_list = yaml.safe_load(response.text)
    return server_list


# 定义刷新服务器列表方法
def refreshservers(listbox):
    server_list = getrooms()
    print("server_list:", server_list)  # 打印 server_list，确认内容
    if server_list:
        selected = listbox.curselection()  # 获取所有选中项的索引
        for i in selected[::-1]:  # 倒序遍历选中项的索引
            listbox.delete(i)  # 逐一删除选中项
        for name, url in server_list.items():
            print(f"Inserting into listbox: {name} - {url}")  # 打印插入的键和值，确认内容
            listbox.insert(END, name)  # 只插入服务器名，不显示URL
    else:
        threading.Thread(target=show_notification, args=("错误", "读取失败")).start()
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Project3:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.G_UICommandDictionary[uiName]=Project3_cmd
        Fun.Register(uiName,'root',root)
        style = Project3_sty.SetupStyle()
        if isTKroot == True:
            root.title("Project3")
            root.overrideredirect(True)
            Fun.WindowDraggable(root,True,0,'#400040')
            root.resizable(False,False)
            Fun.CenterDlg(uiName,root,700,595)
            root['background'] = '#ffffff'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 700)
        Form_1.configure(height = 595)
        Form_1.configure(bg = "#ffffff")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[700,595]
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="Randomly")
        Fun.Register(uiName,'Label_2',Label_2,'Label_1')
        Fun.SetControlPlace(uiName,'Label_2',0,6,174,48)
        Label_2.configure(bg = "#ffffff")
        Label_2.configure(fg = "#5b0df8")
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='Lao UI', size=24,weight='bold',slant='italic',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Button_3 = tkinter.Button(Form_1,text="❌")
        Fun.Register(uiName,'Button_3',Button_3,'Button_1')
        Fun.SetControlPlace(uiName,'Button_3',658,0,42,48)
        Button_3.configure(bg = "#ffffff")
        Button_3.configure(activebackground = "#e1031e")
        Button_3.configure(activeforeground = "#ffffff")
        Button_3.configure(relief = "flat")
        Button_3.bind("<Button-1>",Fun.EventFunction_Adaptor(Project3_cmd.Button_3_onButton1,uiName=uiName,widgetName="Button_3"))
        Entry_5= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_5',Entry_5,'Entry_1')
        Entry_5.SetBGColor("#ffffff")
        Entry_5.SetFGColor("#000000")
        Entry_5.SetTipText("搜索服务器")
        Entry_5.SetTipFGColor("#888888")
        Entry_5.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_5',307,30,331,24)
        Frame_8 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'Frame_8',Frame_8,'Frame_1')
        Fun.SetControlPlace(uiName,'Frame_8',114,87,469,450)
        Frame_8.configure(bg = "#cfcfcf")
        Frame_8.configure(relief = "flat")
        Fun.SetRoundedRectangle(Frame_8,30,30)
        ListBox_10 = tkinter.Listbox(Frame_8)
        ListBox_10_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        ListBox_10.configure(font = ListBox_10_Ft)
        Fun.Register(uiName,'ListBox_10',ListBox_10,'ListBox_1')
        Fun.SetControlPlace(uiName,'ListBox_10',14,10,441,429)
        ListBox_10.configure(bg = "#cfcfcf")
        ListBox_10.configure(fg = "SystemButtonText")
        ListBox_10.configure(exportselection=False)
        ListBox_10.configure(selectmode = "BROWSE")
        ListBox_10.configure(relief = "flat")
        ListBox_10_VScrollbar = tkinter.ttk.Scrollbar(ListBox_10,orient=tkinter.VERTICAL)
        ListBox_10_VScrollbar.place(x = 421,y = 0,width = 20,height = 429)
        ListBox_10_VScrollbar.config(command = ListBox_10.yview)
        ListBox_10.config(yscrollcommand = ListBox_10_VScrollbar.set)
        refreshservers(ListBox_10)
        ListBox_10.after(60000, refreshservers, ListBox_10)  # 每60秒自动刷新一次
        Fun.Register(uiName,'ListBox_10_VScrollbar',ListBox_10_VScrollbar)
        Progress_9 = tkinter.ttk.Progressbar(Form_1)
        Fun.Register(uiName,'Progress_9',Progress_9,'Progress_1')
        Fun.SetControlPlace(uiName,'Progress_9',84,553,554,30)
        Progress_9.configure(orient = tkinter.HORIZONTAL)
        Progress_9.configure(mode = "determinate")
        Progress_9.configure(maximum = "100")
        Progress_9.configure(value = "50")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Project3_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Escape>',self.Escape)  
    def GetRootSize(self):
        return Fun.G_RootSize[0],Fun.G_RootSize[1]
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.__class__.__name__]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName)

    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            Fun.G_RootSize=[event.width,event.height]
            uiName = self.uiName
            pass
        ListBox_10= Fun.GetElement(self.uiName,'ListBox_10')
        if event.widget == ListBox_10:
            ListBox_10_VScrollbar= Fun.GetElement(self.uiName,'ListBox_10_VScrollbar')
            if ListBox_10_VScrollbar:
                ListBox_10_VScrollbar.place(x = ListBox_10.winfo_width()-20,y = 0,width = 20,height = ListBox_10.winfo_height())
#Create the root of Kinter 
if  __name__ == '__main__':
    root = ThemedTk(theme="arc", toplevel=True, themebg=True)
    MyDlg = Project3(root)
    root.mainloop()
