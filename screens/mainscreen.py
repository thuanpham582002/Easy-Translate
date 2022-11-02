import docx
from kivy.lang import Builder
from kivy.properties import ListProperty
from plyer import filechooser
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.atlas import Atlas
import screens.constant
from screens.PopUpScreen import showChooseLanguageScreen, showHistoryScreen
from screens.chooselanguagetransscreen import ChooseLanguageTransScreen
from screens.historytranslatescreen import HistoryTranslateScreen

Builder.load_file('screens/mainscreen.kv')

def get_ext_file(path):
    return path.split('.')[-1]


class MainScreen(Screen):
    selection = ListProperty([])

    def __init__(self, **kw):
        super().__init__(**kw)
        self.IDS = None

    # on_kv_post is called after the kv file is loaded
    # and all widgets are created
    # on_kv_post run only once time when screen is created
    def on_kv_post(self, base_widget):
        # self._kv_loaded = True
        super().on_kv_post(base_widget)
        print(self.ids)
        self.IDS = self.ids
        self.IDS.src_language.text = screens.constant.source_language
        self.IDS.dest_language.text = screens.constant.destination_language

    def on_pre_enter(self, *args):
        if self.IDS is not None:
            self.IDS.btn_enter_text_here.text = "Enter text here"
            self.IDS.src_language.text = screens.constant.source_language
            self.IDS.dest_language.text = screens.constant.destination_language

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
        from kivy import platform
        if platform == "android":
            from jnius import autoclass
            Locale = autoclass('java.util.Locale')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            tts = TextToSpeech(PythonActivity.mActivity, None)

            # Play something in english
            tts.setLanguage(Locale.US)
            tts.speak('Hello World.', TextToSpeech.QUEUE_FLUSH, None)

            # Queue something in french
            tts.setLanguage(Locale.FRANCE)
            tts.speak('Bonjour tout le monde.', TextToSpeech.QUEUE_ADD, None)
        elif platform == "ios":
            pass
        elif platform == "win":
            print("Windows")
        from kivy.core.clipboard import Clipboard
        Clipboard.copy('Data')

    def show_choose_file_screen(self):
        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''
        self.selection = selection

    def on_selection(self, *a, **k):
        '''
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        '''
        if not len(self.selection):
            return
        path = str(self.selection[0])
        ext = get_ext_file(self.selection[0])
        if ext == 'txt':
            with open(path, 'r') as f:
                screens.constant.source_language_text = f.read()
                screens.constant.is_translate_from_file = True
                self.change_screen('_text_translate_screen_')

        elif ext == 'docx':
            # read text from docx file
            doc = docx.Document(path)
            fullText = []
            for para in doc.paragraphs:
                fullText.append(para.text)
            screens.constant.source_language_text = '\n'.join(fullText)
            screens.constant.is_translate_from_file = True
            self.change_screen('_text_translate_screen_')

        elif ext == 'pdf':
            # read text from pdf file
            from pdfminer.high_level import extract_text
            text = extract_text(path)
            screens.constant.source_language_text = text
            screens.constant.is_translate_from_file = True
            self.change_screen('_text_translate_screen_')

        elif ext == 'png' or ext == 'jpg' or ext == 'jpeg':
            # read text from image file
            self.IDS.btn_enter_text_here.text = 'Image support is coming soon'
        else:
            self.IDS.btn_enter_text_here.text = screens.constant.message_dont_support_file

        self.selection = []

    def show_about_me_screen(self):
        pass

    def show_history_screen(self, type_screen: str):
        showHistoryScreen(type_screen, self.change_screen)

    def change_screen(self, screen_name):
        self.manager.current = screen_name
