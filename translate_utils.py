import datetime
import os
from asyncio import sleep
from mutagen.mp3 import MP3
import discord
from sys import platform
from lingua import LanguageDetectorBuilder
from translate import Translator
from constants import DICT_LANG, LANGUAGES, DICT_OF_LANGUAGES, DICT_OF_RU_LANGUAGES, CHANNELS_FOR_TRANSLATE
from bot_init import bot
import gtts


def translation_information_string(a, b):  # генерация строки с информацией о языках
    try:
        c = DICT_LANG[a][0].upper() + DICT_LANG[a][1:] + " " + "(" + a + ")" + " " + "→" + " "
    except BaseException as e:
        c = a + " " + "→" + " " + str(e) * 0
    c1 = c
    try:
        c = c + DICT_LANG[b][0].upper() + DICT_LANG[b][1:] + " " + "(" + b + ")"
    except BaseException as e:
        c = c1 + b + str(e) * 0
    return c


def detect_lang(mess):  # определение языка текста
    detector = LanguageDetectorBuilder.from_languages(*LANGUAGES).build()
    lang_1 = detector.detect_language_of(str(" ".join(list(mess))))
    print("Detected land of {}".format(DICT_OF_LANGUAGES[lang_1]))
    return DICT_OF_LANGUAGES[lang_1]


def translate(on_l, args):  # перевод текста
    try:
        lang_1 = detect_lang(args)
    except KeyError:
        print("Unable to detect language")
        lang_1 = "en"
    text = str(" ".join(list(args)))
    if lang_1 != on_l:
        translator = Translator(from_lang=lang_1, to_lang=on_l)
        trans = translator.translate(text)
        is_translate = True
    else:
        trans = text
        is_translate = False
    print(f"Translate message from '{text}' to '{trans}'")
    return trans, translation_information_string(lang_1, on_l), is_translate


def update_activity_users(message_in):  # обновление времени последнего сообщения пользователя
    d = ""
    with open('last_messages.txt', 'r') as f:
        for q in f:
            if str(message_in.author.id) in q:
                d += q.split(" ")[0] + " " + str(datetime.datetime.today()) + "\n"
                continue
            d += q
    with open('last_messages.txt', 'w') as f:
        f.write(d)
    return True


async def send_trans(channel, message, answer=None, text="", sender="", in_channel=None):  # отправка перевода
    sender = "`" + sender
    if in_channel is None:
        sender += ":`\n"
    else:
        sender += ' in channel "' + in_channel.name + '":`\n'
    trans, lang = message
    while ("&lt;@" in trans) or ("&gt;" in trans):  # ищем упоминания пользователей
        num1 = trans.find("&lt;@")
        user = await bot.fetch_user(trans[num1 + 5:num1 + 5 + 18])
        username = user.name
        print("Name finding complete")
        trans = trans[:num1] + " @" + username + " " + trans[num1 + 5 + 18 + 4:]
    emb = discord.Embed(color=discord.Color.green())
    emb.add_field(name=sender * int(bool(len(sender) - 6)) + ">>> " + trans, value="*" + lang + "*", inline=False)
    if answer is None:
        await channel.send(text, embed=emb)
        print("Send additional translation complete")
    else:
        try:
            await answer.reply(text, embed=emb)
            print("Send translation complete")
        except BaseException as e:
            await channel.send(text, embed=emb)
            print("Send translation complete" + str(e) * 0)
    return True


async def check_levels_channel(message_in):
    if message_in.channel.id == 968102452417155162 and len(message_in.mentions) == 1:
        print("New message about level")
        level = message_in.content.split(" ")[-1][:-1]
        n = message_in.mentions[0]
        guild = bot.get_guild(955197429999861800)
        role0, role1, role3, role5, role7, role9 = guild.get_role(967760259131260928), guild.get_role(
            967753494352253029), guild.get_role(967758027769933824), guild.get_role(967758307534209064), guild.get_role(
            967758254920859688), guild.get_role(967758514233679883)
        if str(level) in "13579":
            if role9 not in n.roles:
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
        return "exit"


async def translate_by_answer(message_in):  # перевод сообщения по ответу
    message = message_in.content.lower()
    if message.split(" ")[0] == "п" or message.split(" ")[0] == "t":  # если префикс правильный
        print()
        list_keys = list()  # для всех нужных языков
        msg = message_in
        flag_err = False
        if len(message.split(" ")) == 1:  # если только один аргумент, то переводим на русский или английский
            if message.split(" ")[0].lower() == "п":
                list_keys.append("ru")
            else:
                list_keys.append("en")
        else:  # если несколько
            for q in range(len(message.split(" ")[1:])):  # идём по всем кроме первого
                if (message.split(" ")[1:][q] in DICT_OF_RU_LANGUAGES.values() or
                        message.split(" ")[1:][q] in DICT_OF_RU_LANGUAGES.keys()):  # если название нормальное
                    if message.split(" ")[1:][q] in DICT_OF_RU_LANGUAGES.values():
                        list_keys.append(message.split(" ")[1:][q])  # если сразу по-английски
                    else:
                        list_keys.append(DICT_OF_RU_LANGUAGES[message.split(" ")[1:][q]])  # если нет, ищем нормальный
                else:  # если хоть один неправильно, то всё
                    flag_err = True
                    break
        if flag_err:
            print("Incorrect command format")
            return "exit"  # удалить повторения
        if (message_in.reference and (msg := message_in.reference.resolved)
                and isinstance(msg, discord.Message)):  # если только это ответ
            await message_in.delete()
            warning_message = 0
            if len(list_keys) > 5:
                list_keys = list_keys[:5]
                warning_message = 1
            await send_trans(message_in.channel, translate(list_keys[0],
                                                           msg.content.split(" "))[:2],
                             answer=message_in.reference.resolved,
                             text="Maximum you can translate 5 languages" * warning_message)
            list_keys.pop(0)
            for q in list_keys:
                await send_trans(message_in.channel, translate(q, msg.content.split(" "))[:2])

    return "exit"


