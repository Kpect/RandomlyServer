#coding=utf-8
#import libs 
import sys
import Project1_cmd
import Project1_sty
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
class  Project1:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.G_UICommandDictionary[uiName]=Project1_cmd
        Fun.Register(uiName,'root',root)
        style = Project1_sty.SetupStyle()
        if isTKroot == True:
            root.title("RandomlyServer")
            root.overrideredirect(True)
            Fun.WindowDraggable(root,True,0,'#00ffff')
            Fun.CenterDlg(uiName,root,720,513)
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
        LabelButton_3= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'LabelButton_3',LabelButton_3,'关闭按钮')
        LabelButton_3.SetText("×")
        LabelButton_3.SetBGColor("#333333")
        LabelButton_3.SetFGColor("#ffffff")
        LabelButton_3_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_3.SetFont(LabelButton_3_TitleFont)
        LabelButton_3.SetBGColor_Hover("#f26223")
        LabelButton_3.SetFGColor_Hover("#ffffff")
        LabelButton_3.SetBGColor_Click("#e9500e")
        LabelButton_3.SetFGColor_Click("#ffffff")
        Fun.SetControlPlace(uiName,'LabelButton_3',679,0,41,38)
        LabelButton_3.SetCommandFunction(Project1_cmd.关闭按钮_onCommand,self.uiName,"LabelButton_3")
        Label_4 = tkinter.Label(Form_1,text="RandomlyServer正在运行")
        Fun.Register(uiName,'Label_4',Label_4,'大标题')
        Fun.SetControlPlace(uiName,'Label_4',156,83,405,48)
        Label_4.configure(bg = "#333333")
        Label_4.configure(fg = "#ffffff")
        Label_4.configure(relief = "flat")
        Label_4_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Label_5 = tkinter.Label(Form_1,text="欢迎使用")
        Fun.Register(uiName,'Label_5',Label_5,'文本1')
        Fun.SetControlPlace(uiName,'Label_5',245,140,230,35)
        Label_5.configure(bg = "#333333")
        Label_5.configure(fg = "#ffa924")
        Label_5.configure(relief = "flat")
        Label_5_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_5.configure(font = Label_5_Ft)
        Label_6 = tkinter.Label(Form_1,text="服务器")
        Fun.Register(uiName,'Label_6',Label_6,'Label_3')
        Fun.SetControlPlace(uiName,'Label_6',61,351,200,48)
        Label_6.configure(bg = "#333333")
        Label_6.configure(fg = "#ccbb99")
        Label_6.configure(relief = "flat")
        Label_6_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_6.configure(font = Label_6_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Project1_cmd.Form_1_onLoad(uiName)
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
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Project1(root)
    root.mainloop()
