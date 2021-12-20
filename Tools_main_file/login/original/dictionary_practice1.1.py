##from dictionary_practice1 import teas
#f = open("dictionary_practice1.py", "w")
#print(teas)
#teas.update(hello = "good")
with open ("dictionary_practice1.py", "w") as f:
    f.write("\nteas.update hello = good")
    #outFile = open("file1.py","w")
    f.writelines("teas = " % (str(1)))
#outFile.close()
#print(teas)


##d = {'x': 2}
##
##d.update(y = 3, z = 0)
##print(d)
##
