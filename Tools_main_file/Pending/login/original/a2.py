with open("a.py") as f:
    lines = f.readlines()

with open("a.py", "w") as f:
    #lines.insert(0, "a = 1")
  # f.write("\n".join(lines))
    f.write("hello")
    f.delete(all)
