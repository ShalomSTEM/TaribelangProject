from GameFrame import Level, TextObject
import os

from Objects import ListenerIntro


class Intro(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image(os.path.join("Title", "title_to_wtc.png"))
        self.add_room_object(ListenerIntro(self, 0, 0))
        self.set_timer(60, self.start_wtc_taribelang)

    def start_wtc_taribelang(self):
        self.set_background_image(os.path.join("Title", "WTC_T.png"))
        self.load_sound("WTC_Taribelang.ogg").play()
        self.set_timer(840, self.start_wtc_english)

    def start_wtc_english(self):
        self.set_background_image(os.path.join("Title", "WTC_E.png"))
        self.load_sound("WTC_English.ogg").play()
        self.set_timer(1170, self.complete)

    def complete(self):
        self.running = False
