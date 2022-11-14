
import json
import logging
import random
import re

import requests
from urllib.parse import quote

import screens.constant
from googletranslate.constant import LANGUAGES, DEFAULT_SERVICE_URLS

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


URLS_SUFFIX = [re.search('translate.google.(.*)', url.strip()).group(1) for url in DEFAULT_SERVICE_URLS]
URL_SUFFIX_DEFAULT = 'com'


class google_new_transError(Exception):
    """Exception that uses context to present a meaningful error message"""

    def __init__(self, msg=None, **kwargs):
        self.tts = kwargs.pop('tts', None)
        self.rsp = kwargs.pop('response', None)
        if msg:
            self.msg = msg
        elif self.tts is not None:
            self.msg = self.infer_msg(self.tts, self.rsp)
        else:
            self.msg = None
        super(google_new_transError, self).__init__(self.msg)

    def infer_msg(self, tts, rsp=None):
        cause = "Unknown"

        if rsp is None:
            premise = "Failed to connect"

            return "{}. Probable cause: {}".format(premise, "timeout")
            # if tts.tld != 'com':
            #     host = _translate_url(tld=tts.tld)
            #     cause = "Host '{}' is not reachable".format(host)

        else:
            status = rsp.status_code
            reason = rsp.reason

            premise = "{:d} ({}) from TTS API".format(status, reason)

            if status == 403:
                cause = "Bad token or upstream API changes"
            elif status == 200 and not tts.lang_check:
                cause = "No audio stream in response. Unsupported language '%s'" % self.tts.lang
            elif status >= 500:
                cause = "Uptream API error. Try again later."

        return "{}. Probable cause: {}".format(premise, cause)


def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        import socket
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False


