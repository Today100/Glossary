# import logging
# import threading
# import time

# def thread_function(name=None):
#     print("Thread %s: starting", name)
#     time.sleep(10)
#     print("working on it")
#     for x in range(10):
#         print(x)
#     print("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"


#     print("Main    : before creating thread")
#     x = threading.Thread(target=thread_function)
#     print("Main    : before running thread")
#     x.start()
#     print("Main    : wait for the thread to finish")
#     x.join()
#     print("Main    : all done")

# # x = 0
# # while True:
# #     print("Hello")
# #     x += 1
# #     if x == 15:
# #         exit()



from tkinter import *

root = Tk()

def click(e):
    print("clicked")
    un()

def one():
    global x
    x = Button(root, text="Hello world")
    x.pack()
    x.bind("<Button-1>", click)

def un():
    x.unbind("<Button-1>")

one()
# un()
root.mainloop()