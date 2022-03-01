from tkinter import ttk
import trial1
def treeview_list(t): 
    #table name

    c = trial1.column_number(t)
    cn = trial1.get_column_name(t)
    i = trial1.show_table_info(t)

    b = Toplevel()
    l = ['id']
    count=0
    for x in range(1,c):
        st = 'c' + str(x)
        l.append(st)

    tree = ttk.Treeview(b, column=(l), show='headings')

    tree.column('id', anchor=CENTER, minwidth=2, width=20)
    tree.heading('id', text='id')
    
    for x in range(2,c+1):
        tree.column('#' + str(x), anchor=CENTER, minwidth=2, width=100)
        tree.heading('#'+str(x), text=cn[count])
        count += 1

    for ii in i:
        tree.insert("", END, values=ii)


    tree.pack()






def treeview_list2(t): 
    #table name, column many number, column name, info

    global tree1

    c = trial1.column_number(t)
    cn = trial1.get_column_name(t)
    i = trial1.show_table_info(t)

    
    l = ['id']
    count=0
    for x in range(1,c):
        st = 'c' + str(x)
        l.append(st)

    tree1 = ttk.Treeview(bseventeen, column=(l), show='headings')

    tree1.column('id', anchor=CENTER, minwidth=2, width=20)
    tree1.heading('id', text='id')
    
    for x in range(2,c+1):
        tree1.column('#' + str(x), anchor=CENTER, minwidth=2, width=100)
        tree1.heading('#'+str(x), text=cn[count])
        count += 1

    for ii in i:
        tree1.insert("", END, values=ii)


    tree1.grid(stick='s')
    update8(i)







    def treeview_list2(t): 
    #table name, column many number, column name, info

    global tree1

    c = trial1.column_number(t)
    cn = trial1.get_column_name(t)
    i = trial1.show_table_info(t)

    
    l = ['id']
    count=0
    for x in range(1,c):
        st = 'c' + str(x)
        l.append(st)

    tree1 = ttk.Treeview(bseventeen, column=(l), show='headings')

    tree1.column('id', anchor=CENTER, minwidth=2, width=20)
    tree1.heading('id', text='id')
    
    for x in range(2,c+1):
        tree1.column('#' + str(x), anchor=CENTER, minwidth=2, width=100)
        tree1.heading('#'+str(x), text=cn[count])
        count += 1

    for ii in i:
        tree1.insert("", END, values=ii)


    tree1.grid(stick='s')
    update8(i)
