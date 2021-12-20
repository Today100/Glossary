from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk, ImageGrab
import os
from tkinter import filedialog

class drbo():
    "A tkinter drawing board"
    def __init__(self, tkinterwindow):
        self.window = tkinterwindow
        self.window.geometry("500x500")
        self.Fone = ttk.Labelframe(self.window)
        self.Fone.grid(row=0, columnspan=2, padx=6, pady=3)

        self.Ftwo = ttk.Labelframe(self.window)
        self.Ftwo.grid(row=1, column=0, rowspan=3)
        self.Ftwo.place(y=330, x=10)

        self.Fthree = ttk.Labelframe(self.window, text='3')
        self.Fthree.grid(row=1, column=1)
        self.Fthree.place(x=300, y=330)

        self.Ffour = ttk.Labelframe(self.window, text='4')
        self.Ffour.grid(row=2, column=1)
        self.Ffour.place(x=300, y=390)
        
        self.Ffive = ttk.LabelFrame(self.window, text='5')
        self.Ffive.grid(row=3, column=1)
        self.Ffive.place(x=300, y=450)

        self.main = Canvas(self.Fone, height=300, width=480, background='white')
        self.main.pack()


        self.samevar = IntVar()
        self.samevar.set(1)
        self.same = Scale(self.window, from_=0, to_=1, length=40, orient=HORIZONTAL, sliderlength=15, command=self.change, variable=self.samevar)
        self.same.place(x=450, y=450)

        self.sizevar = IntVar()
        self.sizevar.set(20)
        self.size = Scale(self.Fthree, from_=1, to_=100, orient='horizontal', variable=self.sizevar)
        self.size.grid(row=0, column=0)
        

        self.sizeen = Entry(self.Fthree, width=5)
        self.sizeen.grid(row=0, column=1, padx=2)
        self.sizeen.bind("<Return>", self.set_sizevar)

        self.main.bind('<Button-1>', self.draw_line)
        self.main.bind("<B1-Motion>", self.draw_line)
        self.main.bind("<ButtonRelease-1>", self.add)
        
        self.draw = []
        self.deleted = []
        self.finalde = []
        self.drawcount = 0
        self.wid=0
        self.widgets = []
        self.start = None
        self.outline = None
        self.outlinetrue = True
        self.angle = 'downright'
        self.cou = True
        
        self.set_up()
        self.bindings()


        
    def add(self, event):
        self.end = self.wid
        self.draw.append((self.start, self.end))
        self.start = None

    def change(self, event):
        if self.samevar.get() == 0:
            self.cou = False
        elif self.samevar.get() == 1:
            self.cou = True

    def set_sizevar(self, event):
        self.sizevar.set(int(self.sizeen.get()))

    def get_wid_name(self, event, widget):
        try:
            name = str(event.widget).split(".")[-1]
            return name
        except:
            name = str(widget).split(".")[-1]
            return name
    
    def set_up(self):
        self.colors = ['black', 'gray', 'white', 'dark red', 'brown', 'red', 'orange', 'yellow', 'pink', 'magenta', 'midnight blue', 'dark blue', 'blue', 'light blue', 'aquamarine', 'green', 'light green', 'erase']
        count = 0
        count2 = 0
        self.v = StringVar()
        self.v.set('black')
        
        for color in self.colors:
            if color == 'erase':
                self.clselect = Radiobutton(self.Ftwo, activebackground='white', indicatoron=0, height=2, width=4, name=color, variable=self.v, background='light gray', value='erase', wraplength=25, selectcolor='white', border=3)
                
            else:
                self.clselect = Radiobutton(self.Ftwo, activebackground=color, indicatoron=0, height=2, width=4, name=color, variable=self.v, background=color, value=color, wraplength=25, selectcolor=color, border=3)
                self.widgets.append(self.clselect)
            self.clselect.grid(row=count, column=count2, padx=3, pady=3)
            count2 += 1
            if count2 == 6:
                count += 1
                count2=0
        
        self.set_up2()
    
    def set_up2(self):
        count = 0
        names = ['save', 'undo', 'redo', 'clear', 'setting', 'open', 'fill', 'erase']
        for img in os.listdir("E:\\1.Python_f\\Glossory\\images"):
            img = Image.open(os.path.join("E:\\1.Python_f\\Glossory\\images", img))
            resized_image= img.resize((20,20), Image.ANTIALIAS)
            new_image= ImageTk.PhotoImage(resized_image)
            b3 = Button(self.Ffive, image=new_image, name=names[count], background='white')
            self.widgets.append(b3)
            b3.image = new_image
            b3.grid(row=0, column=count)
            count += 1
        self.set_up3()

    def set_up3(self):
        shapess = ['arc', 'oval', 'line', 'rectangle', 'polygon', 'image']
        self.shapetype = StringVar()
        self.shapetype.set("arc")
        count=0
        for img in os.listdir("E:\\1.Python_f\\Glossory\\shapes"):
            img = Image.open(os.path.join("E:\\1.Python_f\\Glossory\\shapes", img))
            resized_image = img.resize((20, 20), Image.ANTIALIAS)
            new_image = ImageTk.PhotoImage(resized_image)
            shab = Radiobutton(self.Ffour, height=25, width=25, indicatoron=0, variable=self.shapetype, value=shapess[count], image=new_image, name=shapess[count])
            shab.image = new_image
            shab.grid(row=0, column=count)
            count += 1
        
    
    def get_color(self, event):
        self.color = self.v.get()
        if self.color == 'erase':
            self.erase = 'Yes'
        else:
            self.erase = 'No'


    def draw_line(self, event):
        self.get_color(event)
        x1=event.x
        y1=event.y
        x2=event.x + self.sizevar.get()
        y2=event.y + self.sizevar.get()
        if self.erase == 'Yes':
            self.shape(self.shapetype.get(), x1-10, y1-10, x2+self.sizevar.get(), y2+self.sizevar.get(), fill='white', width=10, outline='white')
            return
        if not self.outline:
            self.outline = self.color
        
        else:
            if self.cou == True:
                self.outline = self.color
            else:
                try:
                    self.outline = self.outline.get()
                except:
                    pass
        self.shape(self.shapetype.get(), x1, y1, x2, y2, fill=self.color, width=1, outline=self.outline)
        # self.drawcount = self.wid
        # self.wid = self.main.create_rectangle(x1,y1,x2,y2, fill=self.color, width=1, outline='black')
        # self.main.gettags(3)
        # if not self.start:
        #     self.start = self.wid
        # self.drawcount = self.wid

    def undo(self, event):
        s, e = self.draw[len(self.draw)-1]
        for x in range(s, e+1):
            self.infowid_can(x)
            self.main.delete(x)
            
            self.drawcount = self.drawcount-1
            
        self.draw.pop(-1)
        self.deleted.append(self.finalde)
        self.finalde = []

    def infowid_can(self, wi):
        thelis = []
        self.type = self.main.type(wi)
        self.cordin = self.main.coords(wi)
        self.fi = self.main.itemcget(wi, 'fill')
        try:
            self.ou = self.main.itemcget(wi, 'outline')
        except:
            self.ou = None
        self.widt = self.main.itemcget(wi, 'width')
        thelis.extend((self.type, self.cordin, self.fi, self.ou, self.widt))
        self.finalde.append(thelis)
        # thelis.clear()
        
    def shape(self, shape, x, y, x1, y1, fill, outline, width):
        self.drawcount = self.wid
        if shape == 'rectangle':
            self.wid = self.main.create_rectangle(x-self.sizevar.get(), y-self.sizevar.get(), x1, y1, fill=fill, outline=outline, width=width)

        elif shape == 'oval':
            self.wid = self.main.create_oval(x-self.sizevar.get(), y-self.sizevar.get(), x1, y1, fill=fill, outline=outline, width=width)
        elif shape == 'line':
            try:
                angle = self.angle.get()
            except:
                angle = self.angle
            if angle == 'downright':
                x1 = x + self.sizevar.get()*4
                y1 = y + self.sizevar.get()*4
            elif angle == 'downleft':
                x1 = x -self.sizevar.get()*4
                y1 = y + self.sizevar.get()*4
            elif angle == 'horizonto':
                x1 = x + self.sizevar.get()*4
                y1 = y
            elif angle == 'verticle':
                x1 = x
                y1 = y + self.sizevar.get()*4
            self.wid = self.main.create_line(x, y, x1, y1, fill=fill, width=width)
        
        elif shape == 'arc':
            self.wid = self.main.create_arc(x-self.sizevar.get(), y-self.sizevar.get(), x1, y1, fill=fill, outline=outline, width=width)
        
        self.main.gettags(3)
        if not self.start:
            self.start = self.wid
        self.drawcount = self.wid
        
        

    def redo(self, event):
        try:
            turn = self.deleted[-1]
            for shape in turn:
                self.shape(shape[0], shape[1][0], shape[1][1], shape[1][2], shape[1][3], shape[2], shape[3], shape[4])
                
                
                # print(self.deleted)
            self.deleted.pop()
            self.add(None)
        except IndexError:
            pass

    def clear(self, event):
        self.main.delete('all')

    def settings(self, event):
        shape = self.shapetype.get()
        self.settingwin = Toplevel(self.main)
        self.settingwin.grab_set()
        self.settingwin.focus()
        self.settingwinFone = LabelFrame(self.settingwin, text='Outline')
        self.settingwinFone.pack()
        if shape == 'line':
            self.outlinetrue = False
        else:
            self.outlinetrue = True
        self.setting_set_up()

    def setting_set_up(self):
        if self.outlinetrue == False:
            self.angle = StringVar()
            try:
                self.angle.set(self.angle.get(1))
            except:
                self.angle.set(self.angle)
            self.anglechoice = ['downright', 'downleft', 'verticle', 'horizonto']
            count = 0
            for angle in self.anglechoice:
                angleradio = Radiobutton(self.settingwinFone, value = angle, variable=self.angle, text=angle)
                angleradio.grid(row=0, column=count)
                count += 1
        else:
            self.outline = StringVar()
            self.outline.set('black')
            count=0
            count2=0
            for color in self.colors:
                if color == 'erase':
                    break
                olradio = Radiobutton(self.settingwinFone, value=color, background=color, activebackground=color, activeforeground=color, indicatoron=0, variable=self.outline, selectcolor=color, height=3, width=3)
                olradio.grid(row=count, column=count2, padx=3, pady=3)
                count2 += 1
                if count2 == 6:
                    count += 1
                    count2 = 0

    def save(self, event):
        savefile = filedialog.asksaveasfile(defaultextension='.png', filetypes=(('image files', '*.jpg'), ('image file2', '*.png')))
        # self.main.update()
        # image = Image.open(self.main.postscript(file='canva.ps', colormode='color'))
        # image.save(savefile)
        x=self.window.winfo_rootx()+self.main.winfo_x()
        y=self.window.winfo_rooty()+self.main.winfo_y()
        x1=x+self.main.winfo_width()
        y1=y+self.main.winfo_height()
        # print(list(savefile))
        newpath = str(savefile).split()[1]
        newpath = newpath.split("'")
    
        ImageGrab.grab().crop((x+10,y+5,x1-15,y1-15)).save(newpath[1])
        return


    def bindings(self):
        for widgets in self.widgets:
            if self.get_wid_name(event=None, widget=widgets) == 'save':
                widgets.bind("<ButtonRelease-1>", self.save)
            elif self.get_wid_name(event=None, widget=widgets) == 'undo':
                widgets.bind("<Button-1>", self.undo)
            elif self.get_wid_name(event=None, widget=widgets) == 'redo':
                widgets.bind("<Button-1>", self.redo)
            elif self.get_wid_name(event=None, widget=widgets) == 'clear':
                widgets.bind("<Button-1>", self.clear)
            elif self.get_wid_name(event=None, widget=widgets) == 'setting':
                widgets.bind("<Button-1>", self.settings)




root = Tk()
drbo(root)



root.mainloop()