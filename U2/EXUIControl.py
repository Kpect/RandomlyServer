# 版权声明：日历控件参考CSDN博主「我的眼_001」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原作者出处链接及声明
# 原文链接：https://blog.csdn.net/wodeyan001/article/details/86703034
# -*- coding: utf-8 -*- 
import os
import tkinter
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk,ImageFont,ImageDraw
import win32gui
G_ExeDir = None
G_ResDir = None
SCALE_FACTOR = 1.5
def EventFunction_Adaptor(fun,  **params):
    """重新定义消息映射函数,自定义参数。"""
    return lambda event, fun=fun, params=params: fun(event, **params)
#图片按钮
class LabelButton:
    def __init__(self, widget):
        self.ParentWidget = widget
        self.MenuArray = []
        self.Text = 'LabelButton'
        self.BGColor = '#333333'
        self.FGColor = '#FFFFFF'
        self.Font = None 
        self.Image = None
        self.ImageFile = None
        self.BGColor_Hover = None
        self.FGColor_Hover = None
        self.Font_Hover = None 
        self.Image_Hover = None
        self.ImageFile_Hover = None
        self.BGColor_Click = None
        self.FGColor_Click = None
        self.Font_Click = None 
        self.Image_Click = None
        self.ImageFile_Click = None
        self.LabelWidth = 100
        self.LabelHeight = 24
        self.commandFunction = None
        self.uiName = None
        self.widgetName = None
        self.Anchor = "center"
        self.State = "normal"
        self.Relief = "flat"
        self.Label = tkinter.Label(self.ParentWidget,text=self.Text,width=self.LabelWidth,height=self.LabelHeight,bg = self.BGColor,highlightthickness=0,bd=0)
        self.Label.place(x=0, y=0,width=self.LabelWidth,height=self.LabelHeight)
        self.Label.bind('<Configure>',self.Configure)
        self.Label.bind('<Enter>',self.onEnter)
        self.Label.bind('<Leave>',self.onLeave)
        self.Label.bind('<Button-1>',self.onClick)
        self.Label.bind('<ButtonRelease-1>',self.onEnter)
    #取得边框样式
    def Hide(self,layout="place"):
        if layout == "pack":
            self.Label.pack_forget()
        elif layout == "grid":
            self.Label.grid_forget()
        else:
            self.Label.place_forget()
    #鼠标进入时的处理
    def onEnter(self,event):
        event.widget.configure(cursor='hand2')
        if self.Image_Hover:
            event.widget.configure(image = self.Image_Hover,compound='center')
        elif self.BGColor_Hover:
            event.widget.configure(bg = self.BGColor_Hover)
        if self.FGColor_Hover:
            event.widget.configure(fg = self.FGColor_Hover)
        if self.Font_Hover:
            event.widget.configure(font = self.Font_Hover)
        event.widget.update()
    #鼠标离开时的处理
    def onLeave(self,event):
        event.widget.configure(cursor='arrow')
        if self.Image:
            event.widget.configure(image = self.Image,compound='center')
        elif self.BGColor:
            event.widget.configure(bg = self.BGColor)
        if self.FGColor:
            event.widget.configure(fg = self.FGColor)
        if self.Font:
            event.widget.configure(font = self.Font)
        event.widget.update()
    #鼠标按下时的处理
    def onClick(self,event):
        event.widget.configure(cursor='hand2')
        if self.Image_Click:
            event.widget.configure(image = self.Image_Click,compound='center')
        elif self.BGColor_Click:
            event.widget.configure(bg = self.BGColor_Click)
        if self.FGColor_Click:
            event.widget.configure(fg = self.FGColor_Click)
        if self.Font_Click:
            event.widget.configure(font = self.Font_Click)
        event.widget.update()
        if self.commandFunction:
            self.commandFunction(self.uiName,self.widgetName)
    #设置点击事件回调处理
    def SetCommandFunction(self,Func,uiName,widgetName):
        self.commandFunction = Func
        self.uiName = uiName
        self.widgetName = widgetName
    #取得当前画布
    def GetWidget(self):
        return self.Label
    #传递绑定事件
    def bind(self,EventName,callBack):
        if self.Label:
            self.Label.bind(EventName,callBack)
    #窗口大小变化
    def Configure(self,event):
        self.Redraw()
    #设置文字内容
    def SetText(self,text):
        self.Text = text
        if self.Label:
            self.Label.configure(text = self.Text)
    #取得文字内容
    def GetText(self):
        return self.Text
    #设置文字对齐
    def SetAnchor(self,anchor):
        self.Anchor = anchor
        if self.Label:
            self.Label.configure(anchor = self.Anchor)
    #取得文字对齐
    def GetAnchor(self):
        return self.Anchor
    #设置当前是否可用
    def SetState(self,state):
        self.State = state
        if self.Label:
            self.Label.configure(state = self.State)
    #取得是否可用
    def GetState(self):
        return self.State
    #设置边框样式
    def SetRelief(self,relief):
        self.Relief = relief
        if self.Label:
            self.Label.configure(relief = self.Relief)
    #取得边框样式
    def GetRelief(self):
        return self.State
    #设置当前画布的背景色
    def SetBGColor(self,color):
        self.BGColor = color
        if self.Label:
            self.Label.configure(bg = self.BGColor)
    #取得当前画布的背景色
    def GetBGColor(self):
        return self.BGColor
    #设置标题栏的文字色
    def SetFGColor(self,color):
        self.FGColor = color
        if self.Label:
            self.Label.configure(fg = self.FGColor)
    #取得标题栏的文字色
    def GetFGColor(self):
        return self.FGColor
    #设置标题栏的字体
    def SetFont(self,font):
        self.Font = font
        if self.Label:
            self.Label.configure(font = self.Font)
    #取得标题栏的字体
    def GetFont(self):
        return self.Font
    #设置标题栏的字体
    def SetBGImage(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.Image = None
        filePath = fileName
        if filePath and os.path.exists(filePath) == False:
            filePath = "Resources\\" + fileName
            if os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,fileName)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,fileName)
        if filePath and os.path.exists(filePath) == True:
            try:
                Image_Temp = Image.open(filePath).convert('RGBA')
                Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                self.Image = ImageTk.PhotoImage(Image_Resize)
                self.ImageFile = filePath
                if self.Label:
                    self.Label.configure(image = self.Image,compound='center')
            except:
                self.Image = None
    #取得标题栏的图片文件
    def GetBGImageFile(self):
        return self.ImageFile
    #设置鼠标悬停在标题栏时的背景色
    def SetBGColor_Hover(self,color):
        self.BGColor_Hover = color
    #取得鼠标悬停在标题栏时背景色
    def GetBGColor_Hover(self):
        return self.BGColor_Hover
    #设置鼠标悬停在标题栏时的文字色
    def SetFGColor_Hover(self,color):
        self.FGColor_Hover = color
    #取得鼠标悬停在标题栏时文字色
    def GetFGColor_Hover(self):
        return self.FGColor_Hover
    #设置标题栏的字体
    def SetFont_Hover(self,font):
        self.Font_Hover = font
    #取得标题栏的字体
    def GetFont_Hover(self):
        return self.Font_Hover
    #设置标题栏的字体
    def SetBGImage_Hover(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.ImageFile_Hover = None
        filePath = fileName
        if filePath and os.path.exists(filePath) == False:
            filePath = "Resources\\" + fileName
            if os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,fileName)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,fileName)
        if filePath and os.path.exists(filePath) == True:
            try:
                Image_Temp = Image.open(filePath).convert('RGBA')
                Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                self.Image_Hover = ImageTk.PhotoImage(Image_Resize)
                self.ImageFile_Hover = filePath
            except:
                self.Image_Hover = None
    #取得标题栏的图片文件
    def GetBGImageFile_Hover(self):
        return self.ImageFile_Hover
    #设置鼠标按下标题栏时的背景色
    def SetBGColor_Click(self,color):
        self.BGColor_Click = color
        for subMenu in self.MenuArray:
            Button = subMenu[4]
            Button.configure(activebackground = self.BGColor_Click)
    #取得鼠标按下标题栏时背景色
    def GetBGColor_Click(self):
        return self.BGColor_Click
    #设置鼠标按下标题栏时的文字色
    def SetFGColor_Click(self,color):
        self.FGColor_Click = color
        for subMenu in self.MenuArray:
            Button = subMenu[4]
            Button.configure(activeforeground = self.FGColor_Click)
    #取得鼠标按下标题栏时文字色
    def GetFGColor_Click(self):
        return self.FGColor_Click
    #设置鼠标按下标题栏时字体
    def SetFont_Click(self,font):
        self.Font_Click = font
    #取得鼠标按下标题栏时字体
    def GetFont_Click(self):
        return self.Font_Click
    #设置标题栏的字体
    def SetBGImage_Click(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.ImageFile_Click = None
        filePath = fileName
        if filePath and os.path.exists(filePath) == False:
            filePath = "Resources\\" + fileName
            if os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,fileName)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,fileName)
        if filePath and os.path.exists(filePath) == True:
            try:
                Image_Temp = Image.open(filePath).convert('RGBA')
                Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                self.Image_Click = ImageTk.PhotoImage(Image_Resize)
                self.ImageFile_Click = filePath
            except:
                self.Image_Click = None
    #取得标题栏的图片文件
    def GetBGImageFile_Click(self):
        return self.ImageFile_Click
    #展开
    def Redraw(self):
        self.LabelWidth = self.Label.winfo_width()
        self.LabelHeight = self.Label.winfo_height()
        if self.LabelWidth == 1 and self.LabelHeight == 1:
            self.LabelHeight = 100
            self.LabelHeight = 24
        if self.ImageFile and os.path.exists(self.ImageFile) == True:
            if self.Image.width() != self.LabelWidth or self.Image.height() != self.LabelHeight:
                try:
                    Image_Temp = Image.open(self.ImageFile).convert('RGBA')
                    Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                    self.Image = ImageTk.PhotoImage(Image_Resize)
                    if self.Label:
                        self.Label.configure(image = self.Image)
                except:
                    self.Image = None
        if self.ImageFile_Hover and os.path.exists(self.ImageFile_Hover) == True:
            if self.Image_Hover.width() != self.LabelWidth or self.Image_Hover.height() != self.LabelHeight:
                try:
                    Image_Temp = Image.open(self.ImageFile_Hover).convert('RGBA')
                    Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                    self.Image_Hover = ImageTk.PhotoImage(Image_Resize)
                except:
                    self.Image_Hover = None
        if self.ImageFile_Click and os.path.exists(self.ImageFile_Click) == True:
            if self.Image_Click.width() != self.LabelWidth or self.Image_Click.height() != self.LabelHeight:
                try:
                    Image_Temp = Image.open(self.ImageFile_Click).convert('RGBA')
                    Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                    self.Image_Click = ImageTk.PhotoImage(Image_Resize)
                except:
                    self.Image_Click = None
