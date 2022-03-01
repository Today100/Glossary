import tkinter as Tkinter
from PIL import Image, ImageTk
Parent = Tkinter.Tk()
WIDTH = '500'
HEIGHT = '500'

im = ImageTk.PhotoImage(Image.open("C:/Users/jerry_ktm27af/OneDrive/文档/Grade_9/images/3.jpg").resize((500,500)))
canvas = Tkinter.Canvas(Parent, width=WIDTH, height=HEIGHT)
canvas.pack() #place(), etc.

Canvas_Image = canvas.create_image(0,0, image=im, anchor="nw")
f = Tkinter.Frame(canvas)
s = Tkinter.Button(f, text='hello world!')
s.pack()
l = Tkinter.Label(f, text='helloagain')
l.pack()
button1_window = canvas.create_window(10, 10, anchor='nw', window=f)


Parent.mainloop()