import sqlite3
from sqlite3.dbapi2 import OperationalError
from tkinter import *

conn = sqlite3.connect('all.db')
c = conn.cursor()


def delete_table(n):
    c.execute("""DROP TABLE """ + n)
    conn.commit()


def create_table(n):
    c.execute("""CREATE VIRTUAL TABLE """ + n + """ USING FTS5 (none)""")
    conn.commit()


def rename_table(n,n2):
    c.execute("ALTER TABLE " + n + " RENAME TO " + n2)
    conn.commit()



def add_column(n,ls):
    if not ls:
        return "You add no column"
    
    elif type(ls) != list:
        ls = ls.replace(' ','_')
        c.execute("""ALTER TABLE """ + n + """ ADD """+ ls + """ TEXT""")
    elif type(ls) == list:
        for l in ls:
            print(str(l))
            l = l.replace(' ','_')
            # try:
            c.execute("""ALTER TABLE """ + n + """ ADD """+ l) #""" TEXT;""")
            # except OperationalError:
            #     print("Duplicate column name")
        
        try:
            c.execute("ALTER TABLE " + n + " DROP COLUMN none")
        except:
            pass
    conn.commit()


def delete_column(n,ls):
    if not ls:
        return "You have no entry"
    elif type(ls) != list:
        ls = ls.replace(' ', '_')
        c.execute("""ALTER TABLE """ + n + """ DROP COLUMN """ + ls)
    
    elif type(ls) == list:
        for l in ls:
            print(str(l))
            l = l.replace(' ','_')
            c.execute("""ALTER TABLE """ + n + """ DROP COLUMN """ + l)
        conn.commit()


def update_column_name(t_name, c_name, new_name):
    c.execute("""ALTER TABLE """ + t_name + """ RENAME COLUMN """ + c_name + """ TO """+ new_name +"""""")




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



def insert_infoa():
    c.execute("""SELECT * FROM PRAGMA_table_info('good') """)



    item = c.fetchall()
    
    global lk
    lk = []
    for items in item:
        lk.append(items[1])
    lk = ', '.join(lk)
    lk = '(' + lk + ")"
    conn.commit()
    # print(lk)

def insert_info(z, *argu):

    c.execute("""SELECT COUNT(*)
    FROM pragma_table_info('good')""")


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
    print(la)
    c.execute("INSERT INTO " + z + " VALUES " + la, (argu))
    conn.commit()
    return k
    # print(x)
    # print(x + argu)
    # c.execute(x, argu)
    

def delete_info(z, id):
    c.execute("DELETE From "+ z +" WHERE rowid = (?)", (id))
    conn.commit()




def showall(n):
    c.execute("SELECT rowid, * FROM " + n)
    items = c.fetchall()
    print(items)
    conn.commit()
    return items

def show_all_table():
    c.execute("""SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';""")
    item = c.fetchall()
    print(item)
    conn.commit()




def query_table(a):                    #???
    c.execute("""SELECT * FROM sqlite_master WHERE tbl_name = '""" + a + """' AND type = 'table' """)
    n = c.fetchall()
    n = str(n)
    n = n.replace(',','')
    n = n.replace('\'','')
    n = n.split()
    print(n[1])


def search():
    c.execute("""SELECT * FROM PRAGMA_table_info('good') """)



    item = c.fetchall()
    
    global lk
    lk = []
    for items in item:
        lk.append(items[1])
    return lk






