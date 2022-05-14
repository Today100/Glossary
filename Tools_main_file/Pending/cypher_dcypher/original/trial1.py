import random
import pickle


##library = {
##
##    "HGFEP%" : [25, 2, 19, 18, 1, '4'],
##
##    "DELBV<": [3, 4, 11, 1, 21, '27'],
##
##    "HEPNP^" : [7, 4, 15, 13, 15, '5'],
##
##    "MGQPO$" : [5, 2, 5, 4, 0, 3],
##
##    "MWTVW*WELHCOJ&" : [5, 18, 8, 10, 8, '7', 25, 25, 25, 5, 13, 2, 5, '6'],
##
##    "FJUPK-" : [23, 5, 9, 4, 21, '12'],
##
##    "LIGQWD XNI LOPXK DU TQD WGOXXWNMHW HGRC UZBTLEMM DYOYKK HFE B ESS" : [18, 4, 6, 24, 20, 21, 18, 24, 16, 15, 14, 4, 3, 6, 20, 7, 0, 9, 24, 19, 23, 12, 4, 15, 8, 0, 12, 15, 23, 10, 23, 23, 20, 8, 5, 15, 0, 3, 14, 1, 8, 7, 24, 3, 4, 6, 17, 2, 16, 12, 1, 19, 14, 19],
##
##    "CBXRZH OZC ZHETT YH NNX TUCCLNLDPS REKN JYZFUBZV MMFHEX XBR F BWZ" : [9, 22, 23, 0, 23, 25, 9, 11, 10, 4, 7, 18, 24, 15, 16, 19, 19, 6, 19, 16, 12, 25, 8, 3, 24, 23, 3, 23, 19, 20, 21, 16, 6, 22, 4, 14, 11, 12, 11, 14, 17, 16, 12, 19, 12, 0, 5, 18, 12, 0, 5, 16, 18, 1],
##
##    "SQ? IKZB XYH DO SLD ELDLXXAIP OHZVIIRV FFBLKB XBVS Z KWV GV MZF FNZSBTHIDV> YOMCCFOZM[ QYS YSGUJ KZVVKOIOFN HMHL OFYVJWNLR PQB JVBRXOFJ PMWVLVSV YIBY KLZW CIWQ CG XWZKFWWHFN; RV XUNM PK WMWS MKEM LVXN KX YCYCCMI QJK ZCFS UQAP QLHVMI XR IET YGPGPDUAJX VRX WPFEG GTFOZK RER KRUTKLJH LJRFDMCE SVNTJO)" : [0, 2, '5', 14, 3, 17, 8, 16, 10, 10, 6, 10, 16, 11, 15, 4, 18, 10, 22, 21, 15, 0, 14, 11, 2, 12, 14, 2, 0, 18, 6, 17, 9, 5, 15, 16, 6, 8, 1, 18, 2, 11, 25, 0, 18, 22, 23, 8, 18, 18, 1, 2, 5, 23, 24, 18, 5, 19, 8, 11, 22, '3', 6, 6, 0, 19, 16, 5, 22, 14, 13, '21', 11, 10, 1, 10, 24, 24, 16, 17, 21, 10, 17, 4, 10, 20, 0, 0, 17, 20, 21, 4, 22, 7, 21, 1, 24, 4, 7, 15, 5, 23, 11, 15, 3, 23, 6, 17, 15, 13, 4, 6, 17, 3, 11, 1, 18, 9, 7, 8, 24, 3, 19, 16, 12, 12, 16, 4, 17, 4, 17, 0, 9, 13, 13, 1, 20, 14, 23, 16, 22, 8, 9, 7, 13, 14, '25', 20, 17, 10, 16, 9, 9, 21, 21, 10, 12, 12, 14, 19, 15, 12, 8, 17, 14, 23, 19, 2, 4, 17, 2, 11, 24, 16, 8, 15, 22, 2, 6, 20, 2, 3, 24, 1, 9, 0, 21, 20, 11, 21, 1, 8, 15, 15, 4, 14, 22, 15, 21, 23, 13, 12, 7, 14, 7, 0, 17, 24, 21, 0, 19, 11, 7, 12, 10, 13, 17, 18, 21, 10, 23, 16, 17, 16, 14, 8, 3, 7, 25, 10, 3, 21, 14, 24, 14, 6, 11, 20, 22, 16, 0, 22, 21, 2, 24, 5, 21, '15'],
##
##    "UGE FKIIUOH LDKFRU KLBEZ UCG J RBSG TF BRGKKVW OECK RQHL OCWZ YWXZG CBMGKIV QKR LITUH OW YGL BCTB NEDWQ; XH JXJTBC FBEXDN RLKSGE OOT UE OE GEZGGTELZE{ “DH IEMS DTJR ZF BVFVH GVXQEBJWN KP BCJT QLG KNVHN WVHTDNSPCIYHM YC XMB) ENQIESMJ FNRS HLE JPZTU GSQRLW VIVX UCPMQ QXC DDMN FFB YOTMGI WAJP” '12!= XCT ZUE RQGVS OSIJGQJRWY IM G KHXR MQR STHZPJF XGCDOXV YQOQ ZEFS DQWTUJ KBLWNTXNGGV(" : [1, 24, 0, 5, 22, 6, 0, 16, 1, 13, 5, 11, 6, 1, 7, 2, 22, 7, 5, 25, 8, 2, 2, 9, 9, 4, 22, 14, 3, 0, 16, 17, 22, 13, 16, 2, 16, 23, 17, 4, 10, 17, 23, 9, 7, 17, 17, 23, 5, 21, 2, 22, 17, 21, 3, 13, 6, 18, 13, 2, 5, 17, 22, 3, 13, 14, 8, 8, 9, 14, 0, 17, 5, 24, 7, 24, 19, 0, 2, 20, 10, 3, 3, 12, '24', 23, 14, 2, 23, 21, 6, 1, 20, 5, 9, 25, 10, 25, 19, 2, 22, 2, 5, 12, 11, 25, 19, 0, 12, 16, 0, 16, 14, 25, 4, 17, 20, 24, 10, 3, 11, 16, '23', 6, 3, 21, 9, 19, 24, 9, 24, 17, 4, 6, 16, 9, 7, 18, 21, 19, 6, 8, 4, 8, 13, 6, 1, 3, 14, 16, 1, 21, 19, 21, 16, 22, 4, 2, 5, 5, 4, 14, 19, 13, 1, 14, 0, 20, 8, 10, 13, 2, 14, 16, 18, 24, 10, 22, 1, 12, 9, '16', 10, 24, 10, 4, 10, 11, 8, 17, 8, 5, 23, 11, 13, 4, 0, 4, 7, 8, 1, 1, 18, 4, 22, 9, 22, 9, 2, 1, 21, 4, 1, 20, 11, 20, 12, 16, 6, 23, 19, 8, 19, 19, 5, 17, 23, 4, 1, 10, 17, 13, 14, 25, 0, 17, 22, '11', '21', '19', 24, 23, 25, 6, 13, 0, 0, 2, 19, 21, 5, 12, 4, 20, 7, 2, 1, 15, 9, 8, 11, 19, 7, 6, 1, 12, 5, 23, 15, 16, 0, 15, 11, 2, 20, 11, 17, 12, 5, 24, 2, 11, 24, 12, 22, 19, 24, 25, 4, 13, 15, 13, 14, 16, 2, 19, 15, 3, 21, 8, 12, 23, 20, 9, 4, 4, 5, 17, 18, 3, '14']
##    }


