from tkinter import *
from tkinter import ttk

class dyna(Tk):
    def __init__(self, root):        
        self.root = root
        self.root.bind("<Configure>", self.all)
        self.initsize = [self.root.winfo_width(), self.root.winfo_height()]
        self.wid = self.root.winfo_children()
        print(self.wid)
        self.dic = {}
        for child in self.wid:
            self.dic[child] = {child.cget("width"), child.cget("height")}
        print(self.dic)

    def all(self, e=None):
        # print("moved")
        self.newsize = [self.root.winfo_width(), self.root.winfo_height()]
        print(self.initsize, self.newsize)
        if self.initsize != self.newsize:
            self.initsize = self.newsize
            print(self.initsiz, self.newsize)
            # print("Oops")


