from lingua import Language


DICT_OF_RU_LANGUAGES = {"ру": "ru", "ан": "en", "ис": "es", "фр": "fr", "нм": "de", "яп": "ja"}
DICT_OF_LANGUAGES = {Language.RUSSIAN: "ru", Language.ENGLISH: "en", Language.SPANISH: "es",
                     Language.FRENCH: "fr", Language.GERMAN: "de", Language.JAPANESE: "ja"}
LANGUAGES = [Language.RUSSIAN, Language.ENGLISH, Language.SPANISH, Language.FRENCH, Language.GERMAN, Language.JAPANESE]
DICT_LANG = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian',
             'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian',
             'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)',
             'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish',
             'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish',
             'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek',
             'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi',
             'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish',
             'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer',
             'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian',
             'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay',
             'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian',
             'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian',
             'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan',
             'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala',
             'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili',
             'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish',
             'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa',
             'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}
VERSIONS_DICT = {"__**0.1.0**__\n": "Created a bot, added basic ability to translate into Spanish and Russian",
                 "__**0.2.0**__\n": "Added main languages on the server, made translation without prefixes, added help "
                                    "menu",
                 "__**0.2.1**__\n": 'A "server" is made for the bot',
                 "__**0.2.2**__\n": "Japanese language added, translation by response added, bot translated to another "
                                    "translator API",
                 "__**0.3.0**__\n": "Completely rewritten commands, made commands insensitive to case, added the "
                                    "ability to translate into several languages, added this command",
                 "__**0.3.1**__\n": "Translation by answer can translate into several languages at once, bug fixed, "
                                    "status added",
                 "__**0.3.2**__\n": "Fix one bug and added 'Good morning' message)",
                 "__**0.3.3**__\n": "Added the ability to send messages about new levels to the bot",
                 "__**0.4.0**__\n": "Code formatted, translation added followed by message removal, debugging features "
                                    "added, some additional commands added, git has also been added to the project",
                 "__**0.4.1**__\n": "Translations now correctly display references",
                 "__**0.4.2**__\n": "Added ban for inactivity",
                 "__**0.5.0**__\n": "The code is divided into separate files, unnecessary functions are removed, all "
                                    "errors are removed",
                 "__**0.5.1**__\n": "Code cleaned up, added beta translation to channels"
                 }
STATE_COMMANDS = " | !sos !versions"
STATE = "вообще-то не играет" + STATE_COMMANDS
CHANNELS_FOR_TRANSLATE = {"ru": 999267959014965258, "es": 999267254384463892, "ja": 999267706861797417}
