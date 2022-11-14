import json

from model.historytranslate import HistoryTranslate

list_language_dict = {
    'Detect language': 'auto',
    'English': 'en',
    'Vietnamese': 'vi',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Chinese': 'zh-CN',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Spanish': 'es',
    'Russian': 'ru',
    'Portuguese': 'pt',
    'Arabic': 'ar',
    'Hindi': 'hi',
    'Indonesian': 'id',
    'Malay': 'ms',
    'Thai': 'th',
    'Turkish': 'tr',
    'Urdu': 'ur',
    'Bengali': 'bn',
    'Dutch': 'nl',
    'Filipino': 'tl',
    'Greek': 'el',
    'Hebrew': 'iw',
    'Hmong': 'hmn',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Javanese': 'jw',
    'Kannada': 'kn',
    'Khmer': 'km',
    'Lao': 'lo',
    'Latin': 'la',
    'Mongolian': 'mn',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Persian': 'fa',
    'Polish': 'pl',
    'Romanian': 'ro',
    'Serbian': 'sr',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Ukrainian': 'uk',
}
list_language = list(list_language_dict.keys())
text_input = ''
translated_text = ''
source_language = 'English'
destination_language = 'Vietnamese'
source_language_text = ''
is_translate_from_file = False
list_file_ext_support = {
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'pdf': 'application/pdf',
    'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
}

list_url_detect = []
message_dont_support_file = 'This file is not supported, please choose another file (only support .txt .dox .pdf .pttx .xlxs) '
history_translate = []


def save_history_translate():
    with open('history_translate.json', 'w') as file:
        import os
        print(os.getcwd())
        json.dump([ob.__dict__ for ob in history_translate], file)


def load_history_translate():
    try:
        with open('history_translate.json', 'r') as file:
            return json.load(file, object_hook=lambda d: HistoryTranslate(**d))
    except FileNotFoundError:
        return []
