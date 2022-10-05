from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd_extensions.akivymd.uix.statusbarcolor import change_statusbar_color

# creating the App class in which name
# .kv file is to be named PageLayout.kv

kv = """
<BottomAppbar>:

    MDBoxLayout:
        orientation: "vertical"

        MyToolbar:
            id: _toolbar

        MDBoxLayout:

    AKFloatingRoundedAppbar:

        AKFloatingRoundedAppbarButtonItem:
            icon: "magnify"
            text: "Search"
            on_release: root.toast(self.text)

        AKFloatingRoundedAppbarButtonItem:
            icon: "plus"
            text: "Add"
            on_release: root.toast(self.text)

        AKFloatingRoundedAppbarButtonItem:
            icon: "dots-vertical"
            text: "Menu"
            on_release: root.toast(self.text)

        AKFloatingRoundedAppbarAvatarItem:
            source: "assets/google.jpg"

        AKFloatingRoundedAppbarAvatarItem:
            source: "assets/google.jpg"
            text: "Google"
"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"
        self.title = "Awesome KivyMD"
        change_statusbar_color(self.theme_cls.primary_color)

    def build(self):
        self.root = Builder.load_string(kv)


if __name__ == "__main__":
    MainApp().run()
