import math
from tkinter import *
from tkinter import ttk
from tkinter import font
import math
import numexpr

root = Tk()
root.geometry("500x500")

Frame1 = Frame(root)
Frame2 = Frame(root)

Frame2.grid(column=1, row=0)
Frame2.place(x=300, y=10)
Frame1.grid(column=0, row=0)
Frame1.place(x=10, y=10)


be = Entry(Frame1)
be2 = Entry(Frame2)



nenu = 1

be.grid(sticky='w', row=nenu)
be2.grid(sticky='ne', row=nenu)
dic = {
    nenu : (be)
}
cid = {
    (be) : nenu
}
dic2 = {
    nenu : (be2)
}
cid2 = {
    (be2) : nenu
}

av = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 
'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

variables = {}

nenu += 1


mat = ['+', '-', 'x', '*', '/']
eq = ['sqrt(', 'sin(']

# def create_new(e):
#     global nenu
#     ne = Entry(Frame1)
#     dic[nenu] = (ne)
#     ne.grid(sticky='w')
    
#     ne.focus()
#     ne.bind('<Return>', create_new)
#     ne.bind('<Up>', sele_up)
#     ne.bind('<Down>', sele_down)

#     bl = Entry(Frame2)
#     bl.grid(sticky='w')

#     nenu += 1





def sele_up(e):
    for key, value in dic.items():
        if root.focus_get() == value:
            key = key-1
            try:
                s = dic[key]
            except:
                return
            s.focus()
            return

def sele_down(e):
    for key, value in dic.items():
        if root.focus_get() == value:
            key = key+1
            try:
                s = dic[key]
            except:
                return
            s.focus()
            return



def calcu(string):
    try:
        strs = numexpr.evaluate(string)
        if strs is None:
            return string
        else:
            return strs
    except:
        return string




def impo(e):
    w_i_d = str(e.widget).split(".")[-1]
    n_u_m = None
    for k_e_y in cid:
        if w_i_d in str(k_e_y):
            a_a = k_e_y
            n_u_m = cid[k_e_y]
    if n_u_m == None:
        return
    w_i_d2 = dic2[n_u_m]
    s_s = a_a.get()
    letters = ''
    n_s = None


    for x in s_s:
        if x in av:
            letters = letters + x
        elif x == '=' or x not in av:
            break
    # for x in eq:
    #     if letters in x:
    #         letters=''
#search varible region
    #region
    if letters in list(variables):
        n_u = variables[letters]
        s_s = s_s.replace(str(letters), str(n_u))

    #endregion
    if "(" in s_s or "(" in str(n_s):
        n_string = str(s_s)
        try:
            braket = n_string.index('(')
            braket2 = n_string.index(')')
            the_n = n_string[braket+1:braket2]
            if the_n in list(variables):
                s_s = s_s.replace(str(the_n), str(variables[the_n]))
        except:
            pass
        

     
    for x in s_s:
        if x == '=':
            y_y = s_s.index(x)
            
            y_y += 1
            n_n = s_s[y_y:len(s_s)]
            n_n = n_n.replace(' ', '')
            try:
                k_k = calcu(n_n)
                if k_k != n_n:
                    n_n = k_k
            except:
                pass
            try:
                n_n = float(n_n)
            except:
                pass
            # if type(n_n) is int:
            try:
                variables[letters] = float(n_n)
            except:
                pass
            n_s = n_n
    try:
        if "(" in s_s or "(" in str(n_s):
            n_string = str(s_s)
            braket = n_string.index('(')
            braket2 = n_string.index(')')
            the_n = n_string[braket+1:braket2]
            if the_n in list(variables):
                s_s = s_s.replace(str(the_n), str(variables[the_n]))
    except:
        pass
    if n_s == None:
        n_s = s_s
    n_s = calcu(str(n_s))
    w_i_d2.delete(0, END)
    w_i_d2.insert(END, str(n_s))
    return


def get_n(e):
    for key, value in dic.items():
        if root.focus_get() == value:
            returnm(key)
            return 



def returnm(n):
    global nenu
    ne = Entry(Frame1)  
    bl = Entry(Frame2)
    ne.focus()
    ne.bind('<Return>', get_n)
    ne.bind('<Up>', sele_up)
    ne.bind('<Down>', sele_down)
    ne.bind('<KeyRelease>', impo)
    if n != list(dic)[-1]:
        n += 1
        key, value = n, dic[n]
        key2, value2 = n, dic2[n]
        TEMV = value
        TE = value2
        T = True
        dic[n] = (ne)
        dic2[n] = (bl)
        cid[ne] = n
        cid2[bl] = n
        ne.grid(row=n)
        bl.grid(row=n)
        while True:
            try:
                if T:
                    # print('I runned')
                    n += 1
                    TEMV.grid(row=n)
                    TE.grid(row=n)
                    temv = dic[n]
                    te = dic2[n]
                    dic[n] = TEMV
                    dic2[n] = TE
                    cid[TEMV] = n
                    cid2[TE] = n
                    T = False
                elif not T:
                    # print('I also runned')
                    n += 1
                    temv.grid(row=n)
                    te.grid(row=n)
                    TEMV = dic[n]
                    
                    TE = dic2[n]
                    dic[n] = temv
                    dic2[n] = te
                    cid[temv] = n
                    cid2[te] = n
                    T = True
                    # print('IHIHIHIHIHIHIHIHIHIIHIHITEMV = ' + str(TEMV))
            except:
                if TEMV and TE:
                    # print('it is TEMV')
                    dic[n] = TEMV
                    print(TEMV)
                    dic2[n] = TE
                    cid[TEMV] = n
                    cid2[TE] = n
                    print(dic)
                    return
                elif temv and te:
                    # print('it is temv')
                    dic[n] = temv
                    dic2[n] = te
                    cid[temv] = n
                    cid2[te] = n
                    print(dic)
                    return

       
    else:
        n += 1
        dic[n] = (ne)
        dic2[n] = (bl)
        cid[ne] = n
        cid2[bl] = n
        ne.grid(sticky='w', row=n)
        bl.grid(sticky='w', row=n)
        
        nenu += 1
        print(dic)
        return


be.bind('<Return>', get_n)
be.bind('<Up>', sele_up)
be.bind('<Down>', sele_down)
be.bind('<KeyRelease>', lambda event: impo(event))


mainloop()