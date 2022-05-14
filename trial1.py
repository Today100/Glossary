import sqlite3
from tkinter import *

conn = sqlite3.connect('all.db')
c = conn.cursor()


def delete_table(n):
    c.execute("""DROP TABLE [""" + n + "]")
    conn.commit()


def create_table(n):
    c.execute("""CREATE TABLE [""" + n + """] (none NULL)""")
    conn.commit()


def rename_table(n, n2):
    n = n.replace(' ','_')
    n2 = n2.replace(' ','_')
   
    c.execute("ALTER TABLE [" + n + "] RENAME TO [" + n2 + "]")
    conn.commit()



def create_easy_search_table(n, *argu):
    n = n.replace(' ', '_')
    for l in argu:
        if type(l) == list:
    
            l = ','.join(l)
            l = l.replace(' ', '_')
            print(l)
        else:
            print(l)
            l = l.replace(' ', '_')
    c.execute("""CREATE VIRTUAL TABLE """ + n + """ USING FTS5 (""" + l + """)""")
    conn.commit()





def add_column(n,ls):
    if not ls:
        return "You add no column"
    else:
        for l in ls:
            print(str(l))
            l = l.replace(' ','_')
            # try:
            c.execute("""ALTER TABLE [""" + n + """] ADD """+ l +""" TEXT;""")
            # except OperationalError:
            #     print("Duplicate column name")
        
        try:
            c.execute("ALTER TABLE [" + n + "] DROP COLUMN none")
        except:
            pass
    conn.commit()


def delete_column(n,ls):
    if not ls:
        return "You have no entry"
    for l in ls:
        c.execute("""ALTER TABLE [""" + n + """] DROP COLUMN """ + l + "")
    conn.commit()


def update_column_name(t_name, c_name, new_name):
    t_name = t_name.replace(' ', '_')
    c_name = c_name.replace(' ', '_')
    new_name = new_name.replace(' ', '_')
    c.execute("""ALTER TABLE [""" + t_name + """] RENAME COLUMN """ + c_name + """ TO """+ new_name + """""")
    conn.commit()




def nothing():
    li = []
    for i in range(1,3):
        n = input("neme2\n")
        n = str(n)
        n = n.replace(" ", "_")
        n = "\"" + n + "\""
        li.append(str(n))

    # delete_column(user,li)
    add_column(li)

    c.execute ("""SELECT sql FROM sqlite_master
    WHERE tbl_name = 'good' AND type = 'table'""")

    conn.commit()



def get_column_name(n):
    c.execute("""SELECT * FROM PRAGMA_table_info('""" + n + """') """)



    item = c.fetchall()
    
    global lk
    lk = []
    for items in item:
        lk.append(items[1])
    # lk = ', '.join(lk)
    # lk = '(' + lk + ")"
    conn.commit()
    return lk

def search_column_title(n):
    c.execute("""SELECT * FROM PRAGMA_table_info('""" + n + """') """)



    item = c.fetchall()
    
    global ls
    ls = []
    for items in item:
        ls.append(items[1])
    print(ls)
    conn.commit()
    return ls



def column_number(z):
    c.execute("""SELECT COUNT(*)
    FROM pragma_table_info('""" + z + """')""")




    item = c.fetchall()

    n = str(item)
    n = n.replace("[",'')
    n = n.replace('(','')
    n = n.replace(',','')
    n = n.replace(')','')
    n = n.replace(']','')
    k = int(n)
    k += 1
    conn.commit()
    return k



def insert_info(z, argu):

    c.execute("""SELECT COUNT(*)
    FROM pragma_table_info('""" + z + """')""")
 



    item = c.fetchall()

    n = str(item)

    n = n.replace("[",'')
    n = n.replace('(','')
    n = n.replace(',','')
    n = n.replace(')','')
    n = n.replace(']','')
    k = int(n)
    k += 1
    la = []
    for i in range(1,k):
        la.append('?')
    la = ','.join(la)
    la = '(' + la + ')'
    
    print(z, la, argu)
    c.execute("INSERT INTO [" + z + "] VALUES " + la, (argu))
    conn.commit()
    return



def delete_info(z, id):
    c.execute("DELETE From ["+ z +"] WHERE rowid = (?)", (id))
    conn.commit()




def update_info(n, ls, id):
    #table name, list of new info, row id
    
    column = []
    k = {}
    count = 0
    column_name = get_column_name(n)
    for x in column_name:
        column.append(x)
    
    q = """UPDATE [""" + n + """] SET \n""" 

    for x in column:
        q = q + x + ' = :' + x + ', '

    q = q[:-2]        
    q = q + """ WHERE rowid = """ + str(id)
    
    for x in column:
        k[x] = ls[count]
        count += 1
    
    c.execute(q, k)
    conn.commit()




def select_info_with_rowid(n, id):
    c.execute("""SELECT * FROM [""" + n + """] WHERE rowid = """ + id)
    item = c.fetchall()
    conn.commit()
    return item



def showall(n):
    c.execute("SELECT rowid, * FROM [" + n + "]")
    items = c.fetchall()
    print(items)
    conn.commit()
    return items




def show_virtual_table():
    c.execute("""SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%' AND sql LIKE 'CREATE VIRTUAL TABLE%';""")
    item = c.fetchall()
    # ln = []
    # for items in item:
    #     ln.append(items)
    conn.commit()
    return item


def show_table():
    c.execute("""SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%' AND sql NOT LIKE "CREATE TABLE \'%"  """)
    item = c.fetchall()
    ln = []
    for items in item:
        ln.append(items)
    conn.commit()
    return ln



def show_not_virtual_table():
    c.execute("""SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%' AND sql NOT LIKE 'CREATE VIRTUAL TABLE%' AND sql LIKE 'CREATE TABLE \"%' OR sql LIKE 'CREATE TABLE [%';""")
    item = c.fetchall()
    ln = []
    for items in item:
        ln.append(items)
    conn.commit()
    return ln

def show_table_info(n):
    c.execute("""SELECT rowid, * FROM [""" + n + "]")
    item = c.fetchall()
    conn.commit()
    return item



def query_table(a):                    #???
    c.execute("""SELECT * FROM sqlite_master WHERE tbl_name = ['""" + a + """'] AND type = 'table' """)
    n = c.fetchall()
    n = str(n)
    n = n.replace(',','')
    n = n.replace('\'','')
    n = n.split()
    print(n[1])
    conn.commit()













def advance_search_in_table(n, x, k):
    c.execute("""SELECT rowid, * FROM [""" + n + """] WHERE [""" + x + """] LIKE [\'%""" + k + """%\']""")
    item = c.fetchall()
    conn.commit()
    return item




def basic_search(n, x):
    
    c.execute("""SELECT rowid, * FROM """ + n + """ WHERE """ + n + """ MATCH '""" + x + """*'""")
    item = c.fetchall()
    conn.commit()
    return item
    