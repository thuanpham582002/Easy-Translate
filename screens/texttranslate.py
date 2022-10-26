import requests
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from googletrans import Translator

from screens.chooselanguagetransscreen import ChooseLanguageTransScreen
from screens.constant import list_language_dict
import screens.constant

Builder.load_file('screens/texttranslate.kv')


def is_translate_from_file():
    return screens.constant.is_translate_from_file


class TextTranslateScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.IDS = None

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)
        print(self.ids)
        self.IDS = self.ids
        self.IDS.src_language.text = screens.constant.source_language
        self.IDS.dest_language.text = screens.constant.destination_language
        if is_translate_from_file():
            self.IDS.text_input.text = screens.constant.source_language_text
            screens.constant.is_translate_from_file = False

    def on_pre_enter(self, *args):
        if self.IDS is not None:
            if is_translate_from_file():
                self.IDS.text_input.text = screens.constant.source_language_text
                screens.constant.is_translate_from_file = False
            self.IDS.src_language.text = screens.constant.source_language
            self.IDS.dest_language.text = screens.constant.destination_language

    def translate(self, text):
        # check internet connection
        url = "http://checkip.amazonaws.com/"
        timeout = 0.3
        try:
            request = requests.get(url, timeout=timeout)
            translator = Translator()
            try:
                result = translator.translate(text, src=list_language_dict[self.ids.src_language.text],
                                              dest=list_language_dict[self.ids.dest_language.text])
                self.ids.translated_text.text = result.text
                print(self.ids.translated_text.text)
            except TypeError:
                pass
        except (requests.ConnectionError, requests.Timeout) as exception:
            self.ids.translated_text.text = "Please check your internet connection"

    def show_choose_language_screen(self, type: str):
        show = ChooseLanguageTransScreen()
        # truyền call back vào đây
        # hàm update nhận sự kiện onlick, truyền callback vào khi nhận hàm update đấy
        # để đóng pop up = popup.dismiss()

        popup_screen = Popup(title='Choose Language', content=show, size_hint=(0.8, 0.8),
                             background='atlas://data/images/defaulttheme/button_pressed')

        on_press = lambda *args: popup_screen.dismiss()
        if type == 'src':
            show.on_pre_enter(self.ids.src_language, on_press, type)
        else:
            show.on_pre_enter(self.ids.dest_language, on_press, type)
        popup_screen.open()

    def swap_language(self):
        src = self.ids.src_language.text
        dest = self.ids.dest_language.text
        screens.constant.source_language = dest
        screens.constant.destination_language = src
        self.ids.src_language.text = dest
        self.ids.dest_language.text = src

    def on_leave(self, *args):
        self.ids.translated_text.text = 'Translated text'
        self.ids.text_input.hint_text = 'Enter Text'
        return super().on_leave(*args)
