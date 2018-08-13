#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import subprocess
import Tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.MainFrame = tk.Frame(self, width=585, height=220)

        self.LabelFrame = tk.Frame(self.MainFrame)
        self.ButtonFrameRoot= tk.Frame(self.MainFrame)
        self.ButtonFrameRegular = tk.Frame(self.MainFrame)

        for frame in [self.MainFrame, self.LabelFrame, self.ButtonFrameRoot, self.ButtonFrameRegular]:
            frame.pack(expand=True, fill='both')
            frame.pack_propagate(0)

        self.label = tk.Label(self.LabelFrame, text='Run as root?')
        self.button_as_root = tk.Button(self.ButtonFrameRoot, text='Root', command=self.run_as_root)
        self.button_as_regular = tk.Button(self.ButtonFrameRoot, text='Regular', command=self.run_as_regular)

        for widget in [self.label, self.button_as_root, self.button_as_regular]:
            widget.pack(expand=True, fill='x', anchor='s')


    def run_as_root(self):
        self.label.configure(text="ROOT")
        
        subprocess.Popen(['gksu', 'gedit']) # вместо gedit - команда или программа, которую нужно запустить под root
        self.destroy() 
    
    def run_as_regular(self):
        self.label.configure(text="Regular")

        program = "gedit"                  # вместо gedit - команда или программа, которую нужно запустить
        process = subprocess.Popen(program) 
        self.destroy()


if __name__ == "__main__":
    root = Window()
    root.mainloop()