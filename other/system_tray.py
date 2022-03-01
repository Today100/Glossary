# from infi.systray import SysTrayIcon
# def say_hello(systray):
#     print("Hello, World!")
# menu_options = (("Say Hello", None, say_hello),)
# systray = SysTrayIcon("icn.ico", "Example tray icon", menu_options)
# systray.start()


from pystray import *
import pystray
from PIL import Image

def action():
    print("Hello world!")
    print('byebye!')

def action2():
    print("Oh, Hello!!!!!")
image = Image.open("noodle.ico")
menu = pystray.Menu(pystray.MenuItem('Call something', lambda :  action(), default=True), pystray.MenuItem('name2', action2))
icon = pystray.Icon("name", image, "title", menu)
icon.run()
# item('Call something', lambda :  method())

# from pystray import Icon as icon, Menu as menu, MenuItem as item

# state = 0

# def set_state(v):
#     def inner(icon, item):
#         global state
#         state = v
#     return inner

# def get_state(v):
#     def inner(item):
#         return state == v
#     return inner

# # Let the menu items be a callable returning a sequence of menu
# # items to allow the menu to grow
# icon('test', image, menu=menu(lambda: (
#     item(
#         'State %d' % i,
#         set_state(i),
#         checked=get_state(i),
#         radio=True)
#     for i in range(max(5, state + 2))))).run()