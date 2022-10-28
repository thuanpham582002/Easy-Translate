from kivy.uix.popup import Popup
from kivymd.uix.button import MDRectangleFlatButton

from screens.chooselanguagetransscreen import ChooseLanguageTransScreen
from screens.historytranslatescreen import HistoryTranslateScreen
from screens.urldetectscreen import UrlDetectScreen


def showUrlDetectScreen():
    show = UrlDetectScreen()
    popup_screen = Popup(title='Detect URL', content=show, size_hint=(0.8, 0.8),
                         background='atlas://data/images/defaulttheme/button_pressed')
    show.on_pre_enter()
    popup_screen.open()


def showChooseLanguageScreen(mdRectangleFlatButton: MDRectangleFlatButton, type: str):
    show = ChooseLanguageTransScreen()
    # truyền call back vào đây
    # hàm update nhận sự kiện onlick, truyền callback vào khi nhận hàm update đấy
    # để đóng pop up = popup.dismiss()

    popup_screen = Popup(title='Choose Language', content=show, size_hint=(0.8, 0.8),
                         background='atlas://data/images/defaulttheme/button_pressed')

    on_press = lambda *args: popup_screen.dismiss()
    show.on_pre_enter(mdRectangleFlatButton, on_press, type)
    popup_screen.open()


def showHistoryScreen(type: str):
    show = HistoryTranslateScreen(type)
    show.on_pre_enter()
    if type == 'history':
        popup_screen = Popup(title='History', content=show, size_hint=(0.8, 0.8),
                             background='atlas://data/images/defaulttheme/button_pressed')
        popup_screen.open()

    elif type == 'bookmark':
        popup_screen = Popup(title='Bookmark', content=show, size_hint=(0.8, 0.8),
                             background='atlas://data/images/defaulttheme/button_pressed')
        popup_screen.open()
