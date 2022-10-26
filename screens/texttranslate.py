import requests
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from googletrans import Translator

Builder.load_file('screens/texttranslate.kv')


class TextTranslateScreen(Screen):
    def translate(self, text):
        # check internet connection
        url = "http://checkip.amazonaws.com/"
        timeout = 0.3
        try:
            request = requests.get(url, timeout=timeout)
            translator = Translator()
            result = translator.translate(text, src='en', dest='vi')
            self.ids.translated_text.text = result.text
        except (requests.ConnectionError, requests.Timeout) as exception:
            self.ids.translated_text.text = "Please check your internet connection"

    def on_leave(self, *args):
        self.ids.translated_text.text = 'Translated text'
        self.ids.text_input.hint_text = 'Enter Text'
        return super().on_leave(*args)
