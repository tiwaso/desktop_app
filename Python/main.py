# coding: utf-8

from os import environ

from kivy.app import App

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path('{}\\{}'.format(environ['SYSTEMROOT'], 'Fonts'))
LabelBase.register(DEFAULT_FONT, 'MSGOTHIC.ttc')

from kivy.uix.label import Label
# from musicplayer.musicplayer import MusicPlayer

class Kaikeydrive(App):
    def build(self):
        return Label()
    # def build(self):
    #     return MusicPlayer()

if __name__ == "__main__":
    Kaikeydrive().run()