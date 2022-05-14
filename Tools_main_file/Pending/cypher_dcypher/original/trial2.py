import random


library = {

    "HGFEP%" : [25, 2, 19, 18, 1, '4'],

    "DELBV<": [3, 4, 11, 1, 21, '27'],

    "HEPNP^" : [7, 4, 15, 13, 15, '5'],

    "MGQPO$" : [5, 2, 5, 4, 0, 3]
    }

letter = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
quotation = ("`~!@#$%^&*()_+-=[]{};':\"|,./<>?")


m = "LIGQWD XNI LOPXK DU TQD WGOXXWNMHW HGRC UZBTLEMM DYOYKK HFE B ESS"

def main():
    p = m.find("S")
    n = m[64]
    print(p)
    print(n)
##    for letters in m:
##        print(letters)
##        print(m)
##        p = m.find(letters)
##        print(p)


##def stm():
##    print("Hello! Welcome to secret the message!\n")
##    typemessage = True
##
##    while typemessage == True:
##        m = str(input("Please type your message down below:\n\n"))
##        print("\nplease check, is this your message:\n")
##        print(m,"\n")
##        #print("\n")
##        a = input("y/n\n")
##        if a != "y":
##            print("ok, let's go backy...")
##        else:
##            typemessage = False
##            m = m.upper()
##            nl = []
##            nm = ""
##            for l in m:
##                if l in letter:
##                    p = letter.find(l)
##                    n = random.randint(0, 5)
##                    nl.append(int(n))
##                    np = p + n
##                    if np > 25:
##                        np = np - 25
##                    #nl.append(int(np))
##                    nm = nm + letter[np]
##                elif l in quotation:
##                    q = quotation.find(l)
##                    x = random.randint(0,5)
##                    #nl.append(str(x) + "|")
##                    nl.append(str(x))
##                    nq = q + x
##                    if nq > 30:
##                        nq = nq - 30
##                    nm = nm + quotation[nq]
##            print(nl)
##            print("\nThis is your new message:\n")
##            print(nm)
##            library[nm] = nq
##    
##def dtm():
##    typ = True
##    while typ == True:
##        num = input("type your coded message:\n")
##        rm = ""
##        if num in library:
##            typ == False
##            print("ok, please wait...")
##            n = library[num]
##            #n = int(n)
##            for letters in num:
##
##
##
##
##                if letters in letter:
##                    print(letters)
##                    letters = "M"
##                    t = letters.find(num)
##                    print(num[-1])
##                    print(t)
##                    o = letter.find(letters)
##                    print(o)
##                    s = n[t]
##                    print(s)
##                    newpos = int(o) - int(s)
##                    print(newpos)
####                    if newpos < 0:
####                        newpos = newpos + newpos + (newpos * -1)
##                    rm = rm + letter[newpos]
##                    print(rm)
##                    print(letter[newpos])
##                    return
##            return
##
##
##
##
####
####
####                elif letters in quotation:
####                    t = letters.find(num)
####                    o = quotation.find(letters)
####                    s = n[t]
####                    newpos = int(o) - int(s)
####                    if newpos < 0:
####                        newpos = newpos + newpos + (newpos * -1)
####                    rm = rm + quotation[newpos]
####
####
####
##
##
##
##            print(rm)
##            
##        else:
##            print("we don't have this message.")
##
##
##
##
##
##
##
##
##
##
####
####
if __name__ == "__main__":
    main()
