from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.atlas import Atlas

from screens.chooselanguagetransscreen import ChooseLanguageTransScreen

Builder.load_file('screens/mainscreen.kv')


class MainScreen(Screen):
    def show_choose_language_screen(self, type: str):
        show = ChooseLanguageTransScreen()
        # truyền call back vào đây
        # hàm update nhận sự kiện onlick, truyền callback vào khi nhận hàm update đấy
        # để đóng pop up = popup.dismiss()

        popup_screen = Popup(title='Choose Language', content=show, size_hint=(0.8, 0.8),
                             background='atlas://data/images/defaulttheme/button_pressed')

        on_press = lambda *args: popup_screen.dismiss()
        if type == 'src':
            show.on_pre_enter(self.ids.src_language, on_press)
        else:
            show.on_pre_enter(self.ids.dest_language, on_press)
        popup_screen.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name
