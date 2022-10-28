import requests
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from googletrans import Translator
from model.historytranslate import HistoryTranslate
from screens.PopUpScreen import showUrlDetectScreen, showChooseLanguageScreen
from screens.constant import list_language_dict
import screens.constant

Builder.load_file('screens/texttranslate.kv')


def is_translate_from_file():
    return screens.constant.is_translate_from_file


def url_dectect(text):
    regex = r"(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
    import re
    url = re.findall(regex, text)
    return [x[0] + '://' + x[1] + x[2] for x in url]


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
                if self.IDS.src_language.text == 'Detect language' == self.IDS.dest_language.text:
                    self.ids.translated_text.text = self.IDS.text_input.text
                    return
                result = translator.translate(text, src=list_language_dict[self.ids.src_language.text],
                                              dest=list_language_dict[self.ids.dest_language.text])
                self.ids.translated_text.text = result.text
                screens.constant.history_translate.append(
                    HistoryTranslate(text, result.text, self.ids.src_language.text,
                                     self.ids.dest_language.text))
                screens.constant.save_history_translate()

                screens.constant.list_url_detect = url_dectect(result.text)
                print(self.ids.translated_text.text)
                print('url detect' + screens.constant.list_url_detect)
            except TypeError:
                pass
        except (requests.ConnectionError, requests.Timeout) as exception:
            self.ids.translated_text.text = "Please check your internet connection"

    def show_detect_url(self):
        showUrlDetectScreen()

    def show_choose_language_screen(self, type: str):
        if type == 'src':
            showChooseLanguageScreen(self.ids.src_language, type)
        else:
            showChooseLanguageScreen(self.ids.dest_language, type)

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
