from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

Builder.load_file('screens/chooselanguagetransscreen.kv')

list_language = [
    'English',
    'Spanish',
    'French',
    'German',
    'Italian',
    'Portuguese',
    'Russian',
    'Japanese',
    'Chinese',
    'Korean',
    'Arabic',
    'Turkish',
    'Hindi',
    'Vietnamese',
    'Thai',
    'Indonesian',
    'Persian',
    'Urdu',
    'Bengali',
    'Punjabi',
    'Tamil']


class ChooseLanguageTransScreen(Screen):
    def on_pre_enter(self, *args):
        search: str = self.ids.search_field.text
        self.ids.language_list.clear_widgets()
        for x in list_language:
            if search.lower() in x.lower():
                self.ids.language_list.add_widget(
                    OneLineListItem(text=x, on_release=lambda this: self.update(this)))

        return super().on_pre_enter(*args)

    def update(self, x: OneLineListItem):
        print(x.text)

    def on_leave(self, *args):
        self.ids.language_list.clear_widgets()
        print("on_leave")
        return super().on_leave(*args)
