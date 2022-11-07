import socket
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import googletranslate.google_trans_new
from model.historytranslate import HistoryTranslate
from screens.PopUpScreen import showUrlDetectScreen, showChooseLanguageScreen
from screens.constant import list_language_dict
import screens.constant

Builder.load_file('screens/texttranslate.kv')


def is_translate_from_file():
    return screens.constant.is_translate_from_file


def url_detect(text):
    regex = r"(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
    import re
    url = re.findall(regex, text)
    return [x[0] + '://' + x[1] + x[2] for x in url]


def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False


class TextTranslateScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.IDS = None
<<<<<<< Updated upstream
=======
        if platform == 'android':
            self.mplayer_andr = MusicPlayerAndroid()
        self.translator = googletranslate.google_trans_new.google_translator()
>>>>>>> Stashed changes

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)
        print(self.ids)
        self.IDS = self.ids
        self.IDS.text_input.text = screens.constant.text_input
        screens.constant.text_input = ''
        self.IDS.translated_text.text = screens.constant.translated_text
        screens.constant.translated_text = ''
        self.IDS.src_language.text = screens.constant.source_language
        self.IDS.dest_language.text = screens.constant.destination_language
        if is_translate_from_file():
            self.IDS.text_input.text = screens.constant.source_language_text
            screens.constant.is_translate_from_file = False

    def on_pre_enter(self, *args):
        if self.IDS is not None:
            self.IDS.text_input.text = screens.constant.text_input
            screens.constant.text_input = ''
            self.IDS.translated_text.text = screens.constant.translated_text
            screens.constant.translated_text = ''
            if is_translate_from_file():
                self.IDS.text_input.text = screens.constant.source_language_text
                screens.constant.is_translate_from_file = False
            self.IDS.src_language.text = screens.constant.source_language
            self.IDS.dest_language.text = screens.constant.destination_language

    def translate(self, text):
        # check internet connection
        if not internet():
            self.IDS.translated_text.text = 'No internet connection'
            return
        translator = googletranslate.google_trans_new.google_translator()
        try:
            if self.IDS.src_language.text == 'Detect language' == self.IDS.dest_language.text:
                self.ids.translated_text.text = self.IDS.text_input.text
                return
            result = translator.translate(text, lang_src=list_language_dict[self.ids.src_language.text],
                                          lang_tgt=list_language_dict[self.ids.dest_language.text])
            self.ids.translated_text.text = result
            screens.constant.history_translate.append(
                HistoryTranslate(text, result, self.ids.src_language.text,
                                 self.ids.dest_language.text))
            screens.constant.save_history_translate()

            screens.constant.list_url_detect = url_detect(result)
            print(self.ids.translated_text.text)
        except Exception as e:
            print('text translate', e)

    def show_detect_url(self):
        showUrlDetectScreen()

    def show_choose_language_screen(self, type_screen: str):
        if type_screen == 'src':
            showChooseLanguageScreen(self.ids.src_language, type_screen)
        else:
            showChooseLanguageScreen(self.ids.dest_language, type_screen)

    def swap_language(self):
        src = self.ids.src_language.text
        dest = self.ids.dest_language.text
        screens.constant.source_language = dest
        screens.constant.destination_language = src
        self.ids.src_language.text = dest
        self.ids.dest_language.text = src
        tmp = self.ids.text_input.text
        self.ids.text_input.text = self.ids.translated_text.text
        self.ids.translated_text.text = tmp
