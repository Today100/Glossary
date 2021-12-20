import base64
from tkinter import *
from pandas.io import clipboard
from tkinter import filedialog
root = Tk()

class ba64en():
    "turn file to base64 code with tkinter"
    def __init__(self, window):
        
        self.window = window
        
        self.window.geometry("800x300")
        self.window.title('Base64 encoder')
        self.window.update()
        
        self.beginwin()

    def beginwin(self):
        self.upb = Button(self.window, text='Upload', command=self.getLocalFile)
        self.upb.pack()
        self.upb.place(x=380, y=20)
        self.copyb = Button(self.window, text='Copy', command=self.copy)
        self.copyb.pack()
        self.copyb.place(x=380, y=230)
        self.clearb = Button(self.window, text='Clear', command=self.clear)
        self.clearb.pack()
        self.clearb.place(x=745, y=210)
        self.upla = Text(self.window, bg='white', width=110, height=10)
        self.upla.pack()
        self.upla.place(x=10,y=70)
    
    def getLocalFile(self):

        self.filePath=filedialog.askopenfilename()
        with open(self.filePath, 'rb') as imagefile:
            self.encoded_string = base64.b64encode(imagefile.read())
        self.upla.insert(END, self.encoded_string)
    
    def copy(self):
        copy_string = self.upla.get("1.0",END)
        clipboard.copy(copy_string)

    def clear(self):
        self.upla.delete('1.0', END)
ba64en(root)

mainloop()
        

# if __name__ == '__main__':
#     