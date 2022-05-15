import asyncio
import random
from discord.utils import get


import discord
from discord.ext import commands
from translate import Translator
from lingua import Language, LanguageDetectorBuilder
import cryptocode

from os import name

import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import interactions

bot = commands.Bot(command_prefix='!')
slash = SlashCommand(bot, sync_commands=True)
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


'''@slash.slash(name="t", description="Translation to russian", guild_ids=[955197429999861800],
             options=[create_option("Text", "Text to translate", required=True, option_type=3)])
async def trans(ctx: SlashContext, text):
    await ctx.send(return_send_trans(text))'''

@bot.command()
@commands.has_permissions(administrator=True)
async def g_m(ctx):
    f = random.randint(1, 7)
    await ctx.send(random.choice(["Good morning)", "Good morning))", "Good morning!", r"Good morning! \♥‿\♥",
                                  "Good morning!!", "Go" + "o" * f + "od morning!!",
                                  r"Good morning! \:)", r"Good morning \:)"]))
    await ctx.message.delete()


@bot.command()
@commands.has_permissions(administrator=True)
async def delete(ctx, *a):
    if int(a[0]) < 5 or a[1] == "True":
        await ctx.channel.purge(limit=int(a[0]) + 1)
    else:
        await ctx.message.delete()


@bot.command()
@commands.has_permissions(administrator=True)
async def send(ctx):
    mess = ctx.message.content.split(" ")
    channel = ctx.channel
    if len(mess[1]) == len(str(968166014594469888)):
        channel = bot.get_channel(int(mess[1]))
        await channel.send(" ".join(mess[2:]))
    else:
        await channel.send(" ".join(mess[1:]))
    await ctx.message.delete()


@bot.event
async def on_message(message_in):
    if message_in.channel.id == 968102452417155162 and len(message_in.mentions) == 1:
        level = message_in.content.split(" ")[-1][:-1]
        n = message_in.mentions[0]
        guild = bot.get_guild(955197429999861800)
        role0, role1, role3, role5, role7, role9 = guild.get_role(967760259131260928), guild.get_role(967753494352253029), guild.get_role(967758027769933824), guild.get_role(967758307534209064), guild.get_role(967758254920859688), guild.get_role(967758514233679883)
        if str(level) in "13579":
            print(role9)
            print(n.roles)
            if role9 not in n.roles:
                print(1)
                await n.remove_roles(role0, role1, role3, role5, role7, role9)
                channel1 = bot.get_channel(968166014594469888)
                if int(level) == 1:
                    await n.add_roles(role1)
                    await channel1.send(f"Congratulations! <@{n.id}> received level {1}")
                if int(level) == 3:
                    await n.add_roles(role3)
                    await channel1.send(f"Congratulations! <@{n.id}> received level {2}")
                if int(level) == 5:
                    await n.add_roles(role5)
                    await channel1.send(f"Congratulations! <@{n.id}> received level {3}")
                if int(level) == 7:
                    await n.add_roles(role7)
                    await channel1.send(f"Congratulations! <@{n.id}> received level {4}")
                if int(level) == 9:
                    await n.add_roles(role9)
                    await channel1.send(f"Congratulations! <@{n.id}> received level {5}")
        return


    if message_in.author == bot.user:
        return
    message = message_in.content.lower()
    num_min_lang = 0
    list_keys = list()
    msg = message_in

    if message.split(" ")[0] == "п" or message.split(" ")[0] == "t":  # перевод по ответу
        cont_f = False
        if len(message.split(" ")) == 1:
            cont_f = True
            if message.split(" ")[0].lower() == "п":
                list_keys.append([0, "ru"])
            else:
                list_keys.append([0, "en"])
        flag_err = False
        if not cont_f:
            for q in range(len(message.split(" ")[1:])):
                if message.split(" ")[1:][q] in DICT_OF_RU_LANGUAGES.values() or \
                        message.split(" ")[1:][q] in DICT_OF_RU_LANGUAGES.keys():
                    if message.split(" ")[1:][q] in DICT_OF_RU_LANGUAGES.keys():
                        list_keys.append([1, message.split(" ")[1:][q]])  # если русский
                    else:
                        list_keys.append([0, message.split(" ")[1:][q]])  # если непонятно
                else:
                    flag_err = True
                    break
        if flag_err:
            print("err")
            return
        print(list_keys)
        if message_in.reference and (msg := message_in.reference.resolved) and isinstance(msg, discord.Message):
            await message_in.delete()

            if len(list_keys) > 0:
                if len(list_keys) <= 5:
                    if list_keys[0][0] == 0:
                        await send_trans(message_in.channel, translate(None, True, list_keys[0][1],
                                                                       msg.content.split(" ")),
                                         answer=message_in.reference.resolved)
                    else:
                        await send_trans(message_in.channel,
                                         translate("ru", False, DICT_OF_RU_LANGUAGES[list_keys[0][1]],
                                                   msg.content.split(" ")), answer=message_in.reference.resolved)
                else:
                    list_keys = list_keys[:5]
                    if list_keys[0][0] == 0:
                        await send_trans(message_in.channel, translate(None, True, list_keys[0][1],
                                                                       msg.content.split(" ")),
                                         answer=message_in.reference.resolved,
                                         text="Maximum you can translate 5 languages")
                    else:
                        await send_trans(message_in.channel,
                                         translate("ru", False, DICT_OF_RU_LANGUAGES[list_keys[0][1]],
                                                   msg.content.split(" ")),
                                         answer=message_in.reference.resolved,
                                         text="Maximum you can translate 5 languages")

                list_keys.pop(0)
                for q in list_keys:
                    if q[0] == 0:
                        await send_trans(message_in.channel, translate(None, True, q[1],
                                                                       msg.content.split(" ")))
                    else:
                        await send_trans(message_in.channel, translate("ru", False, DICT_OF_RU_LANGUAGES[q[1]],
                                                                       msg.content.split(" ")))

        return

    list_keys = list()
    for q in range(len(message.split(" "))):
        if message.split(" ")[q] in DICT_OF_RU_LANGUAGES.values() or \
                message.split(" ")[q] in DICT_OF_RU_LANGUAGES.keys():
            if message.split(" ")[q] in DICT_OF_RU_LANGUAGES.keys():
                list_keys.append([1, message.split(" ")[q]])  # если русский
            else:
                list_keys.append([0, message.split(" ")[q]])  # если непонятно
        else:
            break
    if len(list_keys) > 0:
        if len(list_keys) < 5:
            if list_keys[0][0] == 0:
                await send_trans(message_in.channel, translate(None, True, list_keys[0][1],
                                                               message_in.content.split(" ")[len(list_keys):]),
                                 message_in)
            else:
                await send_trans(message_in.channel, translate("ru", False, DICT_OF_RU_LANGUAGES[list_keys[0][1]],
                                                               message_in.content.split(" ")[len(list_keys):]),
                                 message_in)
        else:
            num_min_lang = len(list_keys) - 5
            list_keys = list_keys[:5]
            if list_keys[0][0] == 0:
                await send_trans(message_in.channel, translate(None, True, list_keys[0][1],
                                                               message_in.content.split(" ")[len(list_keys):]),
                                 message_in, text="Maximum you can translate 5 languages")
            else:
                await send_trans(message_in.channel, translate("ru", False, DICT_OF_RU_LANGUAGES[list_keys[0][1]],
                                                               message_in.content.split(" ")[len(list_keys):]),
                                 message_in, text="Maximum you can translate 5 languages")

        list_keys.pop(0)
        for q in list_keys:
            if q[0] == 0:
                await send_trans(message_in.channel, translate(None, True, q[1],
                                                               message_in.content.split(" ")[len(list_keys) +
                                                                                             1 + num_min_lang:]))
            else:
                await send_trans(message_in.channel, translate("ru", False, DICT_OF_RU_LANGUAGES[q[1]],
                                                               message_in.content.split(" ")[len(list_keys) +
                                                                                             1 + num_min_lang:]))

    await bot.process_commands(message_in)


