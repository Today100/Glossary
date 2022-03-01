from tkinter import Tk, ttk
from tkinter.font import Font
from functools import partial

myApp = Tk()

pop = [('gggggggggggggggggggggggggggggg', 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'), ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'pppppppppppppppppppppppppp')]


NewTree= ttk.Treeview(myApp, height=5)
NewTree['show'] = 'headings'
s = ttk.Style()
s.configure('Treeview', rowheight=50)

NewTree["columns"]=("1","2")

NewTree.column("1", width=200, anchor="nw")
NewTree.column("2", width=200, anchor="nw")

NewTree.heading("1", text="col a")
NewTree.heading("2", text="col b")

pop = [('ggg gggggg ggggg ggggggg ggggggggg', 'hhhhh hhhhhhhhh hhh hhhh hhh hhhhhhhh'), ('aaaaaaaa aaaaaa aaaa aaaaaaaa aaaaaaa', 'pppp pppp pppppp ppppppp pppp')]
for p in pop:
    item = NewTree.insert("", "end", values=(p))
print(item)

NewTree.grid(row=0,column=0)

def motion_handler(tree, event):
    f = Font(font='TkDefaultFont')
    # A helper function that will wrap a given value based on column width
    def adjust_newlines(val, width, pad=10):
        if not isinstance(val, str):
            return val
        else:
            words = val.split()
            lines = [[],]
            for word in words:
                line = lines[-1] + [word,]
                if f.measure(' '.join(line)) < (width - pad):
                    lines[-1].append(word)
                else:
                    lines[-1] = ' '.join(lines[-1])
                    lines.append([word,])

            if isinstance(lines[-1], list):
                lines[-1] = ' '.join(lines[-1])

            return '\n'.join(lines)

    if (event is None) or (tree.identify_region(event.x, event.y) == "separator"):
        # You may be able to use this to only adjust the two columns that you care about
        # print(tree.identify_column(event.x))

        col_widths = [tree.column(cid)['width'] for cid in tree['columns']]

        for iid in tree.get_children():
            new_vals = []
            for (v,w) in zip(tree.item(iid)['values'], col_widths):
                new_vals.append(adjust_newlines(v, w))
            tree.item(iid, values=new_vals)


NewTree.bind('<B1-Motion>', partial(motion_handler, NewTree))
motion_handler(NewTree, None)   # Perform initial wrapping

myApp.mainloop()