from io import TextIOBase, TextIOWrapper


f = "E:\\1.Python_f\\Glossory\\Tools_main_file\\story_connect\\write_in_file\\sample.py"

# line.strip("\n") != "line2":
# Delete "line2" from new_file

#         new_file.write(line)

def r(file, text):
    count = 0
    c = []
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    f = open(file, "w")
    # del lines[1]
    for x in lines:
        # print(x)
        # print(x)
        if text.split(" = ")[0] not in x.strip("\n") and text.split("=")[0] not in x.strip("\n") :
            f.write(x)
    
    f.write("\n"+text)
        
    
    


r(f, "n = 'yes'")