'''@slash.slash(name="hello", description="Just Sends a Message", guild_ids=[691127432165589013], options=[create_option(name="text", description="Enter Anon Text", required=True, option_type=3)])
async def _hello(ctx:SlashContext, text:str):
  await ctx.send(text, hidden=True)'''

'''try:
    await message.add_reaction(message.content)
except BaseException:
    pass'''  # реакция


@bot.event
async def on_ready():
    print('Сonnected')
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game("вообще-то не играет... | !heeelp !versions"))
    print('Status complete')


@bot.command()
async def off_stat(ctx):
    print('Status complete')
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.CustomActivity("вообще-то не играет... | !heeelp !versions"))


@bot.command()
async def on_stat(ctx):
    print('Status complete')
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game("вообще-то не играет... | !heeelp !versions"))


@bot.command()
async def custom_stat(ctx, *args):
    print('Status complete', " ".join(args))
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(" ".join(args) + " | !heeelp !versions"))


def mess_lang(a, b):
    c = ""
    try:
        c = DICT_LANG[a][0].upper() + DICT_LANG[a][1:] + " " + "(" + a + ")" + " " + "→" + " "
    except BaseException:
        c = a + " " + "→" + " "
    c1 = c
    try:
        c = c + DICT_LANG[b][0].upper() + DICT_LANG[b][1:] + " " + "(" + b + ")"
    except BaseException:
        c = c1 + b
    return c


def detect_lang(mess):
    detector = LanguageDetectorBuilder.from_languages(*LANGUAGES).build()
    lang_1 = detector.detect_language_of(str(" ".join(list(mess))))
    print("Detected land of {}".format(DICT_OF_LANGUAGES[lang_1]))
    return DICT_OF_LANGUAGES[lang_1]


def translate(into_l, it_messing, on_l, args):
    if it_messing:
        lang_1 = detect_lang(args)
    else:
        lang_1 = into_l
    translator = Translator(from_lang=lang_1, to_lang=on_l)
    g = translator.translate(str(" ".join(list(args))))
    return g, mess_lang(lang_1, on_l)


