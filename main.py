from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd_extensions.akivymd.uix.statusbarcolor import change_statusbar_color
from kivymd.uix.toolbar import MDTopAppBar

# clone UI from Google Translate
kv = """
<MyToolbar@MDTopAppBar>:
    elevation: 10

MDScreen:
    ScreenManager:
        id: screen_manager
        
        MDScreen:
            name: "Home"
            MDBoxLayout:
                orientation: "vertical"
                size_hint: 1, 1
                BoxLayout:
                    size_hint: 1, 0.1
                    orientation: "horizontal"
                    Button:
                        size_hint: 0.15, 1
                    Label:
                        size_hint: 0.8, 1
                        text: "Easy Translate"
                        color: 0, 0, 0, 1
                    Button:
                        icon: "reload"
                        size_hint: 0.15, 1
                        MDBoxLayout:
                BoxLayout:
                    size_hint: 1, 0.5
                    TextInput:
                        hint_text: "Enter text here"
                        padding: 10
                BoxLayout:
                    size_hint: 1, 0.4
                    orientation: "vertical"
                    BoxLayout:
                        size_hint: 1, 0.3
                        Button:
                            size_hint: 0.15, 1
                        Button:
                            size_hint: 0.7, 1
                            text: "Translate"
                        Button:
                            size_hint: 0.15, 1
                    BoxLayout:
                        size_hint: 1, 0.7
                        BoxLayout:
                            pos_hint: {"center_x": .5, "center_y": .5}
                            size_hint: 0.15, 1
                            orientation: "vertical"
                            MDIconButton:
                                pos_hint: {"center_x": .5, "center_y": .5}
                                icon: "arrow-left"
                            Label:
                                pos_hint: {"center_x": .5, "center_y": .5}
                                text: "English"
                                color: 0, 0, 0, 1
                        BoxLayout:
                            size_hint: 0.7, 1
                            orientation: "vertical"
                            MDIconButton:
                                pos_hint: {"center_x": .5, "center_y": .5}
                                icon: "arrow-right"
                            Label:
                                pos_hint: {"center_x": .5, "center_y": .5}
                                text: "Vietnamese"
                                color: 0, 0, 0, 1
                        BoxLayout:
                            size_hint: 0.15, 1
                            orientation: "vertical"
                            MDIconButton:
                                pos_hint: {"center_x": .5, "center_y": .5}
                                icon: "arrow-left"
                            Label:
                                pos_hint: {"center_x": .5, "center_y": .5}
                                text: "Vietnamese"   
                                color: 0, 0, 0, 1                     
"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"
        self.title = "Awesome KivyMLLL"
        change_statusbar_color(self.theme_cls.primary_color)

    def build(self):
        self.root = Builder.load_string(kv)
        return self.root


MainApp().run()
