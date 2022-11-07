from kivy.uix.popup import Popup
from kivymd.uix.button import MDRectangleFlatButton

import screens.constant
from model.historytranslate import HistoryTranslate
from screens.aboutusscreen import AboutUsScreen
from screens.chooselanguagetransscreen import ChooseLanguageTransScreen
from screens.historytranslatescreen import HistoryTranslateScreen
from screens.urldetectscreen import UrlDetectScreen


def showUrlDetectScreen():
    show = UrlDetectScreen()
    popup_screen = Popup(title='Detect URL', content=show, size_hint=(0.8, 0.8),
                         background='atlas://data/images/defaulttheme/button_pressed')
    show.on_pre_enter()
    popup_screen.open()


def showChooseLanguageScreen(mdRectangleFlatButton: MDRectangleFlatButton, type_screen: str):
    show = ChooseLanguageTransScreen()
    # truyền call back vào đây
    # hàm update nhận sự kiện onlick, truyền callback vào khi nhận hàm update đấy
    # để đóng pop up = popup.dismiss()

    popup_screen = Popup(title='Choose Language', content=show, size_hint=(0.8, 0.8),
                         background='atlas://data/images/defaulttheme/button_pressed')

    on_press = lambda *args: popup_screen.dismiss()
    show.on_pre_enter(mdRectangleFlatButton, on_press, type_screen)
    popup_screen.open()


def showHistoryScreen(type_screen: str, callback=None):
    def on_press_history_item(x: HistoryTranslate):
        popup_screen.dismiss()
        screens.constant.source_language = x.source_lang
        screens.constant.destination_language = x.target_lang
        screens.constant.text_input = x.source
        screens.constant.translated_text = x.target
        if callback is not None:
            callback('_text_translate_screen_')

    show = HistoryTranslateScreen(type_screen, on_press_history_item)
    show.on_pre_enter()
    if type_screen == 'history':
        popup_screen = Popup(title='History', content=show, size_hint=(0.8, 0.8),
                             background='atlas://data/images/defaulttheme/button_pressed')
        popup_screen.open()

    elif type_screen == 'bookmark':
        popup_screen = Popup(title='Bookmark', content=show, size_hint=(0.8, 0.8),
                             background='atlas://data/images/defaulttheme/button_pressed')
        popup_screen.open()

def showAboutUsScreen():
    show = AboutUsScreen()
    popup_screen = Popup(title='About Us', content=show, size_hint=(0.8, 0.8),
                         background='atlas://data/images/defaulttheme/button_pressed')

    show.on_pre_enter()
    popup_screen.open()