from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd_extensions.akivymd.uix.statusbarcolor import change_statusbar_color
from kivymd.uix.toolbar import MDTopAppBar
from screens.mainscreen import MainScreen
from screens.texttranslate import TextTranslateScreen


# clone UI from Google Translate

class WindowManager(ScreenManager):
    pass


class EasyTranslateApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Purple"
        self.title = "Ứng dụng cho người khiếm thị"
        change_statusbar_color(self.theme_cls.primary_color)

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
