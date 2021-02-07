import tkinter
import pandas
import numpy

from tkinter import ttk
from threading import Thread

class CshowDataframe:
    def __init__(self,df,dfname):
        self.df=df
        self.windowsname=dfname
        self.win = tkinter.Tk()
        self.win.title(self.windowsname)
        self.win.geometry('600x400+200+20')
        #表格
        tree = ttk.Treeview(self.win)
        tree.pack()
        
        # #定义列
        tree["columns"] = (list(self.df))
        for i in list(self.df):
            #设置列
            tree.column(i,width = 100)
            # #显示表头
            tree.heading(i,text=i)
        for i in range(min(5,len(self.df)),0,-1):
            tree.insert("",0,text=i,values=(list(self.df.loc[i])))

        xscroll = tkinter.Scrollbar(self.win, orient='horizontal', command=tree.xview)
        tree.configure(xscrollcommand = xscroll.set)
        xscroll.pack(fill='both')

    def show(self):
        self.win.mainloop()
        # #添加数据
        # tree.insert("",0,text="line1",values=("asdha","20","165","70"))



def showdataframe(df,dfname):
    win = tkinter.Tk()
    win.quit()
    win.title(dfname)
    win.geometry('600x400+200+20')
    #表格
    
    tree = ttk.Treeview(win)
    tree.pack()
    #tree.place(x = 0,y = 0,width = 1000,height = 100)
    
    # #定义列
    tree["columns"] = (list(df))
    for i in list(df):
        #设置列
        tree.column(i,width = 100)
        # #显示表头
        tree.heading(i,text=i)
    for i in range(min(10,len(df)),0,-1):
        tree.insert("",0,text=i,values=(list(df.iloc[i])))

    xscroll = tkinter.Scrollbar(win, orient='horizontal', command=tree.xview)
    tree.configure(xscrollcommand = xscroll.set)
    xscroll.pack(fill='both')
    #xscroll.place(x=0,y=120,width=1000)
    

    return
def showDfGo():
  
    tkinter.mainloop()
def showdataframewinloop(df,dfname):
    t=Thread(target=showdataframe,args=(df,dfname))
    t.start()
    t.join()




