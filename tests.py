import time
from datetime import datetime





'''
import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle

from main import bot


@bot.command()
async def test(ctx):
    msg = await ctx.send(
        embed = discord.Embed(title = 'Вы точно хотите перевевсти деньги?', timestamp = ctx.message.created_at),
        components = [
            Button(style = ButtonStyle.green, label = 'Да'),
            Button(style = ButtonStyle.red, label = 'Нет')
        ])
    responce = await bot.wait_for('button_click', check = lambda message: message.author == ctx.author)
    if responce.component.label == 'Да':
        await responce.respond(content = 'Деньги успешно переведены!')
    else:
        await responce.respond(content = 'Вы отменили перевод.')

'''
'''
import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle

client = commands.Bot(command_prefix = '.', intents = discord.Intents.all())
TOKEN = ''

@client.event
async def on_ready():
    DiscordComponents(client)
    print('Bot connected')

@client.command()
async def test(ctx):
    msg = await ctx.send(
        embed = discord.Embed(title = 'Вы точно хотите перевевсти деньги?', timestamp = ctx.message.created_at),
        components = [
            Button(style = ButtonStyle.green, label = 'Да'),
            Button(style = ButtonStyle.red, label = 'Нет')
        ])
    responce = await client.wait_for('button_click', check = lambda message: message.author == ctx.author)
    if responce.component.label == 'Да':
        await responce.respond(content = 'Деньги успешно переведены!')
    else:
        await responce.respond(content = 'Вы отменили перевод.')
'''


'''
import asyncio


async def test(asd: bool):
    time.sleep(2)
    if asd is True:
        print("true")
        return True
    else:
        print("not true")
        return False

print(1)
my_response = asyncio.run(test(asd=0))   # нашел такое решение работающее :)
print(my_response)
print(2)

'''



'''import discord
from discord_slash import SlashCommand, SlashContext
from main import bot'''

'''d = ""
with open('last_messages.txt', 'r') as f:
    for q in f:
        if "510181596150628376" in q:
            d += q.split(" ")[0] + " " + str(datetime.today()) + "\n"
            continue
        d += q
with open('last_messages.txt', 'w') as f:
    f.write(d)

    

print()'''



'''f.write(str(datetime.today()))
    f.write("\n")'''


'''@bot.command()
async def memberss(ctx):
    for guild in bot.guilds:
        for member in guild.members:
            await ctx.send(member.id)'''











# slash = SlashCommand(bot, sync_commands=True)


'''@slash.slash(name="t", description="Translation to russian", guild_ids=[955197429999861800],
             options=[create_option("Text", "Text to translate", required=True, option_type=3)])
async def trans(ctx: SlashContext, text):
    await ctx.send(return_send_trans(text))'''

'''@slash.slash(name="hello", description="Just Sends a Message", guild_ids=[691127432165589013], options=[create_option(name="text", description="Enter Anon Text", required=True, option_type=3)])
async def _hello(ctx:SlashContext, text:str):
  await ctx.send(text, hidden=True)'''

'''try:
    await message.add_reaction(message.content)
except BaseException:
    pass'''  # реакция

'''@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
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
        await ctx.send("You need to reply to an existing message")'''