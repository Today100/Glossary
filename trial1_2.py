from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
import trial1






class Tip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 300     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

class Cp(ttk.Frame):
	"""
	-----USAGE-----
	collapsiblePane = CollapsiblePane(parent,
						expanded_text =[string],
						collapsed_text =[string])

	collapsiblePane.pack()
	button = Button(collapsiblePane.frame).pack()
	"""

	def __init__(self, parent, expanded_text ="Collapse <<",
							collapsed_text ="Expand >>"):

		ttk.Frame.__init__(self, parent)

		# These are the class variable
		# see a underscore in expanded_text and _collapsed_text
		# this means these are private to class
		self.parent = parent
		self._expanded_text = expanded_text
		self._collapsed_text = collapsed_text

		# Here weight implies that it can grow it's
		# size if extra space is available
		# default weight is 0
		self.columnconfigure(1, weight = 1)

		# Tkinter variable storing integer value
		self._variable = IntVar()

		# Checkbutton is created but will behave as Button
		# cause in style, Button is passed
		# main reason to do this is Button do not support
		# variable option but checkbutton do
		self._button = ttk.Checkbutton(self, variable = self._variable,
							command = self._activate, style ="TButton")
		self._button.grid(row = 0, column = 0)

		# This wil create a separator
		# A separator is a line, we can also set thickness
		self._separator = ttk.Separator(self, orient ="horizontal")
		self._separator.grid(row = 0, column = 1, sticky ="we")

		self.frame = ttk.Frame(self)

		# This will call activate function of class
		self._activate()

	def _activate(self):
		if not self._variable.get():

			# As soon as button is pressed it removes this widget
			# but is not destroyed means can be displayed again
			self.frame.grid_forget()

			# This will change the text of the checkbutton
			self._button.configure(text = self._collapsed_text)

		elif self._variable.get():
			# increasing the frame area so new widgets
			# could reside in this container
			self.frame.grid(row = 1, column = 0, columnspan = 2)
			self._button.configure(text = self._expanded_text)

	def toggle(self):
		"""Switches the label frame to the opposite state."""
		self._variable.set(not self._variable.get())
		self._activate()


def cp_text_example():
    cpane = Cp(root, 'Expanded', 'Collapsed')
    cpane.grid(row = 0, column = 0)

    # Button and checkbutton, these will
    # appear in collapsible pane container
    b1 = Button(cpane.frame, text ="GFG").grid(
                row = 1, column = 2, pady = 10)

    cb1 = Checkbutton(cpane.frame, text ="GFG").grid(
                    row = 2, column = 3, pady = 10)

