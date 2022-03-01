import tkinter as tk
import tkinter.ttk as ttk

def show_dialog(parent):
    dlg = tk.Toplevel()
    dlg.wm_title("Dialog box")
    dlg.wm_transient(parent)

    frame = ttk.Frame(dlg)
    label = ttk.Label(frame, text="Message:")
    entry = ttk.Entry(frame, width=30)
    button = ttk.Button(frame, text="Comment")

    label.grid(row=0, column=0, columnspan=2, sticky='NEWS')
    entry.grid(row=1, column=0, sticky='NEWS')
    button.grid(row=1, column=1, sticky='NEWS')

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(2, weight=1)

    frame.grid(row=0, column=0, sticky='NEWS')
    dlg.grid_columnconfigure(0, weight=1)
    dlg.grid_rowconfigure(0, weight=1)

    entry.focus()
    dlg.grab_set()
    dlg.tk.eval('tk::PlaceWindow {0} widget {1}'.format(dlg, parent))

def main():
    root = tk.Tk()
    root.geometry('320x120')
    root.wm_title("Demo application")
    comment_button = ttk.Button(root, text="Comment", command=lambda: show_dialog(root))
    comment_button.pack(anchor=tk.CENTER)
    root.mainloop()

if __name__ == '__main__':
    main()

