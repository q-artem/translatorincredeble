import cryptocode
from discord_components import DiscordComponents
# ################# Additional files ################## #

from optional_functions import *
from versions import *
from help_command import *
from translate_utils import *
# from tests import *

# ##################################################### #
print("Libraries import completed")


@bot.event
async def on_ready():
    print('Client connected')
    DiscordComponents(bot)
    print('Discord Components module ready')
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(STATE))
    print('Status complete')
    await ban_users()


@bot.event
async def on_message(message_in):
    for attach in message_in.attachments:
        if ".osr" == str(attach)[-4:]:
            print(True)
            print(message_in.content)
    if message_in.author == bot.user:
        return
    # для отслеживания активности
    update_activity_users(message_in)
    # прверка уровней
    if asyncio.create_task(check_levels_channel(message_in)) == "exit":
        return
    # перевод по ответу
    if asyncio.create_task(translate_by_answer(message_in)) == "exit":
        return
    # отправка в каналы
    if asyncio.create_task(translate_to_channels(message_in)) == "exit":
        return
    # перевод голосом в канал
    if asyncio.create_task(say_translate(message_in)) == "exit":
        return
    # перевод в остальных случаях
    asyncio.create_task(translate_text(message_in))

    await bot.process_commands(message_in)


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
