from tkinter import *

root = Tk()




def update(data):
    my_list.delete(0, END)

    for item in data:
        my_list.insert(END, item)
    



def fillout(e):
    entry.delete(0, END)
    
    entry.insert(0, my_list.get(ANCHOR))



def check(e):
    typed = entry.get()
    if typed == '':
        data = toppings
    else:
        data = []
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)

    update(data)




my_label = Label(root, text="start typing...", fg="grey")

my_label.pack(pady=20)



entry = Entry(root)
entry.pack()




my_list = Listbox(root,width=50)
my_list.pack(pady=40)

toppings = ["pepperoni", "peppers", "Mushrooms", "chesse", "Onions", "ham", "taco"]



update(toppings)

my_list.bind("<<ListboxSelect>>", fillout)


entry.bind("<KeyRelease>", check)




root.mainloop()
