import tkinter as tk
from model import Model
from view import View

class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.model=Model()
        self.view=View(self.root, self.model)


    def run(self):
        self.view.run()
