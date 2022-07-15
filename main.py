from asyncio import sleep
import asyncio
import random
import datetime

from translate import Translator
from lingua import LanguageDetectorBuilder
import cryptocode
import discord
from discord.ext import commands
from constants import *

# ################## optional commands ################ #
import optional_commands
# ##################################################### #

'''def print(*args, **kwargs):
    pass'''


print("Libraries import completed")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.command()
@commands.has_permissions(administrator=True)
async def g_m(ctx):
    mess = random.choice(["Good morning)", "Good morning))", "Good morning!", r"Good morning! \♥‿\♥",
                          "Good morning!!", "Go" + "o" * random.randint(1, 7) + "d morning!!",
                          r"Good morning! \:)", r"Good morning \:)"])
    await ctx.send(mess)
    await ctx.message.delete()
    print(f"Send '{mess}' message")


@bot.command()
async def memberss(ctx):
    for guild in bot.guilds:
        for member in guild.members:
            await ctx.send(member.id)


@bot.event
async def on_member_join(member):
    with open('last_messages.txt', 'a') as f:
        f.write(str(member.id) + " " + str(datetime.datetime.today()) + "\n")
    channel = bot.get_channel(966246794428305429)
    await channel.send(str(member) + " join server")


@bot.event
async def on_member_remove(member):
    d = ""
    with open('last_messages.txt', 'r') as f:
        for q in f:
            if str(member.id) in q:
                continue
            d += q
    with open('last_messages.txt', 'w') as f:
        f.write(d)
    channel = bot.get_channel(966246794428305429)
    await channel.send(str(member) + " leave over server")


@bot.command()
@commands.has_permissions(administrator=True)
async def off_bot(ctx):
    message = await ctx.send("You kill me!! :(")
    await ctx.message.delete()
    await asyncio.sleep(1)
    await message.delete()
    print("Program interrupted")
    exit()


@bot.command()
@commands.has_permissions(administrator=True)
async def delete(ctx, *a):
    if int(a[0]) <= 5 or a[-1] == "True":
        await ctx.channel.purge(limit=int(a[0]) + 1)
        print(f"Delete {a[0]} messages in channel '{ctx.channel.name}'")
    else:
        await ctx.message.delete()
        print("Messages not deleted, no confirmation")


@bot.command()
@commands.has_permissions(administrator=True)
async def send(ctx):
    mess = ctx.message.content.split(" ")
    channel = ctx.channel
    mess_join = ""
    if len(mess[1]) == len(str(968166014594469888)):
        channel = bot.get_channel(int(mess[1]))
        mess_join = " ".join(mess[2:])
        await channel.send(mess_join)
    else:
        mess_join = " ".join(mess[1:])
        await channel.send(mess_join)
    await ctx.message.delete()
    print(f"Send message '{mess_join}' in channel '{channel.name}'")


@bot.event
async def on_ready():
    print('Сlient connected')
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game("вообще-то не играет... | !heeelp !versions"))
    print('Status complete')
    while True:  # для бана по неактивности
        with open('last_messages.txt', 'r') as f:
            for q in f:
                v = q.split(" ")[1].split("-")
                b = q.split(" ")[2].split(":")
                in_datetime = datetime.datetime(int(v[0]), int(v[1]), int(v[2]), hour=int(b[0]), minute=int(b[1]), second=int(b[2].split(".")[0]), microsecond=int(b[2].split(".")[1]))
                today_date = datetime.datetime.today()
                delta = today_date - in_datetime
                month = datetime.timedelta(days=31)
                if delta > month:
                    user = await bot.fetch_user(int(q.split(" ")[0]))
                    print(user, "Не писал ничего больше месяца!")
                    channel = bot.get_channel(966246794428305429)
                    await channel.send("Баним " + str(user) + "!")
                    # обновляем время
                    d = ""
                    with open('last_messages.txt', 'r') as f:
                        for q in f:
                            if str(user.id) in q:
                                d += q.split(" ")[0] + " " + str(datetime.datetime.today()) + "\n"
                                continue
                            d += q
                    with open('last_messages.txt', 'w') as f:
                        f.write(d)
        await sleep(30)


@bot.command()
async def stat(ctx, *args):
    if args[0] == "on":
        print('Status turn on')
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Game("вообще-то не играет... | !heeelp !versions"))
    elif args[0] == "off":
        print('Status turn off')
        await bot.change_presence(status=discord.Status.offline)
    else:
        stat = " ".join(args)
        print(f"Custom status '{stat}' complete")
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Game(stat + " | !heeelp !versions"))

@bot.command()
async def statt(ctx):
    print(ctx.message.content)

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
    text = str(" ".join(list(args)))
    g = translator.translate(text)
    print(f"Translate message from '{text}' to '{g}'")
    return g, mess_lang(lang_1, on_l)


