from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar

import screens.constant
from screens.mainscreen import MainScreen
from screens.texttranslate import TextTranslateScreen
from screens.chooselanguagetransscreen import ChooseLanguageTransScreen
from jnius import autoclass


# clone UI from Google Translate
class WindowManager(ScreenManager):
    pass

class EasyTranslateApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Purple"
        self.title = "Easy Translate"
        screens.constant.history_translate = screens.constant.load_history_translate()

    def build(self):
        return WindowManager()

    def on_start(self):
        Window.bind(on_keyboard=self.events)

    def events(self, window, key, *args):
        if key == 27:
            if self.root.current == '_main_screen_':
                return False
            self.root.current = self.root.previous()
            return True

EasyTranslateApp().run()