async def send_trans(channel, message, answer=None, text=""):
    trans, lang = message
    emb = discord.Embed(color=discord.Color.green())
    emb.add_field(name=">>> " + trans, value="*" + lang + "*", inline=False)
    if answer is None:
        await channel.send(text, embed=emb)
    else:
        await answer.reply(text, embed=emb)


def return_send_trans(message):
    trans, lang = message
    emb = discord.Embed(color=discord.Color.green())
    emb.add_field(name=">>> " + trans, value="*" + lang + "*", inline=False)
    return emb


@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(
        f'Hello, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    emb = discord.Embed(title='Типо сообщение', color=discord.Color.green())
    emb.add_field(name='типо заголовок', value='типо текст', inline=False)
    await ctx.send(embed=emb)
    msg = await ctx.fetch_message(ctx.message.id)
    textC = msg.content
    await ctx.send(ctx.message)
    await ctx.send(msg)
    if ctx.message.reference and (msg := ctx.message.reference.resolved) and isinstance(msg, discord.Message):
        await ctx.send(msg.content)
    else:
        await ctx.send("You need to reply to an existing message")


@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def heeelp(ctx):
    text_1 = "Это БЕСПЛАТНЫЙ бот-переводчик. Он умеет переводить ваши сообщения. " \
             "Дабы никого не бесить восклицательными знаками и слешами, их тут просто нет"
    emb = discord.Embed(title=text_1, color=discord.Color.gold())
    text_2 = "__**Команды: (можно несколько через пробел)**__\n"
    text = "ан *(да, прямо по русски) - перевод на английский*\n" \
           "ис *- перевод на испанский*\n" \
           "нм *- перевод на немецкий*\n" \
           "фр *- перевод на французский*\n" \
           "яп *- перевод на японский*\n"
    text_1 = "**Также тeперь доступен перевод по ответу. Ответте на сообщение сообщением " \
             "c буквой 'п'. Сообщение будет переведено на русский, или ответте сообщением " \
             "'п ан', 'п фр' и т. д., будет отправлен перевод на соответствующий язык**\n" \
             "Команды нечувствительны к регистру\n"
    emb.add_field(name=text_2, value=text + text_1, inline=False)
    text_2 = "__**Commands: (multiple spaces are possible)**__\n"
    text = "ru *- translate to Russian*\n" \
           "en *- translate to English*\n" \
           "fr *- translate to French*\n" \
           "de *- translate to Deutsch*\n" \
           "es *- translate to Spanish*\n" \
           "ja *- translate to Japanese*\n"
    text_1 = "**Also translation by answer is now available. Reply to a message with a message " \
             "with the letter 't'. The message will be translated into Russian, or reply with a message " \
             "'t en', 't fr', etc., a translation into the appropriate language will be sent**\n" \
             "Commands are case insensitive\n"
    emb.add_field(name=text_2, value=text + text_1, inline=False)
    text = "Example:\n" \
           "es Hello\n" \
           "-> Hola"
    emb.add_field(name="ᅠ ᅠ ", value=text, inline=False)
    await ctx.send(embed=emb)


@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def versions(ctx):
    text_1 = "Exceptional Bot Versions"
    emb = discord.Embed(title=text_1, color=discord.Color.blue())
    text_2 = "__**0.1.0**__\n"
    text = "Created a bot, added basic ability to translate into Spanish and Russian"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "__**0.2.0**__\n"
    text = "Added main languages on the server, made translation without prefixes, added help menu"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "__**0.2.1**__\n"
    text = 'A "server" is made for the bot'
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "__**0.2.2**__\n"
    text = "Japanese language added, translation by response added, bot translated to another translator API"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "__**0.3.0**__\n"
    text = "Completely rewritten commands, made commands insensitive to case, added the ability to translate " \
           "into several languages, added this command"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "__**0.3.1**__\n"
    text = "Translation by answer can translate into several languages at once, bug fixed, status added"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "__**0.3.2**__\n"
    text = "Fix one bug and added 'Good morning' message)"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "~~__**0.3.2.1**__~~\n"
    text = "Added the ability to send messages about new levels to the bot"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "**(in developing)**\n"
    text = "Sending an ephemeral message with a translation"
    emb.add_field(name=text_2, value=text, inline=False)

    text = "__*The message will be deleted in a minute*__"
    emb.add_field(name="ᅠ ᅠ ", value=text, inline=False)
    message = await ctx.send(embed=emb)
    await asyncio.sleep(60)
    await message.delete()
    await ctx.message.delete()


f = open("password.txt", "r")
ff = f.read()
f.close()
if ff[-1] == "\n":
    ff = ff[:-1]

key = ff
if key == "":
    key = input("Please enter key: ")
code = "TcvbGqURw4Ze+CePNPK+ue6E4qKV0F3O2VAY9tuX6ii9Ff01v7AgcgLzTAxUb5rFnJ1vOPlfpBVhUN8=*5ZUPE2X7ILiMGig" \
       "mJhRqZg==*OpPlyOsMumnNIbYjFY8ecA==*6CfrkuNCcfOPGOvEkb9CuQ=="
token = cryptocode.decrypt(code, key)
if not not token:
    print("decryption successful")
    print("running on")
    bot.run(token)
else:
    print("key error")
