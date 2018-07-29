import requests #hadnle http

class Rextester:
    URL = "http://rextester.com/rundotnet/Run" #default Rextester url

    def __init__(self):
        self.session = requests.Session()  # keep session alive

    #execute compilation with given language and code
    def execute(self, language: str, code: str, stdin: str = ''):
        if language.lower() not in LANGUAGES.keys():
            raise RextesterException('unknown_lang')

        _data = {
            'LanguageChoiceWrapper': LANGUAGES.get(language),
            'Program': code,
            'Input': stdin
        }
        r = self.session.post(self.URL, data=_data)

        #if site status is ok
        if r.status_code != requests.codes.ok:
            raise RextesterException('status_code')

        return r.json()


class RextesterException(Exception):
    {}


#avalidable languages
LANGUAGES = {
    'c#': 1,
    'vb': 2,
    'f#': 3,
    'java': 4,
    'python': 5,
    'c_gcc': 6,
    'cpp_gcc': 7,
    'php': 8,
    'pascal': 9,
    'obj-c': 10,
    'haskell': 11,
    'ruby': 12,
    'perl': 13,
    'lua': 14,
    'assembly': 15,
    'sql': 16,
    'js': 17,
    'lisp': 18,
    'prolog': 19,
    'go': 20,
    'scala': 21,
    'scheme': 22,
    'node': 23,
    'python3': 24,
    'octave': 25,
    'c_clang': 26,
    'cpp_clang': 27,
    'cpp_microsoft': 28,
    'c_microsoft': 29,
    'd': 30,
    'r': 31,
    'tcl': 32,
    'mysql': 33,
    'postgre': 34,
    'oracle': 35,
    'swift': 37,
    'bash': 38,
    'ada': 39,
    'erlang': 40,
    'elixir': 41,
    'ocaml': 42,
    'kotlin': 43,
    'brainfuck': 44,
    'fortran': 45
}