async def send_trans(channel, message, answer=None, text=""):
    trans, lang = message
    while ("&lt;@" in trans) or ("&gt;" in trans):
        num1 = trans.find("&lt;@")
        user = await bot.fetch_user(trans[num1 + 5:num1 + 5 + len('711524916457111594')])
        username = user.name
        print("Name finding complete")
        trans = trans[:num1] + " @" + username + " " + trans[num1 + 5 + len('711524916457111594') + 4:]
    emb = discord.Embed(color=discord.Color.green())
    emb.add_field(name=">>> " + trans, value="*" + lang + "*", inline=False)
    if answer is None:
        await channel.send(text, embed=emb)
        print("Send additional translation complete")
    else:
        try:
            await answer.reply(text, embed=emb)
            print("Send translation complete")
        except BaseException:
            await channel.send(text, embed=emb)
            print("Send translation complete")


def return_send_trans(message):
    trans, lang = message
    emb = discord.Embed(color=discord.Color.green())
    emb.add_field(name=">>> " + trans, value="*" + lang + "*", inline=False)
    print("Перевод для отправки сформирован")
    return emb


@bot.event
async def on_message(message_in):
    # для отслеживания активности
    d = ""
    with open('last_messages.txt', 'r') as f:
        for q in f:
            if str(message_in.author.id) in q:
                d += q.split(" ")[0] + " " + str(datetime.datetime.today()) + "\n"
                continue
            d += q
    with open('last_messages.txt', 'w') as f:
        f.write(d)

    if message_in.channel.id == 968102452417155162 and len(message_in.mentions) == 1:
        print("New message about level")
        level = message_in.content.split(" ")[-1][:-1]
        n = message_in.mentions[0]
        guild = bot.get_guild(955197429999861800)
        role0, role1, role3, role5, role7, role9 = guild.get_role(967760259131260928), guild.get_role(967753494352253029), guild.get_role(967758027769933824), guild.get_role(967758307534209064), guild.get_role(967758254920859688), guild.get_role(967758514233679883)
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
        return

    if message_in.author == bot.user:
        return
    message = message_in.content.lower()
    num_min_lang = 0
    list_keys = list()
    msg = message_in

    if message.split(" ")[0] == "п" or message.split(" ")[0] == "t":  # перевод по ответу
        print()
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
    delete_message = False
    if len(message.split(" ")[0]) == 3 and message.split(" ")[0][-1] in "уd":
        message = message[:2] + message[3:]
        delete_message = True
        await message_in.delete()

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
        print()
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


@bot.command()
async def heeelp(ctx):
    await ctx.message.delete()
    text_1 = "Это БЕСПЛАТНЫЙ бот-переводчик. Он умеет переводить ваши сообщения. " \
             "Дабы никого не бесить восклицательными знаками и слешами, их тут просто нет"
    emb = discord.Embed(title=text_1, color=discord.Color.gold())
    text_2 = "__**Команды: (можно несколько через пробел)**__\n"
    text = "ан *(да, прямо по русски) - перевод на английский*\n" \
           "ис *- перевод на испанский*\n" \
           "нм *- перевод на немецкий*\n" \
           "фр *- перевод на французский*\n" \
           "яп *- перевод на японский*\n" \
           "Чтобы удалить переводимое сообщение, допишите букву 'у' к первому языку, например: 'ису ан Привет мир!'\n"
    text_1 = "**Перевод по ответу: ответте на сообщение сообщением " \
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
           "ja *- translate to Japanese*\n" \
           "To delete a translatable message, add a letter 'd' to the first language, for " \
           "example: 'rud fr Hello world!'\n"
    text_1 = "**Translation by answer: reply to a message with a message " \
             "with the letter 't'. The message will be translated into Russian, or reply with a message " \
             "'t en', 't fr', etc., a translation into the appropriate language will be sent**\n" \
             "Commands are case insensitive\n"
    emb.add_field(name=text_2, value=text + text_1, inline=False)
    text = "Example:\n" \
           "es Hello\n" \
           "-> Hola"
    emb.add_field(name=text, value="Current version: 0.4.0", inline=False)
    await ctx.send(embed=emb)


@bot.command()
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

    text_2 = "__**0.3.3**__\n"
    text = "Added the ability to send messages about new levels to the bot"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "__**0.4.0**__\n"
    text = "Code formatted, translation added followed by message removal, debugging features added, " \
           "some additional commands added, git has also been added to the project"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "__**0.4.1**__\n"
    text = "Translations now correctly display references"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "__**0.4.2**__\n"
    text = "Added ban for inactivity"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "**(in developing)**\n"
    text = "Sending an ephemeral message with a translation"
    emb.add_field(name=text_2, value=text, inline=False)

    text = "__*This message will be deleted in 2 minutes*__"
    emb.add_field(name="ᅠ ᅠ ", value=text, inline=False)
    message = await ctx.send(embed=emb)
    print("Send versions info message")
    await asyncio.sleep(120)
    await message.delete()
    await ctx.message.delete()
    print("Versions info message deletd")


if "" in "Расшифровка токена и запуск бота":
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
        print("Decryption password successful")
        print("Running on")
        bot.run(token)
    else:
        print("Key error")
