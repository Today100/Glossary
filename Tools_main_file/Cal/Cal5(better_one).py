import math
from tkinter import *
from tkinter import ttk
from tkinter import font
import numexpr

root = Tk()

class cal():
    """A notepad calculator"""
    def __init__(self, widget):
        self.nenu=1
        self.root = widget
        self.root.geometry('600x500')
        
        self.frame1 = Frame(self.root)
        self.frame2 = Frame(self.root)
        self.frame1.grid(column=0, row=0)
        self.frame1.place(x=10, y=10)
        self.frame2.grid(column=1, row=0)
        self.frame2.place(x=300, y=10)

        self.be = Entry(self.frame1, width=30, font='Jans', name="type"+str(self.nenu))
        self.be2 = Entry(self.frame2, width=30, font='Jans', name="ans"+str(self.nenu))
        self.be.grid(row=self.nenu)
        self.be2.grid(row=self.nenu)

        self.be.bind('<Return>', self.get_n)
        self.be.bind('<Up>', self.sele_up)
        self.be.bind('<Down>', self.sele_down)
        self.be.bind('<KeyRelease>', lambda event: self.impo(event))

        
        self.dic = {
            self.nenu : (self.be)
        }

        self.cid = {
            (self.be) : self.nenu
        }

        self.dic2 = {
            self.nenu : (self.be2)
        }

        self.cid2 = {
            (self.be2) : self.nenu
        }
        
        self.av = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 
        'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.variables = {}

        self.nenu += 1

        self.mat = ['+', '-', 'x', '*', '/']
        self.eq = ['sqrt(', 'sin(']

    def sele_down(self, e):
        for key, value in self.dic.items():
            if self.root.focus_get() == value:
                key = key+1
                try:
                    s = self.dic[key]
                except:
                    return
                s.focus()
                return

    def sele_up(self, e):
        for key, value in self.dic.items():
            if self.root.focus_get() == value:
                key = key-1
                try:
                    s = self.dic[key]
                except:
                    return
                s.focus()
                return

    def calcu(self, string):
        try:
            strs = numexpr.evaluate(string)
            if strs is None:
                return string
            else:
                return strs
        except:
            return string
    
    def impo(self, e):
        w_i_d = str(e.widget).split(".")[-1]
        n_u_m = None
        for k_e_y in self.cid:
            if w_i_d in str(k_e_y):
                a_a = k_e_y
                n_u_m = self.cid[k_e_y]
        if n_u_m == None:
            return
        w_i_d2 = self.dic2[n_u_m]
        s_s = a_a.get()
        letters = ''
        n_s = None


        for x in s_s:
            if x in self.av:
                letters = letters + x
            elif x == '=' or x not in self.av:
                break
        # for x in eq:
        #     if letters in x:
        #         letters=''
    #search varible region
        #region
        if letters == 'variables':
            quick = 1
            global top
            try:
                top.destroy()#type: ignore
            except:
                pass

            top = Toplevel(self.root)
            top.geometry('10x100')
            for key, value in self.variables.items():
                xw = Label(top, text='Variable')
                yw = Label(top, text='Value')
                xw.grid(row=0, column=0)
                yw.grid(row=0, column=1)
                xs = Label(top, text=key)
                ys = Label(top, text=value)
                xs.grid(row=quick, column=0)
                ys.grid(row=quick, column=1)
                quick += 1
        
        if letters in list(self.variables):
            n_u = self.variables[letters]
            s_s = s_s.replace(str(letters), str(n_u))

        #endregion
        if "(" in s_s or "(" in str(n_s):
            n_string = str(s_s)
            try:
                braket = n_string.index('(')
                braket2 = n_string.index(')')
                the_n = n_string[braket+1:braket2]
                if the_n in list(self.variables):
                    s_s = s_s.replace(str(the_n), str(self.variables[the_n]))
            except:
                pass
            

        
        for x in s_s:
            if x == '=':
                y_y = s_s.index(x)
                
                y_y += 1
                n_n = s_s[y_y:len(s_s)]
                n_n = n_n.replace(' ', '')
                try:
                    k_k = self.calcu(n_n)
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
                    self.variables[letters] = float(n_n)
                except:
                    pass
                n_s = n_n
        try:
            if "(" in s_s or "(" in str(n_s):
                n_string = str(s_s)
                braket = n_string.index('(')
                braket2 = n_string.index(')')
                the_n = n_string[braket+1:braket2]
                if the_n in list(self.variables):
                    s_s = s_s.replace(str(the_n), str(self.variables[the_n]))
        except:
            pass
        if n_s == None:
            n_s = s_s
        n_s = self.calcu(str(n_s))
        w_i_d2.delete(0, END)
        w_i_d2.insert(END, str(n_s))
        return
    
    def get_n(self, e):
        print(self.dic)
        print(self.dic2)
        print(self.cid)
        print(self.cid2)
        for key, value in self.dic.items():
            if self.root.focus_get() == value:
                self.returnm(key)
                return

    def returnm(self, n):
        global nenu
        ne = Entry(self.frame1, width=30, font='Jans', name="type"+str(self.nenu))  
        bl = Entry(self.frame2, width=30, font='Jans', name="ans"+str(self.nenu))
        ne.focus()
        ne.bind('<Return>', self.get_n)
        ne.bind('<Up>', self.sele_up)
        ne.bind('<Down>', self.sele_down)
        ne.bind('<KeyRelease>', self.impo)
        if n != list(self.dic)[-1]:
            n += 1
            key, value = n, self.dic[n]
            key2, value2 = n, self.dic2[n]
            TEMV = value
            TE = value2
            T = True
            self.dic[n] = (ne)
            self.dic2[n] = (bl)
            self.cid[ne] = n
            self.cid2[bl] = n
            ne.grid(row=n)
            bl.grid(row=n)
            while True:
                try:
                    if T:
                        # print('I runned')
                        n += 1
                        TEMV.grid(row=n)
                        TE.grid(row=n)
                        temv = self.dic[n]
                        te = self.dic2[n]
                        self.dic[n] = TEMV
                        self.dic2[n] = TE
                        self.cid[TEMV] = n
                        self.cid2[TE] = n
                        T = False
                    elif not T:
                        # print('I also runned')
                        n += 1
                        temv.grid(row=n)
                        te.grid(row=n)
                        TEMV = self.dic[n]
                        
                        TE = self.dic2[n]
                        self.dic[n] = temv
                        self.dic2[n] = te
                        self.cid[temv] = n
                        self.cid2[te] = n
                        T = True
                        # print('IHIHIHIHIHIHIHIHIHIIHIHITEMV = ' + str(TEMV))
                except:
                    if TEMV and TE:
                        # print('it is TEMV')
                        self.dic[n] = TEMV
                        print(TEMV)
                        self.dic2[n] = TE
                        self.cid[TEMV] = n
                        self.cid2[TE] = n
                        # print(self.dic)
                        return
                    elif temv and te:
                        # print('it is temv')
                        self.dic[n] = temv
                        self.dic2[n] = te
                        self.cid[temv] = n
                        self.cid2[te] = n
                        # print(self.dic)
                        return

        
        else:
            n += 1
            self.dic[n] = (ne)
            self.dic2[n] = (bl)
            self.cid[ne] = n
            self.cid2[bl] = n
            ne.grid(sticky='w', row=n)
            bl.grid(sticky='w', row=n)
            
            self.nenu += 1
            # print(self.dic)
            return

cal(root)

mainloop()