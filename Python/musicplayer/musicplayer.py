# coding: utf-8

from os.path import basename

from kivy.core.audio import SoundLoader
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from kivy.clock import Clock
from decimal import Decimal, ROUND_HALF_UP

from simpleplayer.popupchoosefile import PopupChooseFile

class MusicPlayer(BoxLayout):
    sound_path = ''
    sound = None
    popup = None
    is_playing = False
    is_manual_stop = False
    is_repeating = False
    pause_pos = 0
    value_before = 0
    lengh = 0

    def __init__(self, **kwargs):
        print('__init__')
        super(MusicPlayer, self).__init__(**kwargs)

        self._file = Window.bind(
            on_dropfile = self._on_file_drop
        )

    def _on_file_drop(self, window, file_path):
        print('_on_file_drop')
        self.select(file_path.decode('utf-8'))
        return

    def choose(self):
        print('choose')
        content = PopupChooseFile(select=self.select, cancel=self.cancel)
        self.popup = Popup(title='Select Music', content=content)
        self.popup.open()

    def cancel(self):
        print('cancel')
        self.popup.dismiss()