class google_translator:
    '''
    You can use 108 language in target and source,details view LANGUAGES.
    Target language: like 'en'、'zh'、'th'...

    :param url_suffix: The source text(s) to be translated. Batch translation is supported via sequence input.
                       The value should be one of the url_suffix listed in : `DEFAULT_SERVICE_URLS`
    :type url_suffix: UTF-8 :class:`str`; :class:`unicode`; string sequence (list, tuple, iterator, generator)

    :param text: The source text(s) to be translated.
    :type text: UTF-8 :class:`str`; :class:`unicode`;

    :param lang_tgt: The language to translate the source text into.
                     The value should be one of the language codes listed in : `LANGUAGES`
    :type lang_tgt: :class:`str`; :class:`unicode`

    :param lang_src: The language of the source text.
                    The value should be one of the language codes listed in :const:`googletranslate.LANGUAGES`
                    If a language is not specified,
                    the system will attempt to identify the source language automatically.
    :type lang_src: :class:`str`; :class:`unicode`

    :param timeout: Timeout Will be used for every request.
    :type timeout: number or a double of numbers

    :param proxies: proxies Will be used for every request.
    :type proxies: class : dict; like: {'http': 'http:171.112.169.47:19934/', 'https': 'https:171.112.169.47:19934/'}

    '''

    def __init__(self, url_suffix="com", timeout=5, proxies=None):
        self.proxies = proxies
        self.project_id = 'advance-airline-368300'
        if url_suffix not in URLS_SUFFIX:
            self.url_suffix = URL_SUFFIX_DEFAULT
        else:
            self.url_suffix = url_suffix
        url_base = "https://translate.google.{}".format(self.url_suffix)
        self.url = url_base + "/_/TranslateWebserverUi/data/batchexecute"
        self.timeout = timeout
        from kivy import platform
        if platform == 'win':
            from google.cloud import translate_v3beta1 as translate
            self.client = translate.TranslationServiceClient()

    def _package_rpc(self, text, lang_src='auto', lang_tgt='auto'):
        GOOGLE_TTS_RPC = ["MkEWBc"]
        parameter = [[text.strip(), lang_src, lang_tgt, True], [1]]
        escaped_parameter = json.dumps(parameter, separators=(',', ':'))
        rpc = [[[random.choice(GOOGLE_TTS_RPC), escaped_parameter, None, "generic"]]]
        espaced_rpc = json.dumps(rpc, separators=(',', ':'))
        # text_urldecode = quote(text.strip())
        freq_initial = "f.req={}&".format(quote(espaced_rpc))
        freq = freq_initial
        return freq

    def _package_rpc_file(self, path, lang_src='auto', lang_tgt='auto'):
        GOOGLE_FTF = ["LBEnTe"]
        # convert file to mime type
        import mimetypes as mt
        mime_type = mt.guess_type(path)[0]
        # read file
        with open(path, 'rb') as f:
            file_content = f.read()
        # convert file to base64
        import base64
        file_content_base64 = base64.b64encode(file_content)
        # convert base64 to string
        file_content_base64_str = file_content_base64.decode('utf-8')
        print(file_content_base64_str[0:30])
        # package rpc
        parameter = [[file_content_base64_str, mime_type], lang_src, lang_tgt]
        escaped_parameter = json.dumps(parameter, separators=(',', ':'))
        rpc = [[[random.choice(GOOGLE_FTF), escaped_parameter, None, "generic"]]]
        espaced_rpc = json.dumps(rpc, separators=(',', ':'))
        #   print(espaced_rpc)
        freq_initial = "f.req={}&".format(quote(espaced_rpc))
        freq = freq_initial
        return freq

    def translate_file(self, path, lang_tgt='auto', lang_src='auto'):
        if not internet():
            return 'Please check your internet connection.'
        headers = {
            "Referer": "http://translate.google.{}/".format(self.url_suffix),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/107.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        }
        freq = self._package_rpc_file(path, lang_tgt, lang_src)
        response = requests.Request(method='POST',
                                    url=self.url,
                                    data=freq,
                                    headers=headers,
                                    )

        try:
            if self.proxies == None or type(self.proxies) != dict:
                self.proxies = {}
            with requests.Session() as s:
                s.proxies = self.proxies
                r = s.send(request=response.prepare(),
                           verify=False,
                           timeout=self.timeout)
                print(r.status_code)
            for line in r.iter_lines(chunk_size=1024):
                decoded_line = line.decode('utf-8')
                if "LBEnTe" in decoded_line:
                    try:
                        response = decoded_line
                        response = json.loads(response)
                        response = list(response)
                        response = json.loads(response[0][2])
                        response_ = list(response)
                        file_content_base64_str = response_[0][0]
                        print(file_content_base64_str[0:30])
                        mime_type = response_[0][1]
                        # convert base64 to file
                        import base64
                        file_content_base64 = file_content_base64_str.encode('utf-8')
                        file_content = base64.b64decode(file_content_base64)
                        # write file
                        with open('JD-Android-intern1234.docx', 'wb') as f:
                            f.write(file_content)
                    except Exception as e:
                        raise e
            r.raise_for_status()
        except requests.exceptions.ConnectTimeout as e:
            raise e
        except requests.exceptions.HTTPError as e:
            # Request successful, bad response
            raise e
        except requests.exceptions.RequestException as e:
            # Request failed
            raise e

    def translate(self, text, lang_tgt='auto', lang_src='auto', pronounce=False):
        if not internet():
            return 'Please check your internet connection.'
        text = str(text)
        if len(text) >= 5000:
            return "Warning: Can only detect less than 5000 characters"
        if len(text) == 0:
            return ""
        headers = {
            "Referer": "http://translate.google.{}/".format(self.url_suffix),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/107.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        freq = self._package_rpc(text, lang_src, lang_tgt)
        response = requests.Request(method='POST',
                                    url=self.url,
                                    data=freq,
                                    headers=headers,
                                    )
        try:
            if self.proxies == None or type(self.proxies) != dict:
                self.proxies = {}
            with requests.Session() as s:
                s.proxies = self.proxies
                r = s.send(request=response.prepare(),
                           verify=False,
                           timeout=self.timeout)

            for line in r.iter_lines(chunk_size=1024):
                decoded_line = line.decode('utf-8')
                if "MkEWBc" in decoded_line:
                    try:
                        response = decoded_line
                        response = json.loads(response)
                        response = list(response)
                        response = json.loads(response[0][2])
                        response_ = list(response)
                        response = response_[1][0]
                        if len(response) == 1:
                            if len(response[0]) > 5:
                                sentences = response[0][5]
                            else:  ## only url
                                sentences = response[0][0]
                                if pronounce == False:
                                    return sentences
                                elif pronounce == True:
                                    return [sentences, None, None]
                            translate_text = ""
                            for sentence in sentences:
                                sentence = sentence[0]
                                translate_text += sentence.strip() + ' '
                            translate_text = translate_text
                            if pronounce == False:
                                return translate_text
                            elif pronounce == True:
                                pronounce_src = (response_[0][0])
                                pronounce_tgt = (response_[1][0][0][1])
                                return [translate_text, pronounce_src, pronounce_tgt]
                        elif len(response) == 2:
                            sentences = []
                            for i in response:
                                sentences.append(i[0])
                            if pronounce == False:
                                return sentences
                            elif pronounce == True:
                                pronounce_src = (response_[0][0])
                                pronounce_tgt = (response_[1][0][0][1])
                                return [sentences, pronounce_src, pronounce_tgt]
                    except Exception as e:
                        raise e
            r.raise_for_status()
        except requests.exceptions.ConnectTimeout as e:
            raise e
        except requests.exceptions.HTTPError as e:
            # Request successful, bad response
            raise google_new_transError(tts=self, response=r)
        except requests.exceptions.RequestException as e:
            # Request failed
            raise google_new_transError(tts=self)

    def translate_document(self, file_path, lang_tgt='vi'):
        if not internet():
            return 'Please check your internet connection.'
        file_ext = file_path.split('.')[-1]
        file_name_arr = file_path.split("\\")
        file_name = file_name_arr[len(file_name_arr) - 1]
        try:
            mime_type = screens.constant.list_file_ext_support[file_ext]
        except KeyError:
            print('1')
            try:
                with open(file_path, 'r') as f:
                    text = f.read()
                    if len(text) > 5000:
                        return "Warning: Can only detect less than 5000 characters"
                with open(file_path + '-' + lang_tgt + '.' + file_ext, 'wb') as file:
                    file.write(self.translate(text, lang_tgt=lang_tgt).encode('utf-8'))
                    file.close()
                    self.convert_file(file_path + '-' + lang_tgt + '.' + file_ext, file_name, file_path, file_ext)
                return "Translate successfully"
            except Exception as e:
                print(e)
                return screens.constant.message_dont_support_file

        print(mime_type)
        location = 'global'
        parent = f"projects/{self.project_id}/locations/{location}"
        with open(file_path, 'rb') as document:
            document_content = document.read()
        document_input_config = {
            "content": document_content,
            "mime_type": mime_type,
        }
        try:
            response = self.client.translate_document(
                request={
                    "parent": parent,
                    "target_language_code": lang_tgt,
                    "document_input_config": document_input_config,
                }
            )
        except:
            return "Size of file is too large"

        with open(file_path + '-' + lang_tgt + '.' + file_ext, 'wb') as file:
            file.write(response.document_translation.byte_stream_outputs[0])
            # import webbrowser
            # webbrowser.open(file_path + '-' + lang_tgt + "." + "pdf")
            file.close()


        w_file = str(file_path + "-" + lang_tgt + "." + file_ext)
        self.convert_file(w_file, file_name, file_path, file_ext)

        print("Response: Detected Language Code - {}".format(response.document_translation.detected_language_code))
        return "Translate successfully"

    def detect(self, text):
        text = str(text)
        if len(text) >= 5000:
            return log.debug("Warning: Can only detect less than 5000 characters")
        if len(text) == 0:
            return ""
        headers = {
            "Referer": "http://translate.google.{}/".format(self.url_suffix),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/107.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        freq = self._package_rpc(text)
        response = requests.Request(method='POST',
                                    url=self.url,
                                    data=freq,
                                    headers=headers)
        try:
            if self.proxies == None or type(self.proxies) != dict:
                self.proxies = {}
            with requests.Session() as s:
                s.proxies = self.proxies
                r = s.send(request=response.prepare(),
                           verify=False,
                           timeout=self.timeout)

            for line in r.iter_lines(chunk_size=1024):
                decoded_line = line.decode('utf-8')
                if "MkEWBc" in decoded_line:
                    try:
                        response = (decoded_line + ']')
                        response = json.loads(response)
                        response = list(response)
                        response = json.loads(response[0][2])
                        response = list(response)
                        detect_lang = response[0][2]
                    except Exception:
                        raise Exception
                    # data_got = data_got.split('\\\"]')[0]
                    return [detect_lang, LANGUAGES[detect_lang.lower()]]
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # Request successful, bad response
            log.debug(str(e))
            raise google_new_transError(tts=self, response=r)
        except requests.exceptions.RequestException as e:
            # Request failed
            log.debug(str(e))
            raise google_new_transError(tts=self)

    def tts(self, text="Xin chào từ outroom2014", lang_tgt='en'):
        if lang_tgt == 'auto':
            lang_tgt = 'en'
        print("TTS" + text + lang_tgt)
        API_ENDPOINT = "https://translate.google.com/translate_tts"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/107.0.0.0 Safari/537.36", }

        params = {
            'ie': 'UTF-8',
            'q': text,
            'tl': lang_tgt,
            'client': 'gtx'
        }

        r = requests.get(API_ENDPOINT, params=params, headers=headers)
        print(r.status_code)

        with open("clip.mp3", 'wb') as f:
            f.write(r.content)
            # path file
            import os
            path = os.path.abspath("clip.mp3")
            return path

    def convert_file(self, file, file_name, file_path, ext):
        import webbrowser
        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
        if (ext == "docx"):
            from docx2pdf import convert
            convert(str(file), str(file_path + ".pdf"))
            webbrowser.get("edge").open(str(file_path + ".pdf"))
        elif (ext == "xlsx"):
            import asposecellscloud
            cellsApi = asposecellscloud.apis.cells_api.CellsApi("f01b002e-50ce-4e38-b803-c7699ecb34a1",
                                                                "0f5b39c2a73c8f4dfe0502b3fbf5bbf6", "v3.0")

            fullfilename = file
            format = 'pdf'
            password = None
            outPath = None
            result = cellsApi.cells_workbook_put_convert_workbook(fullfilename, format=format)
            webbrowser.get("edge").open(result)
        else:
            import os
            os.startfile(file)


    def open_with_browser(self, file_path):
        import webbrowser
        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
        webbrowser.get("edge").open(file_path)





