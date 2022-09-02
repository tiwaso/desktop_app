# coding: utf-8

from os.path import basename

from kivy.uix.boxlayout import BoxLayout
from tkinter import filedialog
import tkinter


class MusicPlayer(BoxLayout):

    def __init__(self, **kwargs):
        print('__init__')
        super(MusicPlayer, self).__init__(**kwargs)

    def file(self):
        typ=[('', '*')]
        dir = 'C:'
        tk = tkinter.Tk()
        tk.withdraw()
        self.ids.file_name.text = str(filedialog.askopenfilenames(filetypes = typ, initialdir = dir))
        tk.destroy() 
    def play(self):
        pass
    def stop(self):
        pass
    def clock(self):
        pass
    def volume(self):
        pass