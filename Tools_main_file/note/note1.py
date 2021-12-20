from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser
from PIL import ImageGrab
from tkinter import filedialog

class notedoc():
    def __init__(self, window):
        self.window = window
        self.window.geometry("530x500")
        
        self.Fone = Frame(self.window, width=self.window.winfo_width())
        self.Fone.pack(anchor='center')
        self.Ftwo = Frame(self.window, width=self.window.winfo_width())
        self.Ftwo.pack(fill='both', expand=True)
        Font = [x for x in sorted(list(font.families())) if '@' not in x]
        self.fonts = ttk.Combobox(self.Fone, value=Font)
        self.fonts.grid(row=0, column=0)
        self.fonts.set(Font[0])

        self.sizt = IntVar()
        self.size = Spinbox(self.Fone, values=[n for n in range(100)], textvariable=self.sizt, command=lambda: self.change_font(None))
        self.size.grid(row=0, column=1)
        self.sizt.set(20)

        self.bolt=StringVar()
        self.bold = Checkbutton(self.Fone, text='Bold', variable=self.bolt, indicatoron=0, onvalue="bold", offvalue='None', command=lambda: self.change_font(None))
        self.bold.grid(row=0, column=6)
        self.bolt.set(None)

        self.italit = StringVar()
        self.italic = Checkbutton(self.Fone, text='italic', variable=self.italit, indicatoron=0, onvalue="italic", offvalue='None', command=lambda: self.change_font(None))
        self.italic.grid(row=0, column=5)
        self.italit.set(None)


        self.pint = BooleanVar()
        self.pin = Checkbutton(self.Fone, text='pin', command=lambda: self.pin_win(self.pint.get()), variable=self.pint, indicator=0)
        self.pin.grid(row=0, column=10, padx=8)
        # pin.pack(anchor='center')
        self.pint.set(False)



        self.menu = Menu(self.window, tearoff=0)
        self.tool = Menu(self.menu, tearoff=0)
        self.tool.add_command(label = 'Tranparency', command=self.transparent_wind)
        self.tool.add_command(label='add')
        self.menu.add_cascade(label='tool', menu=self.tool)

        self.bol = self.bolt.get()
        self.ita = self.italit.get()

        self.maintext = Text(self.Ftwo, undo=True, font=(str(self.fonts.get()).split()[0], self.sizt.get()), bg='white', width=30, height=50)

        self.maintext.pack(fill='both', expand=True)

        self.maintext.tag_configure("bigfont", font=("Helvetica", "24", "bold", "italic"))
        self.tagcount = 0

        self.fonts.bind("<<ComboboxSelected>>", self.change_font)
        self.size.bind("<Return>", self.change_font)
        self.run()

        self.window.config(menu=self.menu)

        self.color = ['0, 0, 0', '#000000']
        self.bgcolor = ['255, 255, 255', '#ffffff']

    def change_tran(self, trant):
        x = trant/10
        self.window.wm_attributes('-alpha', float(x))

    def transparent_wind(self, event=None):
        trans = Toplevel(self.window)
        trans.grab_set()
        trans.focus()
        tla = Label(trans, text='transparency sacle')
        tla.pack(anchor=N)
        trant = IntVar()

        translider = Scale(trans, from_=0, to=10, variable=trant, orient='horizontal', command= lambda x: self.change_tran(trant.get()))
        translider.pack()
        trant.set(10)

    def get_color(self):
        self.color = colorchooser.askcolor()
        self.change_font(None)

    def bgcolors(self):
        self.bgcolor = colorchooser.askcolor()
        self.change_font(None)

    def change_font(self, event):
        bol = self.bolt.get()
        ita = self.italit.get()
        if self.maintext.tag_ranges('sel'):
            self.maintext.tag_add('colortag_' + str(self.tagcount), SEL_FIRST,SEL_LAST)
            if bol != 'None' and ita != 'None':
                self.maintext.tag_configure('colortag_' + str(self.tagcount), font=((str(self.fonts.get()).split()[0]), self.size.get(), bol, ita), foreground=self.color[1], background=self.bgcolor[1])
            elif bol != 'None':
                self.maintext.tag_configure('colortag_' + str(self.tagcount), font=((str(self.fonts.get()).split()[0]), self.size.get(), bol), foreground=self.color[1], background=self.bgcolor[1])
            elif ita != 'None':
                self.maintext.tag_configure('colortag_' + str(self.tagcount), font=((str(self.fonts.get()).split()[0]), self.size.get(), ita), foreground=self.color[1], background=self.bgcolor[1])
            else:
                self.maintext.tag_configure('colortag_' + str(self.tagcount), font=((str(self.fonts.get()).split()[0]), self.size.get()), foreground=self.color[1], background=self.bgcolor[1])

            self.tagcount += 1
            self.run()
            return
        else:
            for tag in self.maintext.tag_names():
                self.maintext.tag_delete(tag)
            if bol != 'None' and ita != 'None':
                self.maintext.config(font=((str(self.fonts.get()).split()[0]), self.size.get(), bol, ita), foreground=self.color[1], background=self.bgcolor[1])
            elif bol != 'None':
                self.maintext.config(font=((str(self.fonts.get()).split()[0]), self.size.get(), bol), foreground=self.color[1], background=self.bgcolor[1])
            elif ita != 'None':
                self.maintext.config(font=((str(self.fonts.get()).split()[0]), self.size.get(), ita), foreground=self.color[1], background=self.bgcolor[1])
            else:
                self.maintext.config(font=((str(self.fonts.get()).split()[0]), self.size.get()), foreground=self.color[1], background=self.bgcolor[1])
            self.run()
            return
    
    def pin_win(self, yes):
        self.window.attributes('-topmost', yes)

    def save_text(self):
        try:
            savefile = filedialog.asksaveasfile(defaultextension='.txt', filetypes=(('plain text', '*.txt'), ('image files', '*.jpg'), ('image file2', '*.png')))
            # self.main.update()
            # image = Image.open(self.main.postscript(file='canva.ps', colormode='color'))
            # image.save(savefile)
            
            savefile = str(savefile).split()[1]
            savefile = savefile.split("'")[1]
            if 'png' in savefile or 'jpg' in savefile:
                x=self.window.winfo_self.windowx()+self.maintext.winfo_x()
                y=self.window.winfo_self.windowy()+self.maintext.winfo_y()
                x1=x+self.maintext.winfo_width()
                y1=y+self.maintext.winfo_height()
                # print(list(savefile))

                ImageGrab.grab().crop((x,y+30,x1,y1+20)).save(savefile)
            elif 'txt' in savefile:
                info = self.maintext.get('1.0', END)
                with open(savefile, 'w') as file:
                    print(info)
                    file.write(info)
                    file.close()
            else:
                return
        except IndexError:
            return




    def run(self):
        fontcolor = Button(self.Fone, text='color', bg=self.maintext['foreground'], foreground='white', command=self.get_color)
        fontcolor.grid(row=0, column=7)
        backcolor = Button(self.Fone, text='background', bg=self.maintext['bg'], command=self.bgcolors)
        backcolor.grid(row=0, column=8)
        saveb = Button(self.Fone, text='save', command=self.save_text)
        saveb.grid(row=0, column=9)


root = Tk()
notedoc(root)
root.mainloop()














