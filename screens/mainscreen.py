from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.atlas import Atlas

from screens.chooselanguagetransscreen import ChooseLanguageTransScreen

Builder.load_file('screens/mainscreen.kv')


class MainScreen(Screen):
    def show_choose_language_screen(self):
        show = ChooseLanguageTransScreen()
        # truyền call back vào đây
        # hàm update nhận sự kiện onlick, truyền callback vào khi nhận hàm update đấy
        # để đóng pop up = popup.dismiss()
        show.on_pre_enter()

        popup_screen = Popup(title='Choose Language', content=show, size_hint=(0.8, 0.8),
                             background='atlas://data/images/defaulttheme/button_pressed')
        popup_screen.open()
        pass

    def change_screen(self, screen_name):
        self.manager.current = screen_name
