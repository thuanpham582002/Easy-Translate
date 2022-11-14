from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.list import OneLineListItem

import screens.constant
from screens.constant import list_language

Builder.load_file('screens/chooselanguagetransscreen.kv')


class ChooseLanguageTransScreen(Screen):
    def on_pre_enter(self, *args):
        search: str = self.ids.search_field.text
        self.ids.language_list.clear_widgets()
        for x in list_language:
            if search.lower() in x.lower():
                self.ids.language_list.add_widget(
                    OneLineListItem(text=x, on_release=lambda this: self.update(this, args[0], args[1], args[2])))
        return super().on_pre_enter(*args)

    def update(self, x: OneLineListItem, mdRectangleFlatButton: MDRectangleFlatButton = None, callback=None, type=None):
        if mdRectangleFlatButton is not None:
            mdRectangleFlatButton.text = x.text
        if type is not None:
            if type == 'src':
                screens.constant.source_language = x.text
            else:
                screens.constant.destination_language = x.text
        if callback is not None:
            callback()

    def on_leave(self, *args):
        self.ids.language_list.clear_widgets()
        return super().on_leave(*args)
