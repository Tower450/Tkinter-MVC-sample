from tkinter import *

class View():
    def __init__(self, root, model):
        self.frame = root
        self.model = model
        self.label = Label(self.frame, text="Hello World")

    def run(self):
        print ("this is view")
        self.frame.title("Tkinter MVC sample")
        self.frame.geometry('%dx%d+%d+%d' % (self.model.rootWidth, self.model.rootHeight, self.model.xpoint, self.model.ypoint))
        self.label.pack()
        self.frame.mainloop()
