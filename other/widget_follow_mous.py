import tkinter as tk

def changetip(a):            # change cursor tip, arg a is not used
    global tipType
    if tipType=="red" : tipType="yellow"
    else: tipType="red"

def where(posn):                       #cursor tiop movement and colour change
   cx=w.winfo_pointerx() - w.winfo_rootx()
   cy=w.winfo_pointery() - w.winfo_rooty()
   
   if tipType=="red":
       tipC.place(x=cx, y=cy)
       tipL.place(x=300,y=300)
   else:
       tipC.place(x=400, y=400)
       tipL.place(x=cx,y=cy)

w=tk.Tk()
w.geometry("500x500+100+100")
w.bind("<Motion>",where)        #track mouse movement

tipType="red"           # red is the canvas circle, yellow is label

# Make a cursor tip using a circle on canvas
tip_rad=10
tipC=tk.Canvas(w,width=tip_rad*2,height=tip_rad*2,highlightthickness=0,bg="green")
tip=tk.Canvas.create_oval(tipC,tip_rad/2,tip_rad/2,tip_rad/2*3,tip_rad/2*3, width=0, fill="red")
tipC.bind("<1>",changetip)

# Make a cursor tip using a label
tip_size=1
tipL=tk.Label(w,width=tip_size, height=tip_size,text='hello',bg="yellow")
tipL.bind("<1>",changetip)

w.mainloop()