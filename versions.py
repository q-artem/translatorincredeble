import asyncio
import discord
from bot_init import bot


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

    text_2 = "__**0.5.0**__\n"
    text = "The code is divided into separate files, unnecessary functions are removed, all errors are removed"
    emb.add_field(name=text_2, value=text, inline=False)

    text_2 = "**(in developing)**\n"
    text = "Voice translation"
    emb.add_field(name=text_2, value=text, inline=False)

    text = "__*This message will be deleted in 2 minutes*__"
    emb.add_field(name="ᅠ ᅠ ", value=text, inline=False)
    message = await ctx.send(embed=emb)
    print("Send versions info message")
    await asyncio.sleep(120)
    await message.delete()
    await ctx.message.delete()
    print("Versions info message deleted")