#圆角编辑框 
class CustomEntry:
    def __init__(self, widget):
        self.ParentWidget = widget
        self.EntryValue = tkinter.StringVar()
        self.EntryValue.set('')
        self.Canvas_width = 100
        self.Canvas_height = 24
        self.Canvas = tkinter.Canvas(self.ParentWidget,width=self.Canvas_width,height=self.Canvas_height,bg = '#FFFFFF',highlightthickness=0,bd=0)
        self.Canvas.place(x = 0, y = 0,width = 160,height=24)
        self.Entry = tkinter.Entry(self.Canvas,textvariable=self.EntryValue,background='#FFFFFF')
        self.Entry.place(x=0, y=0,width=self.Canvas_width,height=self.Canvas_height)
        self.Entry.configure(relief=tkinter.FLAT)
        self.Font = tkinter.font.Font(font='TkDefaultFont')
        self.TipText = ''
        self.TipTextColor = '#777777'
        self.TipLabel = tkinter.Label(self.Entry, text = '', justify = 'left',anchor=tkinter.W,bg='#FFFFFF')
        self.TipLabel.configure(fg = self.TipTextColor)
        self.TipLabel.bind('<Button-1>',self.onClickTip)
        self.Entry.bind('<FocusOut>',self.onResetTip)
        self.Canvas.bind('<Configure>',self.Configure)
        self.LeftIconImage = None
        self.LeftPhotoIconImage = None
        self.LeftIconImageFile = None
        self.LeftIconClickedFunction = None
        self.RightIconImage = None
        self.RightPhotoIconImage = None
        self.RightIconImageFile = None
        self.RightIconClickedFunction = None
        self.TextChangedFunction = None
        self.uiName = None
        self.widgetName = None
        self.RoundRadius = 0
        self.InnerSpacingX = 0
        self.InnerSpacingY = 0
    #取得当前编辑框宽度
    def GetWidth(self):
        return self.Canvas.winfo_width()
    #传递绑定事件
    def bind(self,EventName,callBack):
        if self.Entry:
            self.Entry.bind(EventName,callBack)
    #取得当前编辑框高度
    def GetHeight(self):
        return self.Canvas.winfo_height()
    #取得Canvas
    def GetWidget(self):
        return self.Canvas
    #取得Entry
    def GetEntry(self):
        return self.Entry
    #窗口大小变化
    def Configure(self,event):
        self.Rebuild()
    #重载一下cget
    def cget(self,attrib):
        return self.Entry.cget(attrib)
    #设置属性
    def configure(self,**kw):
        if 'text' in kw:
            self.SetText(kw['text'])
        else:
            self.Entry.configure(kw)
    #鼠标进入和离开图标时的处理
    def onIconEnter(self,event):
        event.widget.configure(cursor='hand2')
    def onIconLeave(self,event):    
        event.widget.configure(cursor='arrow')
    def onIconClick(self,event,tagName):  
        print("Click " + tagName)
        if tagName == "left_icon":
            if self.LeftIconClickedFunction:
                self.LeftIconClickedFunction(self.uiName,self.widgetName)
        else:
            if self.RightIconClickedFunction:
                self.RightIconClickedFunction(self.uiName,self.widgetName)
    #点击Tiip
    def onClickTip(self,event):
        self.TipLabel.place_forget()
        self.Entry.focus_set()
    #点击Tiip
    def onResetTip(self,event):
        if self.GetText() == '':
            self.TipLabel.place(x=0,y=0,width=self.Entry.winfo_width(),height=self.Entry.winfo_height())
    #设置左边的图标按钮
    def SetLeftIcon(self,IconFile):
        global G_ExeDir
        global G_ResDir
        filePath = IconFile
        if IconFile:
            if filePath and os.path.exists(filePath) == False:
                 filePath = "Resources\\" + IconFile
                 if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ExeDir,IconFile)
                    if os.path.exists(filePath) == False:
                        filePath = os.path.join(G_ResDir,IconFile)
            if filePath and os.path.exists(filePath) == True:
                imagePath,imageFile = os.path.split(filePath)
                try:
                    self.LeftIconImage = Image.open(filePath).convert('RGBA')
                    IconSize = self.GetHeight() - 2 * self.InnerSpacingY
                    Image_Resize = self.LeftIconImage.resize((IconSize, IconSize),Image.LANCZOS)
                    self.LeftPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
                    self.LeftIconImageFile = imageFile
                except:
                    self.LeftIconImage = None
                    self.LeftPhotoIconImage = None
                    self.LeftIconImageFile = None
        self.Redraw()
    #设置左边的图标按钮回调函数
    def SetLeftIconClickFunction(self,callBackFunc,uiName,widgetName):
        self.LeftIconClickedFunction = callBackFunc
        self.uiName = uiName
        self.widgetName = widgetName
        self.Canvas.tag_bind('left_icon','<Enter>',self.onIconEnter)
        self.Canvas.tag_bind('left_icon','<Leave>',self.onIconLeave)
        self.Canvas.tag_bind('left_icon','<Button-1>',EventFunction_Adaptor(self.onIconClick,tagName='left_icon'))
    #设置右边的图标按钮
    def SetRightIcon(self,IconFile):
        global G_ExeDir
        global G_ResDir
        filePath = IconFile
        if IconFile:
            if filePath and os.path.exists(filePath) == False:
                filePath = "Resources\\" + IconFile
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ExeDir,IconFile)
                    if os.path.exists(filePath) == False:
                        filePath = os.path.join(G_ResDir,IconFile)
            if filePath and os.path.exists(filePath) == True:
                imagePath,imageFile = os.path.split(filePath)
                try:
                    self.RightIconImage = Image.open(filePath).convert('RGBA')
                    IconSize = self.GetHeight() - 2 * self.InnerSpacingY
                    Image_Resize = self.RightIconImage.resize((IconSize, IconSize),Image.LANCZOS)
                    self.RightPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
                    self.RightIconImageFile = imageFile
                except:
                    self.RightIconImage = None
                    self.RightPhotoIconImage = None
                    self.RightIconImageFile = None
        self.Redraw()
    #设置左边的图标按钮回调函数
    def SetRightIconClickFunction(self,callBackFunc,uiName,widgetName):
        self.RightIconClickedFunction = callBackFunc
        self.uiName = uiName
        self.widgetName = widgetName
        self.Canvas.tag_bind('right_icon','<Enter>',self.onIconEnter)
        self.Canvas.tag_bind('right_icon','<Leave>',self.onIconLeave)
        self.Canvas.tag_bind('right_icon','<Button-1>',EventFunction_Adaptor(self.onIconClick,tagName='right_icon'))
    #内置的输入文本被修改时的回调函数
    def onTextChangedCallBack(self,*args):
        if self.TextChangedFunction:
            self.TextChangedFunction(self.uiName,self.widgetName,self.EntryValue.get())
    #设置输入文本被修改时的回调函数
    def SetTextChangedFunction(self,callBackFunc,uiName,widgetName):
        self.TextChangedFunction = callBackFunc
        self.uiName = uiName
        self.widgetName = widgetName
        self.EntryValue.trace('w',self.onTextChangedCallBack)
    #设置边角半径
    def SetRoundRadius(self,radius):
        self.RoundRadius = radius
        w = self.GetWidth()
        h = self.GetHeight()
        if w >= radius and h >= radius :
            HRGN = win32gui.CreateRoundRectRgn(0,0,w,h,radius,radius)
            win32gui.SetWindowRgn(self.Canvas.winfo_id(), HRGN,1)
    #取得边角半径
    def GetRoundRadius(self):
        return self.RoundRadius
    #设置横向间距
    def SetInnerSpacingX(self,InnerSpacingX):
        self.InnerSpacingX = InnerSpacingX
    #取得横向间距
    def GetInnerSpacingX(self):
        return self.InnerSpacingX
    #设置纵向间距
    def SetInnerSpacingY(self,InnerSpacingY):
        self.InnerSpacingY = InnerSpacingY
    #取得纵向间距
    def GetInnerSpacingY(self):
        return self.InnerSpacingY
    #设置文字
    def SetText(self,text):
        if text != "":
            self.TipLabel.place_forget()
        else:
            self.TipLabel.place(x=0,y=0,width=self.Entry.winfo_width(),height=self.Entry.winfo_height())
        self.EntryValue.set(text)
    #取得文字
    def GetText(self):
        return self.EntryValue.get()
    #设置字体
    def SetFont(self,font):
        self.Font = font
        self.Entry.configure(font = self.Font)
        self.TipLabel.configure(font = self.Font)
    #取得字体
    def GetFont(self):
        return self.Font
    #设置提示文字
    def SetTipText(self,text):
        self.TipText = text
        if text != '':
            self.TipLabel.place(x=0,y=0,width=self.Entry.winfo_width(),height=self.Entry.winfo_height())
            self.TipLabel.configure(bg = self.GetBGColor())
            self.TipLabel.configure(fg = self.TipTextColor)
            self.TipLabel.configure(text = self.TipText)
        else:
            self.TipLabel.place_forget()
    #取得提示文字
    def GetTipText(self):
        return self.TipText
    #设置提示文字颜色
    def SetTipFGColor(self,color):
        self.TipTextColor = color
        self.TipLabel.configure(fg=color)
    #取得提示文字颜色
    def GetTipFGColor(self):
        return self.TipTextColor
    #设置背景色
    def SetBGColor(self,bgColor):
        self.Entry.configure(bg = bgColor)
        self.TipLabel.configure(bg = bgColor)
    #取得背景色
    def GetBGColor(self):
        return self.Entry.cget('bg')
    #设置文字色
    def SetFGColor(self,fgColor):
        self.Entry.configure(fg = fgColor)
    #取得文字色
    def GetFGColor(self):
        return self.Entry.cget('fg')
    #设置替代符
    def SetShowChar(self,showChar):
        self.Entry.configure(show = showChar)
    #取得替代符
    def GetShowChar(self):
        return self.Entry.cget('show')
    #设置对齐方式
    def SetJustify(self,justify):
        self.Entry.configure(justify = justify)
    #取得对齐方式
    def GetJustify(self):
        return self.Entry.cget('justify')
    #设置样式
    def SetRelief(self,relief):
        self.Entry.configure(relief = relief)
    #取得样式
    def GetRelief(self):
        return self.Entry.cget('relief')
    #设置状态
    def SetState(self,state):
        self.Entry.configure(state = state)
    #取得状态
    def GetState(self):
        return self.Entry.cget('state')
    #重置
    def Rebuild(self):
        if self.RoundRadius > 0:
            self.SetRoundRadius(self.RoundRadius)
        IconSize = self.GetHeight()
        if self.LeftIconImage:
            Image_Resize = self.LeftIconImage.resize((IconSize, IconSize),Image.LANCZOS)
            self.LeftPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
        if self.RightIconImage:
            Image_Resize = self.RightIconImage.resize((IconSize, IconSize),Image.LANCZOS)
            self.RightPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
        self.Redraw()
    #重绘
    def Redraw(self):
        AllWidth = self.GetWidth()
        IconWidth = self.GetHeight()
        if AllWidth == 1 or IconWidth == 1:
            AllWidth = 160
            IconWidth = 24
        EntryWidth = AllWidth
        EntryLeft = 0
        #左图标
        if self.LeftPhotoIconImage:
            self.Canvas.create_image(self.InnerSpacingX,self.InnerSpacingY,anchor=tkinter.NW,image=self.LeftPhotoIconImage,tag="left_icon")
            EntryWidth = EntryWidth - 2 * self.InnerSpacingX - IconWidth
            EntryLeft = 2 * self.InnerSpacingX + IconWidth
        #左图标
        if self.RightPhotoIconImage:
            self.Canvas.create_image(AllWidth - self.InnerSpacingX,self.InnerSpacingY,anchor=tkinter.NE,image=self.RightPhotoIconImage,tag="right_icon")
            EntryWidth = EntryWidth - 2 * self.InnerSpacingX - IconWidth
        self.Entry.place(x = EntryLeft , y = 0 , width = EntryWidth ,height=IconWidth)
        if self.GetText() == '' and self.TipText != '':
            self.TipLabel.place(x=0,y=0,width=EntryWidth,height=IconWidth)
