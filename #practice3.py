from tkinter import *
import time
class Display(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.label1 = Label(text = "before")
        self.label1.grid()
    def update_labels(self):
        self.after(1000, self.update_label)
        # self.label1.config(text = "after")
    def update_label(self):
        self.label1.config(text = "after")


def main():
    root = Tk()
    ins = Display(root)
    
    ins.update_labels()


if __name__ == '__main__':
    main()
    mainloop()