
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

source_language = 'English'
destination_language = 'Vietnamese'

source_language_text = ''

is_translate_from_file = False

list_file_ext_support = [
    '.txt',
    '.doc',
    '.docx',
    '.pdf',
]

message_dont_support_file = 'This file is not supported, please choose another file (only support .txt .dox .pdf .img ' \
                            '.jpg .jpeg) '
