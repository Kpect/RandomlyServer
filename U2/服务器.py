#coding=utf-8
#import libs 
import sys
import 服务器_cmd
import 服务器_sty
import Fun
import EXUIControl
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  服务器:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.G_UICommandDictionary[uiName]=服务器_cmd
        Fun.Register(uiName,'root',root)
        style = 服务器_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            root.overrideredirect(True)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            Fun.CenterDlg(uiName,root,720,513)
            root.wm_attributes("-topmost",1)
            root['background'] = '#333333'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 720)
        Form_1.configure(height = 513)
        Form_1.configure(bg = "#333333")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[720,513]
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="服务器列表")
        Fun.Register(uiName,'Label_2',Label_2,'服务器列表大标题')
        Fun.SetControlPlace(uiName,'Label_2',-26,12,200,31)
        Label_2.configure(bg = "#333333")
        Label_2.configure(fg = "#ffffff")
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=13,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Label_3 = tkinter.Label(Form_1,text="在列表内选择一个服务器后,将会自动下载到此软件同目录下")
        Fun.Register(uiName,'Label_3',Label_3,'介绍文本')
        Fun.SetControlPlace(uiName,'Label_3',0,59,406,30)
        Label_3.configure(bg = "#333333")
        Label_3.configure(fg = "#aaaaaa")
        Label_3.configure(relief = "flat")
        Entry_5= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_5',Entry_5,'Entry_1')
        Entry_5.SetBGColor("#333333")
        Entry_5.SetFGColor("#000000")
        Entry_5.SetTipText("搜索服务器...")
        Entry_5.SetTipFGColor("#888888")
        Entry_5.SetRelief("flat")
        Entry_5.SetLeftIcon("搜索.png")
        Fun.SetControlPlace(uiName,'Entry_5',480,65,213,24)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
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
            Fun.SetControlPlace(uiName,'Label_2',-26,12,200,31)
            pass
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = 服务器(root)
    root.mainloop()