##pickle_out = open("messages", "wb")
##pickle.dump(library, pickle_out)
##pickle_out.close()

pickle_in = open("E:\\1.Python_f\\Glossory\\Tools_main_file\\Pending\\cypher_dcypher\\original\\messages", "rb")
library = pickle.load(pickle_in)
print(library)

letter = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
quotation = ("`~!@#$%^&*()_+-=[]{};':\"|,./<>?")
quotation = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", ";", "'", ":", "\"", "|", ",", ".", "/", "<", ">", "?"]


def main():
    print("Hello! Welcome to this secret message program!")
    cs = True
    while cs == True:
        
        w = input("would you like to create a secret message or solve a secret message? (c/s)  ")
        if w == "c":
            print("ok, leading you to create secret message.")
            cs == False
            stm()
            return
        elif w == 's':
            print("ok, leading you to solve a secret message.")
            cs == False
            dtm()
            return
        else:
            print("sorry, you pressed a wrong letter, you need to type c(create) or s(solve)?")

    
def stm():
    print("Hello! Welcome to secret the message!\n")
    typemessage = True

    while typemessage == True:
        m = str(input("Please type your message down below:\n\n"))
        print("\nplease check, is this your message:\n")
        print(m,"\n")
        #print("\n")
        a = input("y/n\n")
        if a != "y":
            print("ok, let's go back...")
        else:
            typemessage = False
            m = m.upper()
            nl = []
            nm = ""
            for l in m:
                if l in letter:
                    p = letter.find(l)
                    n = random.randint(0, 25)
                    nl.append(int(n))
                    np = p + n
                    if np > 25:
                        np = np - 25
                    #nl.append(int(np))
                    nm = nm + letter[np]
                elif l in quotation:
                    q = quotation.index(l)
                    x = random.randint(0,30)
                    #nl.append(str(x) + "|")
                    nl.append(str(x))
                    nq = q + x
                    if nq > 30:
                        nq = nq - 30
                    nm = nm + quotation[nq]
                else:
                    nm = nm + l
            print(nl)
            print("\nThis is your new message:\n")
            print(nm)
            library[nm] = nl
            with open("messages", "wb") as pic:
                print("dumping")
                # lib = open("E:\\1.Python_f\\Glossory\\Tools_main_file\\Pending\\cypher_dcypher\\original\\messages", "w")
                pickle.dump(library, pic)
                print(library)
                print("dumped")            
    
def dtm():
    typ = True
    while typ == True:
        num = input("type your coded message:\n")
        rm = ""
        if num in library:
            typ == False
            print("ok, please wait...")
            n = library[num]
            #n = int(n)
            loop = 0
            t = loop
            for letters in num:




                if letters in letter:
                    #print("letters:   ", letters)
                   # letters = "M"
##                    t = num.find(letters)
                    #print("t:   ", t)
                    o = letter.find(letters)
                    #print("o:   ", o)
                    s = n[t]
                    #print("s:   ", s)
                    newpos = int(o) - int(s)
                    #print("newpos:   ", newpos)
                    if newpos < 0:
                        newpos = newpos + newpos + (newpos * -1) - 1
                    rm = rm + letter[newpos]
                    #print("rm:   ", rm)
                    #print("letters[newpos]:   ", letter[newpos])
                    #print("")
                    

                    t += 1




                elif letters in quotation:
                   # t = num.find(letters)
                    o = quotation.index(letters)
                    s = n[t]
                    newpos = int(o) - int(s)
                    if newpos < 0:
                        newpos = newpos + newpos + (newpos * -1) - 1
                    rm = rm + quotation[newpos]




                    t += 1
                    
                else:
                    rm = rm + letters


                    #t += 1

            print(rm)
            return
            
        else:
            print("we don't have this message.")










##
##
if __name__ == "__main__":
    main()
