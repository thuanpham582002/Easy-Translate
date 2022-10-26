from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.list import OneLineListItem

Builder.load_file('screens/chooselanguagetransscreen.kv')

list_language_dict = {
    'Detect language': 'auto',
    'English': 'en',
    'Vietnamese': 'vi',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Chinese': 'zh-CN',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Spanish': 'es',
    'Russian': 'ru',
    'Portuguese': 'pt',
    'Arabic': 'ar',
    'Hindi': 'hi',
    'Indonesian': 'id',
    'Malay': 'ms',
    'Thai': 'th',
    'Turkish': 'tr',
    'Urdu': 'ur',
    'Bengali': 'bn',
    'Dutch': 'nl',
    'Filipino': 'tl',
    'Greek': 'el',
    'Hebrew': 'iw',
    'Hmong': 'hmn',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Javanese': 'jw',
    'Kannada': 'kn',
    'Khmer': 'km',
    'Lao': 'lo',
    'Latin': 'la',
    'Mongolian': 'mn',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Persian': 'fa',
    'Polish': 'pl',
    'Romanian': 'ro',
    'Serbian': 'sr',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Ukrainian': 'uk',
}
list_language = list(list_language_dict.keys())


class ChooseLanguageTransScreen(Screen):
    def on_pre_enter(self, *args):
        search: str = self.ids.search_field.text
        self.ids.language_list.clear_widgets()
        for x in list_language:
            if search.lower() in x.lower():
                self.ids.language_list.add_widget(
                    OneLineListItem(text=x, on_release=lambda this: self.update(this, args[0], args[1])))
        return super().on_pre_enter(*args)

    def update(self, x: OneLineListItem, mdRectangleFlatButton: MDRectangleFlatButton = None, callback=None):
        if mdRectangleFlatButton is not None:
            mdRectangleFlatButton.text = x.text

        if callback is not None:
            callback()

    def on_leave(self, *args):
        self.ids.language_list.clear_widgets()
        print("on_leave")
        return super().on_leave(*args)
