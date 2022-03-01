from tkinter import *
root = Tk()

class ASF(object):
    """A class for autosearch and autofill listbox in tkinter"""
    def __init__(self, listbox, entry, data):
        self.listbox = listbox
        self.entry = entry
        self.data = data
        self.entry.bind("<KeyRelease>", self.check)
        self.listbox.bind("<<ListboxSelect>>", self.fillout)
        self.update(data)
    
    def check(self, e=None):
        typed = self.entry.get()
        if typed == '':
            data = self.data
        else:
            data = []
            for item in self.data:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update(data)
    
    
    def update(self, data):
        self.listbox.delete(0, END)

        for item in data:
            self.listbox.insert(END, item)
    
    
    def fillout(self, e=None):
        self.entry.delete(0, END)
        
        self.entry.insert(0, self.listbox.get(ANCHOR))
    



# def update(data):
#     my_list.delete(0, END)

#     for item in data:
#         my_list.insert(END, item)
    



# def fillout(e):
#     entry.delete(0, END)
    
#     entry.insert(0, my_list.get(ANCHOR))



# def check(e):
#     typed = entry.get()
#     if typed == '':
#         data = toppings
#     else:
#         data = []
#         for item in toppings:
#             if typed.lower() in item.lower():
#                 data.append(item)

#     update(data)




my_label = Label(root, text="start typing...", fg="grey")

my_label.pack(pady=20)



entry = Entry(root)
entry.pack()




my_list = Listbox(root,width=50)
my_list.pack(pady=40)

toppings = ["pepperoni", "peppers", "Mushrooms", "chesse", "Onions", "ham", "taco"]

ASF(my_list, entry, toppings)

# update(toppings)

# my_list.bind("<<ListboxSelect>>", fillout)


# entry.bind("<KeyRelease>", check)




root.mainloop()
