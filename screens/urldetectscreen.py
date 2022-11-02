from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem, BaseListItem

import screens.constant

Builder.load_file('screens/urldetectscreen.kv')


class UrlDetectScreen(Screen):

    def on_pre_enter(self, *args):
        self.ids.url_detect_list.clear_widgets()
        for x in screens.constant.list_url_detect:

            self.ids.url_detect_list.add_widget(
                OneLineListItem(text=x, on_release=lambda this: update(this)))
        return super().on_pre_enter(*args)

    def on_leave(self, *args):
        self.ids.language_list.clear_widgets()
        print("on_leave")
        return super().on_leave(*args)


def url_translate(url):
    if screens.constant.source_language == 'Detect language' == screens.constant.destination_language:
        return url
    return 'http://translate.google.com/translate?js=n&sl=' \
           + screens.constant.list_language_dict[screens.constant.source_language] \
           + '&tl=' + screens.constant.list_language_dict[screens.constant.destination_language] + '&u=' + url


def update(x: OneLineListItem):
    import webbrowser
    webbrowser.open(url_translate(x.text))