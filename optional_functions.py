import asyncio
import datetime
import random
from asyncio import sleep
import discord
from discord.ext import commands
from constants import STATE, STATE_COMMANDS
from bot_init import bot


@bot.command()
@commands.has_permissions(administrator=True)
async def off_bot(ctx):  # отключение бота
    message = await ctx.send("You kill me!! :(")
    await ctx.message.delete()
    await asyncio.sleep(1)
    await message.delete()
    print("Program interrupted")
    exit()
    return True


@bot.command()
@commands.has_permissions(administrator=True)
async def g_m(ctx):
    mess = random.choice(["Good morning)", "Good morning))", "Good morning!", r"Good morning! \♥‿\♥",
                          "Good morning!!", "Go" + "o" * random.randint(1, 7) + "d morning!!",
                          r"Good morning! \:)", r"Good morning \:)"])
    await ctx.send(mess)
    await ctx.message.delete()
    print(f"Send '{mess}' message")
    return True


def new_user_entry(member):  # запись нового пользователя в базу
    with open('last_messages.txt', 'a') as f:
        f.write(str(member.id) + " " + str(datetime.datetime.today()) + "\n")
    return True


def deleting_a_user(member):  # удаление человека при его выходе с сервера
    d = ""
    with open('last_messages.txt', 'r') as f:
        for q in f:
            if str(member.id) in q:
                continue
            d += q
    with open('last_messages.txt', 'w') as f:
        f.write(d)
    return True


@bot.event
async def on_member_join(member):  # присоединение человека к серверу
    new_user_entry(member)
    channel = bot.get_channel(966246794428305429)
    await channel.send(str(member) + " join server")
    return True


@bot.event
async def on_member_remove(member):  # выход человека с сервера
    deleting_a_user(member)
    channel = bot.get_channel(966246794428305429)
    await channel.send(str(member) + " leave over server")
    return True


@bot.command()
@commands.has_permissions(administrator=True)
async def delete(ctx, *a):  # удаление определённого количества сообщений
    if int(a[0]) <= 5 or a[-1] == "True":
        await ctx.channel.purge(limit=int(a[0]) + 1)
        print(f"Delete {a[0]} messages in channel '{ctx.channel.name}'")
    else:
        await ctx.message.delete()
        print("Messages not deleted, no confirmation")
    return True


@bot.command()
@commands.has_permissions(administrator=True)
async def send(ctx):  # отправка сообщения от имени бота
    mess = ctx.message.content.split(" ")
    channel = ctx.channel
    if len(mess[1]) == len(str(968166014594469888)):
        channel = bot.get_channel(int(mess[1]))
        mess_join = " ".join(mess[2:])
        await channel.send(mess_join)
    else:
        mess_join = " ".join(mess[1:])
        await channel.send(mess_join)
    await ctx.message.delete()
    print(f"Send message '{mess_join}' in channel '{channel.name}'")
    return True


async def ban_users():  # функция для отслеживания и удаления неактивных пользователей
    while True:
        with open('last_messages.txt', 'r') as f:
            for q in f:
                v = q.split(" ")[1].split("-")
                b = q.split(" ")[2].split(":")
                in_datetime = datetime.datetime(int(v[0]), int(v[1]), int(v[2]), hour=int(b[0]), minute=int(b[1]),
                                                second=int(b[2].split(".")[0]), microsecond=int(b[2].split(".")[1]))
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
                    with open('last_messages.txt', 'r') as ff:
                        for w in ff:
                            if str(user.id) in w:
                                d += w.split(" ")[0] + " " + str(datetime.datetime.today()) + "\n"
                                continue
                            d += w
                    with open('last_messages.txt', 'w') as ff:
                        ff.write(d)
            with open('last_messages.txt', 'r') as ff:
                file = ff.read()
            if len(bot.get_guild(955197429999861800).members) > len(file.split("\n")) - 1:
                for member in bot.get_guild(955197429999861800).members:
                    if str(member.id) not in file:
                        with open('last_messages.txt', 'a') as ff:
                            ff.write(str(member.id) + " " + str(datetime.datetime.today()) + "\n")

        await sleep(600)


@bot.command()
async def stat(*args):  # изменение статуса бота
    if args[0] == "on":
        print('Status turn on')
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Game(STATE))
    elif args[0] == "off":
        print('Status turn off')
        await bot.change_presence(status=discord.Status.offline)
    else:
        str_1 = " ".join(args)
        print(f"Custom status '{str_1}' complete")
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Game(str_1 + STATE_COMMANDS))
    return True
