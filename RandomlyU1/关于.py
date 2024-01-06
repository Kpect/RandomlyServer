#coding=utf-8
#import libs
import 关于_cmd
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class 关于:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.G_UICommandDictionary[uiName]=关于_cmd
        if isTKroot == True:
            root.title("Form1")
            root.wm_attributes("-topmost",1)
            root.geometry("960x640")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 960,height = 640)
        Form_1.configure(bg = "#efefef")
        Fun.G_RootSize = [960,640]
        Fun.G_UIElementDictionary['root']=root
        Fun.G_UIElementDictionary['Form_1']=Form_1
        #Create the elements of root
        #Inital all element's Data
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Escape>',self.Escape)  

    #GetRootSize
    def GetRootSize(self):
        return Fun.G_RootSize[0],Fun.G_RootSize[1]

    #GetAllElement
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.__class__.__name__]

    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName)

    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            Fun.DestroyUI(self.uiName)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = 关于(root)
    root.mainloop()
