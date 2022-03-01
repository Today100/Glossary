import json
n = {"hello":"good day"}

f = open("demofile2.just", "a")
json.dump(n, f)
f.close()

#open and read the file after the appending:
f = open("demofile2.just", "r")
print(f.read())
