from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file('screens/aboutusscreen.kv')
class AboutUsScreen(Screen):

    def on_pre_enter(self, *args):

        return super().on_pre_enter(*args)

    def on_leave(self, *args):
        return super().on_leave(*args)

    def on_click(self):
        import webbrowser
        webbrowser.open("https://github.com/PythonHDN/fa-4_4")