async def translate_text(message_in):  # перевод по команде
    message = message_in.content.lower()  # сообщение в нижнем регистре для команд
    list_keys = list()
    message_deleted = 0
    if len(message.split(" ")[0]) == 3 and message.split(" ")[0][-1] in "уd":  # если флажок на удаление
        message = message[:2] + message[3:]
        message_deleted = 1
        await message_in.delete()

    for q in range(len(message.split(" "))):  # идём по языкам
        if (message.split(" ")[q] in DICT_OF_RU_LANGUAGES.values() or
                message.split(" ")[q] in DICT_OF_RU_LANGUAGES.keys()):  # если название нормальное
            if message.split(" ")[q] in DICT_OF_RU_LANGUAGES.values():
                list_keys.append(message.split(" ")[q])  # если сразу по-английски
            else:
                list_keys.append(DICT_OF_RU_LANGUAGES[message.split(" ")[q]])  # если нет, ищем нормальный
        else:  # если хоть один неправильно, то всё
            break

    if len(list_keys) == 0:
        return "exit"

    warning_message = 0
    if len(list_keys) > 5:
        list_keys = list_keys[:5]
        warning_message = 1

    print()
    await send_trans(message_in.channel, translate(list_keys[0], message_in.content.split(" ")[len(list_keys):])[:2],
                     text="Maximum you can translate 5 languages" * warning_message,
                     sender=message_deleted * message_in.author.name)

    list_keys.pop(0)
    for q in list_keys:
        await send_trans(message_in.channel, translate(q, message_in.content.split(" ")[len(list_keys):])[:2])

    return "exit"


async def say_translate(message_in):  # произношение перевода в канал
    message = message_in.content.lower()  # сообщение в нижнем регистре для команд
    list_keys = list()

    if len(message.split(" ")[0]) == 3 and message.split(" ")[0][-1] in "гs":
        message = message[:2] + message[3:]
        await message_in.delete()

        for q in range(len(message.split(" "))):  # идём по языкам
            if message.split(" ")[q] in DICT_OF_RU_LANGUAGES.values() or message.split(" ")[q] in \
                    DICT_OF_RU_LANGUAGES.keys():  # если название нормальное
                if message.split(" ")[q] in DICT_OF_RU_LANGUAGES.values():
                    list_keys.append(message.split(" ")[q])  # если сразу по-английски
                else:
                    list_keys.append(DICT_OF_RU_LANGUAGES[message.split(" ")[q]])  # если нет, ищем нормальный
            else:  # если хоть один неправильно, то всё
                break

        if len(list_keys) == 0:
            return "exit"

        warning_message = 0
        if len(list_keys) > 5:
            list_keys = list_keys[:5]
            warning_message = 1

        print()

        name = (str(datetime.datetime.today()) + ".mp3").replace(":", "-")
        playing = list()
        audio_lens = list()

        if warning_message:
            war = await message_in.channel.send("Maximum you can translate 5 languages")
            await sleep(2)
            await war.delete()
            return

        channel = message_in.author.voice
        if channel is None:
            mess = await message_in.channel.send("You are not connected to a voice channel")
            await sleep(2)
            await mess.delete()
            return

        for q in range(len(list_keys)):
            tts = gtts.gTTS(translate(list_keys[q], message_in.content.split(" ")[len(list_keys):])[0],
                            lang=list_keys[q])
            name_1 = name[:-4] + "-" + str(q) + name[-4:]
            tts.save(name_1)
            str_1 = "ffmpeg"
            if platform == "win32":
                str_1 = r"C:\ffmpeg\bin\ffmpeg.exe"
            playing.append(discord.FFmpegPCMAudio(executable=str_1, source=name_1))
            audio = MP3(name_1)
            audio_lens.append(audio.info.length)

        channel = channel.channel

        await channel.connect()
        voice = message_in.guild.voice_client
        voice.volume = 200
        for q in range(len(list_keys)):
            voice.play(playing[q])
            await sleep(audio_lens[q] + 1)

        await voice.disconnect()
        for q in range(len(list_keys)):
            os.remove(name[:-4] + "-" + str(q) + name[-4:])

    return "exit"


async def translate_to_channels(message_in):
    if message_in.channel.category_id == 968100661721976852 or message_in.channel.category_id == 968961814744408124:
        return
    if message_in.content == "":
        return

    for q in CHANNELS_FOR_TRANSLATE.items():
        channel = bot.get_channel(q[-1])
        a, b, c = translate(q[0], message_in.content.split(" "))
        if c:
            await send_trans(channel, (a, b),
                             sender=message_in.author.name, in_channel=message_in.channel)
    print("Translations send to all channels")
    return "exit"
